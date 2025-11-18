pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials'
        IMAGE_NAME = 'Kaushal/hello-tops:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/kaushal-analyst/kaushal-CI-CD.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Test Docker Container') {
            steps {
                script {
                    docker.image("${IMAGE_NAME}").run('-d -p 5000:5000')
                    sh 'sleep 5'
                    sh 'curl -f http://localhost:5000 || echo "Test failed"'
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('', "${DOCKERHUB_CREDENTIALS}") {
                        docker.image("${IMAGE_NAME}").push()
                    }
                }
            }
        }
    }

    post {
        always {
            sh 'docker ps -a -q | xargs -r docker rm -f'
        }
    }
}
