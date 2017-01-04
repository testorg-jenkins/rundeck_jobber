node('linux') {
    stage(' =~ Start Rundeck Job =~ ') {
        // Why not use the same script with additional parmater to start the job ?
	sh "rundeck_job.sh"
    }
    stage(' =~ Rundeck Job Check =~ ') {

	// Call external Python script to get status of Rundeck job
        // project name and job id is hard-coded for testing convenience :-((
        def rdjob_status = sh(returnStdout: true, script: 'python getRundeckJobStatus.py pipeline_poc 5c970e5b-8d36-4a28-8b5f-905a9c81949e')
        withEnv([
           "RDJOB_STATUS = rdjob_status"
        )]
    }
    stage(" =~=~= Collect Env vars... =~=~= ") {
        // Collect and print all env variables
        sh 'env > env_vars.txt'
        def envdump = readFile('env_vars.txt')
        echo "== START: Dump of enviroment variables =="
        echo "${envdump}"
        echo "== END: Dump of enviroment variables =="
    }
}
