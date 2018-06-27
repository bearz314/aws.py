# aws.py
Slightly edited from Tomas' original version, the script can start/stop one AWS instance. Public IP is also provided when instance is started.

## Setup

#### 1. Requirements

The code is written in Python2. The Python package `boto` is required for interfacing with Amazon Web Services. Installation:
```
pip install boto
```

#### 2. AWS Keys

* You will need to generate an `AWS Access Key ID` and `AWS Secret Access Key`.
* Amazon best practices encourage an [IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) to be added, and AWS keys to be generated for that user instead of for the root account.
* You will need to grant permissions to manage EC2 containers to that new user.

#### 3. Create your EC2 instance

The script allows you to start/stop an instance, not to create one. You will need several information:
* Region (e.g. `eu-west-1` -- *Not to be confused with Availability Zone (e.g. `eu-west-1a`)*)
* Instance ID

## Usage


```
python aws.py {start|stop} [silent=False]
```

* Start instance: `python aws.py start`
* Stop  instance: `python aws.py stop`
* Optional: Add `true` to the back to suppress verbose messages

#### Sample

I love simplifying my workflow, so I've set up an alias in bash `alias ec2="python aws.py"`:

```
❯ ec2 start
Starting the instance...
Waiting for instance to run...
IP address:
18.191.193.251

❯
```

By suppressing other inputs, the IP can be piped or used otherwise:

```
❯ ec2 start true
18.191.193.251

❯
```

## Other stuffs

* Code largely written by Tomas. See his [blog post here](https://www.lisenet.com/2014/simple-python-script-to-start-and-stop-amazon-aws-instances/).
* After starting an instance, the public IP would change making SSH quite a challenge! Therefore the code is changed to output the address.
* More documentation on python boto [here](http://boto.readthedocs.io/en/latest/ref/ec2.html).
