pipeline {
    agent any

    environment {
        IMAGE_NAME = "YOUR_DOCKERHUB_USERNAME/docker-jenkins-demo"
    }

    stages {
        stage('Pull Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER .'
            }
        }

        stage('Scan Image with Trivy') {
            steps {
                sh 'trivy image --severity HIGH,CRITICAL --exit-code 0 $IMAGE_NAME:$BUILD_NUMBER'
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker tag $IMAGE_NAME:$BUILD_NUMBER $DOCKER_USER/docker-jenkins-demo:latest
                        docker push $DOCKER_USER/docker-jenkins-demo:latest
                    '''
                }
            }
        }
    }
}
