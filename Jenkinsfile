node {
    stage 'Preparing VirtualEnv'
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
	sh """
	. .env/bin/activate
	pip install -r requirements/test.txt
	"""
}