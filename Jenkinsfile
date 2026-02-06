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
                script {
                    docker.build('myapp:latest')
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove previous container if exists
                    docker.stop('myapp') || true
                    docker.rm('myapp') || true
                    
                    // Run new container
                    docker.run('myapp:latest', '-d -p 5000:5000 --name myapp')
                }
            }
        }
    }
}
