pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials'
        IMAGE_NAME = 'kaushal/hello-tops'
        CONTAINER_NAME = 'hello-tops-container'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/kaushal-analyst/kaushal-CI-CD.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:latest ."
                }
            }
        }

        stage('Stop Old Container') {
            steps {
                script {
                    sh """
                    docker ps -q --filter "name=${CONTAINER_NAME}" | grep -q . && docker stop ${CONTAINER_NAME} || echo 'No running container'
                    docker ps -aq --filter "name=${CONTAINER_NAME}" | grep -q . && docker rm ${CONTAINER_NAME} || echo 'No container to remove'
                    """
                }
            }
        }

        stage('Run New Container') {
            steps {
                script {
                    sh """
                    docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest
                    """
                }
            }
        }

        stage('Test Application') {
            steps {
                script {
                    sh "sleep 5"
                    sh "curl -f http://localhost:5000"
                }
            }
        }

      

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed! Check the logs."
        }
    }
}

