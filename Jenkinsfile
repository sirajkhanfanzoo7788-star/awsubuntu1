pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credential-id') // <-- use the ID you just created
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
                sh """
                echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                docker tag myapp:latest sirajahmad77/awsubuntu1:latest
                docker push sirajahmad77/awsubuntu1:latest
                """
            }
        }

        stage('Run Docker Container') {
            steps {
                sh """
                docker stop myapp || true
                docker rm myapp || true
                docker run -d -p 5000:5000 --name myapp sirajahmad77/awsubuntu1:latest
                """
            }
        }
    }
}
