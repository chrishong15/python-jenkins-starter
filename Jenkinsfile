pipeline {
  agent {
    docker {
      image 'python:3.12'
      args '-u root'
    }
  }

  options { timestamps(); ansiColor('xterm') }

  environment {
    PIP_CACHE_DIR = "${WORKSPACE}/.pip-cache"
    COVERAGE_DIR  = "reports/coverage_html"
    JUNIT_XML     = "reports/junit/*.xml"
  }

  stages {
    stage('Setup') {
      steps {
        sh '''
          python -V
          python -m pip install -U pip
          python -m pip install -e ".[dev]"
          # pre-commit can fail if hooksPath is set; clear it for CI
          git config --unset-all core.hooksPath || true
          pre-commit install || true
        '''
      }
    }

    stage('Lint & Typecheck') {
      steps {
        sh '''
          ruff check .
          black --check .
          mypy .
        '''
      }
    }

    stage('Tests (parallel)') {
      parallel {
        stage('Unit') {
          steps {
            sh '''
              mkdir -p reports/junit ${COVERAGE_DIR}
              pytest -q \
                 --junitxml=reports/junit/unit.xml \
                 --cov=src/app --cov-report=xml:reports/coverage.xml \
                 --cov-report=html:${COVERAGE_DIR} \
                 -k "not slow"
            '''
          }
        }
        stage('Slow/Integration') {
          steps {
            sh '''
              mkdir -p reports/junit
              pytest -q \
                 --junitxml=reports/junit/integration.xml \
                 -m "slow" || true
            '''
          }
        }
      }
    }

    stage('(Optional) Build Docker Image') {
      when { expression { return env.DOCKERHUB_USERNAME?.trim() } }
      steps {
        sh '''
          IMAGE="${DOCKERHUB_USERNAME}/python-jenkins-starter:${BUILD_NUMBER}"
          echo "Building ${IMAGE}"
          docker build -t "${IMAGE}" .
          echo "${DOCKERHUB_TOKEN}" | docker login -u "${DOCKERHUB_USERNAME}" --password-stdin
          docker push "${IMAGE}"
          echo "IMAGE=${IMAGE}" > image.env
        '''
      }
    }
  }

  post {
    always {
      junit testResults: "${JUNIT_XML}", allowEmptyResults: true
      publishHTML target: [
        reportDir: "${COVERAGE_DIR}",
        reportFiles: 'index.html',
        reportName: 'Coverage (HTML)',
        keepAll: true,
        alwaysLinkToLastBuild: true
      ]
      archiveArtifacts artifacts: 'reports/**/*, image.env', allowEmptyArchive: true
    }
  }
}
