node {    
    def app     
    stage('Clone repository') {               
        checkout scm    
    }     
    stage('Build image') {     
        sh 'echo This is the current user ${USER}'    
        app = docker.build("barrezuetai/bankaccount:${env.BUILD_ID}")    
    }     
    stage('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', 'credentials-id') {
        app.push("latest")
    }        
    }
}