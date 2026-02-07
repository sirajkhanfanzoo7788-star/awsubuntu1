pipeline {
    agent any

    environment {
        // Reference your Docker Hub credential ID here
        DOCKERHUB = credentials('dockerhub-credentials')
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/sirajkhanfanzoo7788-star/awsubuntu1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp:latest .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                echo $DOCKERHUB_PSW | docker login -u $DOCKERHUB_USR --password-stdin
                docker tag myapp:latest sirajahmad77/awsubuntu1:latest
                docker push sirajahmad77/awsubuntu1:latest
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                docker stop myapp || true
                docker rm myapp || true
                docker run -d -p 5000:5000 --name myapp sirajahmad77/awsubuntu1:latest
                '''
            }
        }
    }
}
