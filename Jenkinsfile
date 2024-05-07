pipeline {
    agent any

    stages {
        stage('Run Python Virtual Environment') {
            steps {
                    bat 'python -m venv venv'
                    bat ".\\venv\\Scripts\\activate.bat"
                    bat "python -m pip install --upgrade pip"
            }
        }
        stage('Run Python Scripts') {
            steps {
                    bat 'pip install -r requirements.txt'
                    bat 'python -m behave'
            }
        }
        stage('Run Pylint') {
            steps {

            bat 'pip install pylint'
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
