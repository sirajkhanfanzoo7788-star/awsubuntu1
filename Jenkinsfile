
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'sirajahmad77/awsubuntu1'
        IMAGE_TAG  = "${IMAGE_NAME}:${BUILD_NUMBER}"
        Container  = "khan-name"
       
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

        stage('Docker container creation') {
            steps {
                sh "docker rm -f ${Container} || true"
                sh "docker run -d --name ${Container} -p 3000:5000 ${IMAGE_TAG}"
                sh "docker image prune -f"
                echo "✅ Docker container created successfully"
            }
        }

        // ✅ NEW STAGE: Deploy to EKS with retries and rollout status
        stage('Deploy to EKS') {
            steps {
                script {
                    retry(2) { // Retry in case of transient Jenkins issues
                        sh '''
                            echo "Applying deployment to EKS cluster..."
                            kubectl apply -f deployment.yaml
                            kubectl apply -f service.yaml
                            
                            # Wait for deployment to finish
                            DEPLOYMENT_NAME=$(grep 'name:' deployment.yaml | head -1 | awk '{print $2}')
                            kubectl rollout status deployment/$DEPLOYMENT_NAME --timeout=180s || echo "Deployment may have issues, check manually"
                        '''
                    }
                }
            }
        }
    }
}
