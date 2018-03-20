pipeline {
    agent none
    stages {
      stage('Regression Tests') {
        parallel {
          stage('Pro tests') {
            agent { label "master" }
              steps {
                echo 'Pro tests started'
                script {
                  testrun_id = 12345
                  writeFile file: 'automation/jenkins/testrun_id', text: "${testrun_id}"
                  }
                }
              post {
                success {
                  echo "Pro tests -- DONE"
                    }
                  }
              }

            stage('Pro2 Tests') {
              agent { label "master" }
                steps {
                  echo 'Pro2 tests started'
                  sh "ls -l"
                  }
                post {
                  success {
                    echo "Pro2 tests -- DONE"
                    }
                  }
                }
            } // End parallel
        post {
          always {
            echo "Post at end of parallel..."
            node('master') {
              sh 'echo "run something..."'
              regression_report = readFile("automation/jenkins/testrun_id")
              sh 'echo "${regression_report}"'
            }
          }
        } // end of post
      }
    } 
  }
 
