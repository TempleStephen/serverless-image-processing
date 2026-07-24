"""
AWS Lambda handler triggered by S3 ObjectCreated events.

Copies each newly-uploaded object into a "processed/" prefix in the
configured output bucket, tagging the new key with a UUID to avoid
collisions, and reports per-record success/failure back to the caller.
"""

import logging
import os
import uuid
from typing import Any
from urllib.parse import unquote_plus  # NEW

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOG_LEVEL", "INFO"))

OUTPUT_BUCKET = os.environ.get("OUTPUT_BUCKET")
PROCESSED_PREFIX = os.environ.get("PROCESSED_PREFIX", "processed/")

s3 = boto3.client("s3")


class ConfigurationError(RuntimeError):
    """Raised when required environment configuration is missing."""


def _require_output_bucket() -> str:
    if not OUTPUT_BUCKET:
        raise ConfigurationError("OUTPUT_BUCKET environment variable is not set")
    return OUTPUT_BUCKET


def _build_destination_key(source_key: str) -> str:
    """Generate a collision-free key in the processed/ prefix."""
    return f"{PROCESSED_PREFIX}{uuid.uuid4()}-{source_key}"


def _process_record(record: dict[str, Any], output_bucket: str) -> dict[str, Any]:
    """Copy a single S3 event record into the output bucket."""
    source_bucket = record["s3"]["bucket"]["name"]

    # Decode URL-encoded object key from S3
    source_key = unquote_plus(record["s3"]["object"]["key"])  # NEW

    destination_key = _build_destination_key(source_key)

    logger.info(
        "Copying s3://%s/%s -> s3://%s/%s",
        source_bucket,
        source_key,
        output_bucket,
        destination_key,
    )

    s3.copy_object(
        Bucket=output_bucket,
        Key=destination_key,
        CopySource={
            "Bucket": source_bucket,
            "Key": source_key,
        },
    )

    return {
        "sourceBucket": source_bucket,
        "sourceKey": source_key,
        "destinationBucket": output_bucket,
        "destinationKey": destination_key,
        "status": "success",
    }


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    """Entry point: process every S3 record in the incoming event."""
    output_bucket = _require_output_bucket()

    records = event.get("Records", [])
    if not records:
        logger.warning("No Records found in event; nothing to process")
        return {"processed": 0, "failed": 0, "results": []}

    results: list[dict[str, Any]] = []
    failures = 0

    for record in records:
        try:
            results.append(_process_record(record, output_bucket))
        except ClientError as exc:
            failures += 1
            error_message = exc.response["Error"]["Message"]
            logger.error("Failed to copy object: %s", error_message, exc_info=True)
            results.append(
                {
                    "status": "failed",
                    "error": error_message,
                    "record": record,
                }
            )
        except KeyError as exc:
            failures += 1
            logger.error(
                "Malformed S3 event record, missing key: %s",
                exc,
                exc_info=True,
            )
            results.append(
                {
                    "status": "failed",
                    "error": f"Malformed record: {exc}",
                    "record": record,
                }
            )

    logger.info(
        "Processed %d record(s), %d failure(s)",
        len(results) - failures,
        failures,
    )

    return {
        "processed": len(results) - failures,
        "failed": failures,
        "results": results,
    }