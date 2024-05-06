pipeline {
    agent any

    stages {
        stage('Run Python Scripts') {
            steps {
                    bat 'pip install -r requirements.txt'
                    bat 'python -m behave'
            }
        }
        stage('Run Pylint') {
            steps {
                    bat 'pylint  cat_api/ --rcfile=.pylintrc'
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
