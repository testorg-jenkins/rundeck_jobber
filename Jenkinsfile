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
 
        // Why not use the same script with additional parmater to start the job ?
	sh "${pwd()}/rundeck-scripts/rundeck_job.sh"

	// Call external Python script to get status of Rundeck job
        // project name and job id is hard-coded for testing convenience :-((
	sh "cd ${pwd()}/rundeck-scripts"
        sh "python ./getRundeckJobStatus.py pipeline_poc 5c970e5b-8d36-4a28-8b5f-905a9c81949e"
        
        // why this doesn't work ?
        // def rdjob_status = sh(returnStdout: true, script: 'python ./getRundeckJobStatus.py pipeline_poc 5c970e5b-8d36-4a28-8b5f-905a9c81949e')

        withEnv([ 
            "RDJOB_STATUS = rdjob_status"
        ])
    }

    stage(" =~=~= Collect Env vars... =~=~= ") {
        sh 'env > env_vars.txt'
        def envdump = readFile('env_vars.txt')
        echo "== START: Dump of enviroment variables =="
        echo "${envdump}"
        echo "== END: Dump of enviroment variables =="
    }
}

