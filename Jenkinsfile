pipeline {
    agent any

    environment {
        IMAGE_NAME = 'sirajahmad77/awsubuntu1'          // Your Docker Hub repo
        IMAGE_TAG  = "${IMAGE_NAME}:${BUILD_NUMBER}"   // Unique image per build
    }

    stages {

        stage('Checkout') {
            steps {
                git url: 'https://github.com/sirajkhanfanzoo7788-star/awsubuntu1', branch: 'main'
                sh 'ls -ltr'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin"
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_TAG} ."
                sh "docker tag ${IMAGE_TAG} ${IMAGE_NAME}:latest"
                echo "✅ Docker image built successfully"
                sh "docker images"
            }
        }

        stage('Push Docker Image') {
            steps {
                sh "docker push ${IMAGE_TAG}"
                sh "docker push ${IMAGE_NAME}:latest"
                echo "✅ Docker image pushed successfully"
            }
        }

        stage('Deploy to EKS (Auto-update App)') {
            steps {
                script {
                    retry(2) {
                        sh """
                            echo "Updating kubeconfig..."
                            aws eks update-kubeconfig --region us-east-1 --name test-cluster

                            echo "Applying Kubernetes manifests..."
                            kubectl apply -f deployment.yaml
                            kubectl apply -f service.yaml

                            echo "Auto-updating app with new image..."
                            kubectl set image deployment/awsubuntu-app awsubuntu=${IMAGE_TAG}

                            echo "Waiting for rollout to finish..."
                            kubectl rollout status deployment/awsubuntu-app --timeout=180s
                        """
                    }
                }
            }
        }

    }
}
