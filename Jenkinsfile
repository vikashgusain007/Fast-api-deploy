pipeline {
    agent {
        docker {
            image 'python:3.9'
        }
    }
    environment {
        DOCKER_IMAGE = 'fastapi-celery-rabbitmq:latest'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
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
                    sh 'docker-compose down'
                }
            }
        }
    }
}
