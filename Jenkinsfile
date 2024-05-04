pipeline {
    agent any

    stages {
        stage('Run Python Scripts') {
            steps {
                    bat 'pip install -r requirements.txt'
                    bat 'python -m behave'
            }
        }
        stage('reports') {
            steps {
                script {
                    allure ([
                        includeProperties: false,
                        jdk:'',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'reports/allure']]
                    ])
                 }
            }
        }
    }
}
