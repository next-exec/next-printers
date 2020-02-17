pipeline {
    agent {
        kubernetes {
            cloud 'cdn2.ttp.codes'
            inheritFrom 'docker-agent'
        }
    }

    stages {
        stage('Build') {
            steps {
                container('docker') {
                    sh 'docker build -t=quay.io/ttpcodes/next-printers:latest-arm .'
                }
            }
        }

        stage('Deploy') {
            steps {
                container('docker') {
                    sh 'docker push quay.io/ttpcodes/next-printers:latest-arm'
                }
            }
        }
    }
}
