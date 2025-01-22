pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'fastapi-celery-rabbitmq:latest'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run tests (you can add test stages as needed)
                    echo "Running tests..."
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Deploy using Docker Compose
                    sh 'docker-compose -f docker-compose.yml up -d'
                }
            }
        }
        stage('Clean Up') {
            steps {
                script {
                    // Stop and remove the Docker containers
                    sh 'docker-compose down'
                }
            }
        }
    }
}
