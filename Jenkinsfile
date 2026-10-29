pipeline {
    agent any

    environment {
        IMAGE_NAME = "mlops-hello-uat"
        IMAGE_TAG  = "latest"
    }

    stages {
        stage('Checkout Source') {
            steps {
                echo 'Checking out source code from Git repository...'
                checkout scm
            }
        }

        stage('Run Local Pytest') {
            steps {
                echo 'Executing Pytest unit verification...'
                sh '''
                    python3 -m pip install -q pytest
                    python3 -m pytest -v test_hello.py -s
                '''
            }
        }

        stage('Evidently AI Monitor Dry Run') {
            steps {
                echo 'Executing Evidently AI Monitoring & Drift check...'
                sh '''
                    python3 -m pip install -q -r requirements.txt
                    python3 evidently_monitor.py
                '''
            }
        }

        stage('Docker Build Image') {
            steps {
                echo 'Building lightweight Python Docker image...'
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Docker Container Execution') {
            steps {
                echo 'Running Hello.py inside Docker Container...'
                sh '''
                    docker run --rm ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }
    }

    post {
        always {
            echo 'UAT Pipeline Dry Run Completed.'
            archiveArtifacts artifacts: '*.html', allowEmptyArchive: true
        }
        success {
            echo '=== [RESULT: PASS] UAT Pipeline passed all checks successfully! ==='
        }
        failure {
            echo '=== [RESULT: FAIL] Pipeline encountered an error in UAT environment. ==='
        }
    }
}
