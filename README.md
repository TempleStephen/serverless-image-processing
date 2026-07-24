\# Serverless Image Processing System



\[!\[AWS](https://img.shields.io/badge/AWS-Lambda%20%7C%20S3%20%7C%20CloudWatch-232F3E?logo=amazon-aws\&logoColor=FF9900)](https://aws.amazon.com/)

\[!\[Python](https://img.shields.io/badge/Python-3.x-4FD1FF?logo=python\&logoColor=white)](https://www.python.org/)

\[!\[Architecture](https://img.shields.io/badge/Architecture-Event--Driven-8DA3BE)]()



An event-driven AWS pipeline that automatically processes images the moment they're uploaded to S3 — no servers to provision, patch, or scale.



\*\*Repo:\*\* \[github.com/TempleStephen/serverless-image-processing](https://github.com/TempleStephen/serverless-image-processing)

\*\*Author:\*\* \[Temple Stephen](https://www.linkedin.com/in/temple-stephen-74664a1b3/)



\---



\## Table of Contents



\- \[Overview](#overview)

\- \[Architecture](#architecture)

\- \[AWS Services Used](#aws-services-used)

\- \[Workflow](#workflow)

\- \[Project Structure](#project-structure)

\- \[Screenshots](#screenshots)

\- \[Skills Demonstrated](#skills-demonstrated)

\- \[Author](#author)



\---



\## Overview



This project demonstrates a serverless image processing workflow built entirely on AWS. Whenever an image is uploaded to an Amazon S3 bucket, an AWS Lambda function is triggered automatically. The function copies the uploaded image into a `processed/` folder and emits execution logs to CloudWatch for monitoring and debugging — all without a single server to manage.



\---



\## Architecture



!\[Architecture diagram showing the S3 to Lambda to processed folder pipeline](architecture/architecture-diagram.png)



\---



\## AWS Services Used



| Service | Role |

|---|---|

| \*\*Amazon S3\*\* | Stores incoming and processed images |

| \*\*AWS Lambda\*\* | Runs the image-processing logic on each upload |

| \*\*AWS IAM\*\* | Scopes permissions for the Lambda function and S3 access |

| \*\*Amazon CloudWatch\*\* | Captures execution logs and metrics for every run |



\---



\## Workflow



1\. \*\*Upload\*\* — A user uploads an image to the S3 bucket.

2\. \*\*Trigger\*\* — The upload fires an `ObjectCreated` event that invokes the Lambda function.

3\. \*\*Process\*\* — Lambda picks up the event and processes the image.

4\. \*\*Store\*\* — The processed image is copied into the `processed/` folder under a unique key.

5\. \*\*Log\*\* — CloudWatch records the execution for monitoring and troubleshooting.



\---



\## Project Structure



```

serverless-image-processing/

│

├── architecture/

│   └── architecture-diagram.png

│

├── screenshots/

│   ├── Policy.png

│   ├── Policy to role.png

│   ├── Lambad function role.png

│   ├── AmazonS3FullAccess.png

│   ├── Buckets.png

│   ├── File upload.png

│   ├── Trigger.png

│   ├── Lambda function code deploy.png

│   ├── Lambda function.png

│   └── Bucket-output.png

│

├── website/

│   ├── index.html

│   ├── style.css

│   └── script.js

│

├── lambda/

│   └── lambda\_function.py

│

├── README.md

└── .gitignore

```



\---



\## Screenshots



\### IAM Policy

!\[IAM policy document](screenshots/Policy.png)



\### Policy Attached to Role

!\[Policy attached to the Lambda execution role](screenshots/Policy%20to%20role.png)



\### Lambda Function Role

!\[Lambda function IAM role](screenshots/Lambad%20function%20role.png)



\### Amazon S3 Full Access Permission

!\[AmazonS3FullAccess permission](screenshots/AmazonS3FullAccess.png)



\### S3 Buckets

!\[S3 buckets list](screenshots/Buckets.png)



\### File Upload

!\[Image uploaded to S3](screenshots/File%20upload.png)



\### S3 Trigger

!\[S3 event trigger configuration](screenshots/Trigger.png)



\### Lambda Function Code Deployment

!\[Lambda function code deployed](screenshots/Lambda%20function%20code%20deploy.png)



\### Lambda Function

!\[Lambda function configuration](screenshots/Lambda%20function.png)



\### Processed Output

!\[Processed image in output bucket](screenshots/Bucket-output.png)



\---



\## Skills Demonstrated



`AWS Lambda` · `Amazon S3` · `IAM Permissions` · `CloudWatch Monitoring` · `Event-Driven Architecture` · `Python` · `Git` · `GitHub` · `Serverless Computing`



\---



\## Author



\*\*Temple Stephen\*\*

Aspiring AWS Solutions Architect passionate about building secure, scalable, and serverless cloud solutions.



\[!\[LinkedIn](https://img.shields.io/badge/LinkedIn-Temple%20Stephen-0A66C2?logo=linkedin\&logoColor=white)](https://www.linkedin.com/in/temple-stephen-74664a1b3/)

\[!\[GitHub](https://img.shields.io/badge/GitHub-serverless--image--processing-181717?logo=github\&logoColor=white)](https://github.com/TempleStephen/serverless-image-processing)

