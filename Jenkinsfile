pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python packages...'
                bat 'C:\\Users\\MAYANK\\Desktop\\MLOps-Practical\\.venv\\Scripts\\pip.exe install dvc pandas pyyaml'
            }
        }

        stage('Preprocess') {
            steps {
                echo 'Preprocessing data...'
                bat 'C:\\Users\\MAYANK\\Desktop\\MLOps-Practical\\.venv\\Scripts\\python.exe src\\preprocess.py'
            }
        }

        stage('Train') {
            steps {
                echo 'Training model...'
                bat 'C:\\Users\\MAYANK\\Desktop\\MLOps-Practical\\.venv\\Scripts\\python.exe src\\train.py'
            }
        }

        stage('Evaluate') {
            steps {
                echo 'Evaluating model...'
                bat 'C:\\Users\\MAYANK\\Desktop\\MLOps-Practical\\.venv\\Scripts\\python.exe src\\evaluate.py'
            }
        }

        stage('DVC Push') {
            steps {
                echo 'Pushing data to DVC storage...'
                bat 'C:\\Users\\MAYANK\\Desktop\\MLOps-Practical\\.venv\\Scripts\\python.exe -m dvc push'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed!'
        }
    }
}