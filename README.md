# Docker + Jenkins/GitHub Actions Automation Project

## Objectives
1. Pull code from GitHub
2. Build a Docker image
3. Scan the Docker image using Trivy
4. Push the Docker image to Docker Hub

## Tools
GitHub, GitHub Actions, Docker, Trivy, Docker Hub, Jenkins.

## Project Structure
- app/app.py
- Dockerfile
- requirements.txt
- .dockerignore
- .github/workflows/ci.yml
- Jenkinsfile
- PROJECT_REPORT.md
- README.md

## Run Locally
docker build -t docker-jenkins-demo .
docker run -p 5000:5000 docker-jenkins-demo

Open http://localhost:5000

## GitHub Actions Setup
Create a GitHub repository and upload these files.
In GitHub go to Settings -> Secrets and variables -> Actions.
Create:
DOCKERHUB_USERNAME = your Docker Hub username
DOCKERHUB_TOKEN = your Docker Hub access token

Push to the main branch. The workflow checks out the code, builds the image, scans it with Trivy, and pushes it to Docker Hub.

## Submission
After creating the GitHub repository, submit its URL in both the Comment section and Minor Project Submission Link.
