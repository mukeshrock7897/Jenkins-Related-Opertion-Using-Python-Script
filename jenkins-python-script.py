from jenkinsapi.jenkins import Jenkins
import jenkins
import os


def get_server_instance():
    
    # user account Authentication Credentials
    jenkins_url = 'http://localhost:8080'
    server = jenkins.Jenkins(jenkins_url, username = 'mukeshrock7897', password = '***********')
    
    # # Get information about the user account that authenticated to Jenkins
    data = server.get_whoami()
    print("Logged In User Full Name ",data['fullName'])
    print("Logged In User Id ",data['id'])
    
    # # Create a new Jenkins job
    server.create_job('Md Junaid', jenkins.EMPTY_CONFIG_XML)
    
    # Return the name of a job
    print("Get the Name of a Job ",server.get_job_name('New Extra Job Created'))
    
    # Check whether a job exists
    print("Check if job is Exists",server.job_exists('New Extra Job Created'))
    
    # Rename an existing Jenkins job
    print("Change the Jenkins Job Name ",server.rename_job('from_name', 'to_name'))
    
    # Delete Jenkins job permanently
    print("Delete the existing jobs from Jenkins",server.delete_job(name))
    
    # Get the number of jobs on the Jenkins server
    print("Get The Jobs Count in Jenkins ",server.jobs_count())
    
    # Get information on this Master or item on Master This information includes job list and view information and can be used to retreive information on items such as job folders
    print("Get Job list and view info ",server.get_info())

    return server
def get_job_details():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    for j in server.get_jobs():
        job_instance = server.get_job(j[0])
        print ('Job Name:%s' %(job_instance.name))
        print ('Job Description:%s' %(job_instance.get_description()))
        print ('Is Job running:%s' %(job_instance.is_running()))
        print ('Is Job enabled:%s' %(job_instance.is_enabled()))
        
def get_plugin_details():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    for plugin in server.get_plugins().values():
        print ("Short Name:%s" %(plugin.shortName))
        print ("Long Name:%s" %(plugin.longName))
        print ("Version:%s" %(plugin.version))
        print ("URL:%s" %(plugin.url))
        print ("Active:%s" %(plugin.active))
        print ("Enabled:%s" %(plugin.enabled))
def jenkins_user_creation():
    
    #method 1
    command = '$echo "jenkins.model.Jenkins.instance.securityRealm.createAccount('Vivo20', 'vivo12345')" | java -jar /home/mukesh/Downloads/jenkins-cli.jar -s http://localhost:8080 -auth mukeshrock7897:****** -noKeyAuth groovy ='
    os.sytem(command)
    
    # method 2
    # first create .sh file in same folder where your python script are avaiable 
    #example test.sh and write below command
    
    #!/bin/sh
    
    # "jenkins.model.Jenkins.instance.securityRealm.createAccount('NewUsername', 'NewUSerPassword')" | java -jar /home/mukesh/Downloads/jenkins-cli.jar -s http://localhost:8080 -auth ADMIN:ADMINPASSWORD -noKeyAuth groovy =
    echo "jenkins.model.Jenkins.instance.securityRealm.createAccount('Vivo20', 'vivo12345')" | java -jar /home/mukesh/Downloads/jenkins-cli.jar -s http://localhost:8080 -auth mukeshrock7897:mukMUK@123 -noKeyAuth groovy =
    
    #Now call the test.sh file in python script like below given
    os.system("sh test.sh")
    
if __name__ == '__main__':
    get_server_instance()
    get_job_details()
    get_plugin_details()
    jenkins_user_creation()
