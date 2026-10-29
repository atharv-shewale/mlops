pipeline {
    agent any

    environment {
        PATH = "C:\\Users\\athar\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\Users\\athar\\AppData\\Local\\Microsoft\\WindowsApps;${env.PATH}"
        IMAGE_NAME = "mlops-hello-uat"
        IMAGE_TAG  = "latest"
    }

    stages {
        stage('Run Pytest Verification') {
            steps {
                echo 'Executing Pytest unit verification (Item 11)...'
                bat 'python -m pytest'
            }
        }

        stage('Evidently AI Drift Check') {
            steps {
                echo 'Executing Evidently AI Monitoring check (Item 12)...'
                bat 'python evidently_monitor.py'
            }
        }

        stage('Docker Build Image') {
            steps {
                echo 'Building lightweight Python Docker image (Items 8, 9 & 10)...'
                bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .'
            }
        }

        stage('Docker Container Deployment') {
            steps {
                echo 'Deploying application container on Docker...'
                bat '''
                    docker rm -f mlops-app-uat 2>nul || ver>nul
                    docker run -d -p 8000:8000 --name mlops-app-uat %IMAGE_NAME%:%IMAGE_TAG%
                '''
            }
        }
    }

    post {
        always {
            echo 'UAT Jenkins Pipeline Execution Finished.'
        }
        success {
            echo '=== [RESULT: PASS] Application successfully tested and deployed on Docker via Jenkins! ==='
        }
        failure {
            echo '=== [RESULT: FAIL] Pipeline encountered an error. Check console output. ==='
        }
    }
}
