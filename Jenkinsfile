pipeline {
    agent any

    environment {
        // Jenkins credential ID for DockerHub (Username + Password)
        DOCKERHUB_USR = credentials('dockerhub-credentials').username
        DOCKERHUB_PSW = credentials('dockerhub-credentials').password
        IMAGE_NAME = "sirajahmad77/awsubuntu1:latest"
        CONTAINER_NAME = "myapp"
        APP_PORT = "5000"
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo "Cloning GitHub repository..."
                git branch: 'main', url: 'https://github.com/sirajkhanfanzoo7788-star/awsubuntu1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh "docker build -t ${CONTAINER_NAME}:latest ."
            }
        }

        stage('Docker Login & Push') {
            steps {
                echo "Logging into DockerHub and pushing image..."
                sh '''
                    echo "$DOCKERHUB_PSW" | docker login -u "$DOCKERHUB_USR" --password-stdin
                    docker tag ${CONTAINER_NAME}:latest ${IMAGE_NAME}
                    docker push ${IMAGE_NAME}
                '''
            }
        }

        stage('Stop & Remove Existing Container') {
            steps {
                echo "Stopping and removing existing container if any..."
                sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "Running container on port ${APP_PORT}..."
                sh "docker run -d -p ${APP_PORT}:${APP_PORT} --name ${CONTAINER_NAME} ${IMAGE_NAME}"
            }
        }

    }

    post {
        success {
            echo "Pipeline completed successfully! Your app is running on port ${APP_PORT}."
        }
        failure {
            echo "Pipeline failed. Check the logs above for errors."
        }
    }
}
