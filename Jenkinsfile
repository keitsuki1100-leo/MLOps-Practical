pipeline {
    agent any

    environment {
        PYTHON = 'python3'
    }

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
                sh 'pip install dvc pandas pyyaml'
            }
        }

        stage('Preprocess') {
            steps {
                echo 'Preprocessing data...'
                sh 'python src/preprocess.py'
            }
        }

        stage('Train') {
            steps {
                echo 'Training model...'
                sh 'python src/train.py'
            }
        }

        stage('Evaluate') {
            steps {
                echo 'Evaluating model...'
                sh 'python src/evaluate.py'
            }
        }

        stage('DVC Push') {
            steps {
                echo 'Pushing data to DVC storage...'
                sh 'dvc push'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed!'
        }
    }
}