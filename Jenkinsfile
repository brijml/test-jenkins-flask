pipeline {
    agent any
    stages{
        stage('Build'){
            steps{
            	if (!fileExists('testenv')){
                    echo 'Creating virtualenv ...'
                    sh 'virtualenv --no-site-packages testenv'
                }
                if (fileExists('requirements.txt')) {
                sh """
                . testenv/bin/activate
                pip install -r requirements.txt
                """
            	}
            }
        }
        stage('Test'){
            steps{
                sh """
                echo 'Running unittests...'
                python testapp.py
                """
            }
        }
    }
}