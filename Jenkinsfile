node{
    stage('Python-Docker'){
        echo 'Hello World'
    }
    stage('SCM Checkout'){
        git 'https://github.com/lokesh8389/Python'
    }
	stage('python-build'){
	    sshPublisher(publishers: [sshPublisherDesc(configName: 'docker_server', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: 'docker build -t lokesh8389/my-app:${BUILD_NUMBER} .', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '//home//lokesh', remoteDirectorySDF: false, removePrefix: '', sourceFiles: 'Dockerfile, InsertScript.py')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
	}
	stage('python-run'){
	    sshPublisher(publishers: [sshPublisherDesc(configName: 'docker_server', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: 'docker rm -f python-app || true', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '//home//lokesh', remoteDirectorySDF: false, removePrefix: '', sourceFiles: 'Dockerfile, InsertScript.py'), sshTransfer(cleanRemote: false, excludes: '', execCommand: 'docker run --name python-app- --link my-sql lokesh8389/my-app:${BUILD_NUMBER}', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '//home//lokesh', remoteDirectorySDF: false, removePrefix: '', sourceFiles: '')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
	}
}
