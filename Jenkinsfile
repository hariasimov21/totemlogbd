pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/hariasimov21/totemlogbd', branch: 'master')
      }
    }

    stage('listar') {
      parallel {
        stage('listar') {
          steps {
            sh '''ls -la

pwd'''
          }
        }

        stage('ruta') {
          steps {
            sh 'pwd'
          }
        }

      }
    }

    stage('build') {
      steps {
        sh 'docker build -f /Dockerfile .'
      }
    }

  }
}