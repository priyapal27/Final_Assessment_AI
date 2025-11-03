pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')  // every 2 mins
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/priyapal27/Final_Assessment_AI.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t final_assessment .'
            }
        }

        stage('Run Container') {
            steps {
                bat '''
                docker stop interesting_wozniak
                docker rm interesting_wozniak
                docker run -d -p 5001:5001 --name interesting_wozniak final_assessment:latest
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Build and Deployment Successful!"
        }
        failure {
            echo "❌ Build failed. Please check the logs."
        }
    }
}