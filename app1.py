pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                // Run the build steps here
                sh 'echo "Running build"'
            }
        }
    }  
        
}
