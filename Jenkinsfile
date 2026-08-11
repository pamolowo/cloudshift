pipeline {
    agent any

    stages {
        stage('Build & Test') {
            steps {
                sh 'pip install pytest'
                sh 'pytest test_backup.py'
            }
        }

        stage('Deploy') {
            steps {
                sh 'git pull'
                sh 'python3 run_all.py'
            }
        }
    }
}
