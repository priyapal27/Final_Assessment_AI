pipeline {
    agent any

    environment {
        // Jenkins credentials ID (must exist under Manage Jenkins → Credentials)
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')

        // Docker Hub details
        DOCKERHUB_USER = 'priyapal345'
        IMAGE_NAME = 'final_assessment'
        CONTAINER_NAME = 'interesting_wozniak'
        APP_PORT = '5000'
    }

    triggers {
        githubPush() // Trigger pipeline on GitHub push
    }

    stages {

        stage('Checkout') {
            steps {
                echo '📦 Cloning repository from GitHub...'
                // ✅ Replace with your actual GitHub URL
                git branch: 'main', url: 'https://github.com/priyapal27/Final_Assessment_AI.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                // ✅ Use bat if Jenkins runs on Windows
                script {
                    if (isUnix()) {
                        bat "docker build -t ${priyapal345}/${final_assessment}:latest ."
                    } else {
                        bat "docker build -t ${priyapal345}/${final_assessment}:latest ."
                    }
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                echo '🔐 Logging into Docker Hub...'
                script {
                    if (isUnix()) {
                        bat "echo '${Priya@doc}' | docker login -u '${priyapal345}' --password-stdin"
                    } else {
                        bat "echo ${Priya@doc} | docker login -u ${priyapal345} --password-stdin"
                    }
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                echo '📤 Pushing image to Docker Hub...'
                script {
                    if (isUnix()) {
                        bat "docker push ${priyapal345}/${final_assessment}:latest"
                    } else {
                        bat "docker push ${priyapal345}/${final_assessment}:latest"
                    }
                }
            }
        }

        stage('Deploy Container') {
            steps {
                echo '🚀 Deploying Docker container...'
                script {
                    if (isUnix()) {
                        sh """
                            docker rm -f ${interesting_wozniak} || true
                            docker run -d -p ${APP_PORT}:5000 --name ${interesting_wozniak} ${priyapal345}/${final_assessment}:latest
                        """
                    } else {
                        bat """
                            docker rm -f ${interesting_wozniak} || exit 0
                            docker run -d -p ${APP_PORT}:5000 --name ${interesting_wozniak} ${priyapal345}/${final_assessment}:latest
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful! Visit: http://localhost:${APP_PORT}"
        }
        failure {
            echo "❌ Deployment failed! Check the Jenkins console logs."
        }
    }
}
