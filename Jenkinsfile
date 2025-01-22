pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'fastapi-celery-rabbitmq:latest'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    echo "Running tests..."
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh 'docker-compose -f docker-compose.yml up -d'
                }
            }
        }
        stage('Clean Up') {
            steps {
                script {
                    echo "Deployment completed..."
                }
            }
        }
    }
}
