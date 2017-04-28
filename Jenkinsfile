pipeline {
  agent any
  stages {
    stage('Initialize Environments') {
      steps {
        parallel(
          "Initialize Env": {
            sh 'echo windowsxp'
            
          },
          "": {
            sh 'echo windowsxp'
            
          }
        )
      }
    }
    stage('Exit') {
      steps {
        echo 'Finished'
      }
    }
  }
}