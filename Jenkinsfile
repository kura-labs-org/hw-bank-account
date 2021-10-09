node {    
    def app     
    stage('Clone repository') {               
        checkout scm    
    }     
    stage('Build image') {         
        app = docker.build()    
    }     
    stage('Push image') {
        app.push()          
    }
}