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
        sh 'docker build -f Dockerfile .'
      }
    }

    stage('Login to Dockerhub') {
      environment {
        DOCKERHUB_USER = 'james18bt@gmail.com'
        DOCKERHUB_PASSWORD = 'linkinpark16'
      }
      steps {
        sh 'docker login -u $DOCKERHUB_USER -p $DOCKERHUB_PASSWORD'
      }
    }

  }
}