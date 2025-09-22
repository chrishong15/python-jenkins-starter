pipeline {
  agent {
    docker {
      image 'python:3.12'
      args '-u root' // allow pip installs
    }
  }
  options { timestamps(); ansiColor('xterm') }
  environment {
    PIP_DISABLE_PIP_VERSION_CHECK = '1'
    PYTHONUNBUFFERED = '1'
  }
  stages {
    stage('Setup') {
      steps {
        sh 'python -V'
        sh 'python -m pip install -U pip'
        sh 'python -m pip install -e ".[dev]"'
        sh 'pre-commit install || true'
      }
    }
    stage('Lint') {
      steps {
        sh 'ruff check .'
        sh 'black --check .'
        sh 'mypy src'
      }
    }
    stage('Test') {
      steps {
        sh 'pytest -q --junitxml=test-results/junit.xml --cov=app --cov-report=xml:coverage.xml'
      }
    }
  }
  post {
    always {
      junit 'test-results/junit.xml'
      archiveArtifacts artifacts: 'coverage.xml', onlyIfSuccessful: false
    }
  }
}
