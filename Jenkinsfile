pipeline {
    agent any

    environment {
        DOCKER_USERNAME = credentials('dockerhub-username') // Your Docker Hub username
        DOCKER_PASSWORD = credentials('dockerhub-password') // Your Docker Hub password
        IMAGE_NAME = 'sirajahmad77/awsubuntu1:latest'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/sirajkhanfanzoo7788-star/awsubuntu1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t myapp:latest .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                docker tag myapp:latest $IMAGE_NAME
                docker push $IMAGE_NAME
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                docker stop myapp || true
                docker rm myapp || true
                docker run -d -p 5000:5000 --name myapp myapp:latest
                '''
            }
        }
    }
}
