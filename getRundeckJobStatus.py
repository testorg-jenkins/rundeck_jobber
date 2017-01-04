#!/usr/bin/env python

import subprocess
import sys

## Globals...
rd_cli = "rd "
outformat = " -% " + "\"%id %status %href\" "

def getJobStatus(rd_project, job_uuid):

    rdcmd = rd_cli + "executions query  -p " + rd_project + " -i " + job_uuid + outformat + " -m 1 "

    rdcmd_out = subprocess.check_output([rdcmd], shell=True, stderr=subprocess.STDOUT)

    ## expected output sample : 'succeeded'
    rdjob_status = rdcmd_out.split(' ')[1]

    print("{0} job hosted in {1} project within Rundeck {2}".format(job_uuid, rd_project, rdjob_status))

    return None


def main():

    project = sys.argv[1]
    jobid   = sys.argv[2]

    getJobStatus(project, jobid)



if __name__ == "__main__":
    main()

