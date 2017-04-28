pipeline {
  agent any
  stages {
    stage('error') {
      steps {
        retry(count: 3) {
          echo 'Test'
          sleep 3
        }
        
      }
    }
  }
}