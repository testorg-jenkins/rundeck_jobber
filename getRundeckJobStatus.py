#!/usr/bin/env python

import subprocess
import os
import sys

## Globals...
rd_cli = "rd "
outformat = " -% " + "\"%id %status %href\" "
os.environ['RD_URL'] = 'http://54.202.181.216:4440/api/18'
os.environ['RD_TOKEN'] = 'SBrHrDFwDHr9PMcBI1V3AsKhk6YoIf3J'

def getJobStatus(rd_project, job_uuid):

    rdcmd = rd_cli + "executions query  -p " + rd_project + " -i " + job_uuid + outformat + " -m 1 "

    rdcmd_out = subprocess.check_output([rdcmd], shell=True, stderr=subprocess.STDOUT)

    ## expected output sample : 'succeeded'
    rdjob_status = rdcmd_out.split(' ')[1]

    print()
    print(" ==> Status of latest run for job with UUID, {0}, in Rundeck project, {1} : {2}".format(job_uuid, rd_project, rdjob_status))

    with open('jobinfo.txt', 'w') as rdjob:
        rdjob.write(rdjob_status)

    return None


def main():

    project = sys.argv[1]
    jobid   = sys.argv[2]

    print(" ==> Using env settings for Rundeck CLI: ")
    os.system('echo $RD_URL')
    os.system('echo $RD_TOKEN')

    getJobStatus(project, jobid)



if __name__ == "__main__":
    main()

