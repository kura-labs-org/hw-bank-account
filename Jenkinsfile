node {    
    def app     
    stage('Clone repository') {               
        checkout scm    
    }     
    stage('Build image') {         
        app = docker.build("bankaccount:${env.BUILD_ID}")    
    }     
    stage('Push image') {
        app.push()          
    }
}