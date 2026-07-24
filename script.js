/**
 * Serverless Image Processing Project
 * Temple Stephen — https://www.linkedin.com/in/temple-stephen-74664a1b3/
 */

(function () {
  "use strict";

  const project = {
    name: "Serverless Image Processing System",
    stack: ["Amazon S3", "AWS Lambda", "IAM", "CloudWatch"],
    author: "Temple Stephen",
    linkedin: "https://www.linkedin.com/in/temple-stephen-74664a1b3/",
  };

  function logBanner() {
    const style = "color:#4fd1ff;font-family:monospace;font-weight:600;";
    console.log("%c%s", style, project.name);
    console.log(
      "%cStack: %s",
      "color:#8da3be;font-family:monospace;",
      project.stack.join(" → ")
    );
    console.log(
      "%cBuilt by %s — %s",
      "color:#8da3be;font-family:monospace;",
      project.author,
      project.linkedin
    );
  }

  document.addEventListener("DOMContentLoaded", logBanner);
})();