pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')  // every 2 mins
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Simranjangra31/assessement.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flask-app:latest .'
            }
        }

        stage('Run Container') {
            steps {
                bat '''
                docker stop flask-container
                docker rm flask-container
                docker run -d -p 5001:5001 --name flask-container flask-app:latest
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