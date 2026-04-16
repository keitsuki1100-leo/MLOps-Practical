pipeline {
    agent any

    stages {
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
    }
}