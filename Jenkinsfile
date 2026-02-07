pipeline {
    agent any

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
