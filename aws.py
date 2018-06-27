# /usr/bin/python2.7
# written by Tomas (www.lisenet.com) on 05/11/2012
# edited  by Bearz314 on 27/06/2018
# copyleft free software

import boto.ec2
import sys

from time import sleep

# specify AWS keys
auth = {"aws_access_key_id": "INSERT_KEY_HERE", "aws_secret_access_key": "INSERT_KEY_HERE"}

def main():
    # read arguments from the command line and
    # check whether at least two elements were entered
    usageErr = "Usage: python aws.py {start|stop} [silent=False]\n"

    if len(sys.argv) < 2:
	    print(usageErr)
	    sys.exit(0)
    else:
	    action = sys.argv[1]

    global silent
    try:
        # if third arg exists, check if need to suppress outputs
        silent = True if sys.argv[2].lower()=="true" else False
    except:
        silent = False


    if action == "start":
	    startInstance()
    elif action == "stop":
    	stopInstance()
    else:
    	print(usageErr)


def startInstance():
    printChk("Starting the instance...")

    # change "eu-west-1" region if different
    try:
        ec2 = boto.ec2.connect_to_region("eu-west-1", **auth)

    except Exception, e1:
        error1 = "Error1: %s" % str(e1)
        print(error1)
        sys.exit(0)

    # change instance ID appropriately
    try:
         listInst = ec2.start_instances(instance_ids="i-12345678")

    except Exception, e2:
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0)

    # get IP address - update at least once to get IP
    printChk("Waiting for instance to run...")
    while True:
        listInst[0].update()
        if listInst[0].state == 'running':
            break
        sleep(3)


    printChk("IP address: ")
    sys.stdout.write(listInst[0].ip_address)

def stopInstance():
    printChk("Stopping the instance...")

    try:
        ec2 = boto.ec2.connect_to_region("eu-west-1", **auth)

    except Exception, e1:
        error1 = "Error1: %s" % str(e1)
        print(error1)
        sys.exit(0)

    try:
         ec2.stop_instances(instance_ids="i-12345678")

    except Exception, e2:
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0)

def printChk(string):
    if not silent:
        print(string)

if __name__ == '__main__':
    main()
