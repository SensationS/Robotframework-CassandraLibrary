pipeline {
  agent any
  stages {
    stage('Initialize Environments') {
      steps {
        input(message: 'are you sure to build', id: '1', ok: 'yes')
      }
    }
  }
}