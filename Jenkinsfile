pipeline {
    agent any 
    stages{
        stage("Test-Application"){
            steps{
                sh './scripts/test-application.sh'
            }
        }
        stage("Ansible"){
            steps{
                sh './scripts/ansible.sh'
            }
        }
        stage("Build-Images"){
            steps{
                sh './scripts/build-images.sh'
            }
        }
        stage("Deploy-Services"){
            steps{
                sh './scripts/deploy-services.sh'
            }
        }                   
        stage('Nginx'){
            steps{
                sh './scripts/nginx.sh'
            }
        }
    }
}