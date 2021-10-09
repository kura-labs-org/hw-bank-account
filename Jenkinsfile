node {    
    def app     
    stage('Clone repository') {               
        checkout scm    
    }     
    stage('Build image') {     
        sh 'echo This is the current user ${USER}'    
        app = docker.build("bankaccount:${env.BUILD_ID}")    
    }     
    stage('Push image') {
        docker.withRegistry('barrezuetai/bankaccount', 'credentials-id') {
        app.push()
    }        
    }
}