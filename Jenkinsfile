pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')   // Jenkins credentials ID
        DOCKERHUB_USER = 'priyapal345'                            // Docker Hub username
        IMAGE_NAME = 'final_assessment'
        CONTAINER_NAME = 'interesting_wozniak'
        APP_PORT = '5000'
    }

    triggers {
        githubPush() // Trigger on push to GitHub
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository from GitHub...'
                git branch: 'main', url: 'https://github.com/priyapal27/Final_Assessment_AI.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh """
                    docker build -t ${DOCKERHUB_USER}/${IMAGE_NAME}:latest .
                """
            }
        }

        stage('Login to Docker Hub') {
            steps {
                echo 'Logging into Docker Hub...'
                sh """
                    echo "${DOCKERHUB_CREDENTIALS_PSW}" | docker login -u "${DOCKERHUB_CREDENTIALS_USR}" --password-stdin
                """
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                echo 'Pushing image to Docker Hub...'
                sh """
                    docker push ${DOCKERHUB_USER}/${IMAGE_NAME}:latest
                """
            }
        }

        stage('Deploy Container') {
            steps {
                echo 'Deploying container...'
                sh """
                    docker rm -f ${CONTAINER_NAME} || true
                    docker run -d -p ${APP_PORT}:5000 --name ${CONTAINER_NAME} ${DOCKERHUB_USER}/${IMAGE_NAME}:latest
                """
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful!"
        }
        failure {
            echo "❌ Deployment failed!"
        }
    }
}

