pipeline {
    agent any

    environment {
        PYTHON = 'python'
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
                bat 'pip install dvc pandas pyyaml'
            }
        }

        stage('Preprocess') {
            steps {
                echo 'Preprocessing data...'
                bat 'python src/preprocess.py'
            }
        }

        stage('Train') {
            steps {
                echo 'Training model...'
                bat 'python src/train.py'
            }
        }

        stage('Evaluate') {
            steps {
                echo 'Evaluating model...'
                bat 'python src/evaluate.py'
            }
        }

        stage('DVC Push') {
            steps {
                echo 'Pushing data to DVC storage...'
                bat 'dvc push'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed!'
        }
    }
}