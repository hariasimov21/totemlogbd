pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/hariasimov21/totemlogbd', branch: 'master')
      }
    }

    stage('listar') {
      steps {
        sh 'ls -la'
      }
    }

  }
}