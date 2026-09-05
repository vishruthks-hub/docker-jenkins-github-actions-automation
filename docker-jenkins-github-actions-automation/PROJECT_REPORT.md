# Minor Project Report
## Docker + Jenkins/GitHub Actions Automation Project

### Introduction
This project demonstrates a CI/CD automation workflow using GitHub, Docker, Trivy and GitHub Actions. Source code is obtained from GitHub, containerized into a Docker image, scanned for vulnerabilities and pushed to Docker Hub.

### Objectives
- Automate source-code retrieval from GitHub.
- Build a Docker image.
- Scan the Docker image using Trivy.
- Push the image to a Docker registry.
- Demonstrate practical CI/CD automation.

### Working
A push to the main branch triggers the GitHub Actions workflow. The workflow checks out the source code, prepares Docker Buildx, logs into Docker Hub using repository secrets, builds the image, scans it with Trivy and pushes the image to Docker Hub.

### Security
Docker credentials are stored as GitHub Secrets rather than being written into the workflow. Trivy scans for HIGH and CRITICAL vulnerabilities.

### Conclusion
The project demonstrates a practical containerized CI/CD pipeline covering source retrieval, Docker image creation, security scanning and registry publishing.
