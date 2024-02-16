pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello, this is a simple Jenkins pipeline!'
            }
        }
    }
}
