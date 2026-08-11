pipeline {
    agent any

    stages {
        stage('Build & Test') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install pytest
                    .venv/bin/python -m pytest test_backup.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    python3 run_all.py
                '''
            }
        }
    }
}