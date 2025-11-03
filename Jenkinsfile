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
                    docker build -t priyapal345/final_assessment:latest .
                """
            }
        }

        stage('Login to Docker Hub') {
            steps {
                echo 'Logging into Docker Hub...'
                sh """
                    echo "Priya@doc" | docker login -u "priyapal345" --password-stdin
                """
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                echo 'Pushing image to Docker Hub...'
                sh """
                    docker push priyapal345/final_assessment:latest
                """
            }
        }

        stage('Deploy Container') {
            steps {
                echo 'Deploying container...'
                sh """
                    docker rm -f interesting_wozniak || true
                    docker run -d -p 5000:5000 --name interesting_wozniak priyapal345/final_assessment:latest
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

