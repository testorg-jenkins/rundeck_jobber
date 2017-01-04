// Rundeck's CLI tool is installed in master
node('master') {

    stage(" =~ Archive Sources =~ "){
        timestamps {
            checkout scm
            stash name: "rundeck-scripts"
        }
    }

    stage(' =~ Rundeck Tasks =~ ') {

        dir("rundeck-scripts") {
           unstash "rundeck-scripts"
        }
 
	dir ("rundeck-scripts") {
	    sh "./rundeck_job.sh"

	    // Call external Python script to get status of Rundeck job
            // project name and job id is hard-coded for testing convenience :-((
            // Why not use the same script with additional parmater to start the job ?
            sh "python ./getRundeckJobStatus.py pipeline_poc 5c970e5b-8d36-4a28-8b5f-905a9c81949e"
        
            // why this doesn't work ?
            // def rdjob_status = sh(returnStdout: true, script: 'python ./getRundeckJobStatus.py pipeline_poc 5c970e5b-8d36-4a28-8b5f-905a9c81949e')

            def rdjob_file = fileExists('jobinfo.txt')

            if (rdjob_file) {
                def rdjob_status = readFile('jobinfo.txt')
                echo "Status of rundeck job (parsed from jobinfo) ==>"
                echo "${rdjob_status}"
            }
        }

        // Cleanup stashed sources
	dir ("rundeck-scripts") {
            deleteDir()
        }
    }
}
