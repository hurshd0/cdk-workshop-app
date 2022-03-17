
# CDK Python Project Demo App

This app logs path `/hello`, `/hi` to dynamodb and displays it as HTML website. 

To try the demo visit [CDKWorkshop](https://cdkworkshop.com/)

## Prerequisites

1. Setup Admin user `cdk-workshop` with AdminAccess
2. Configure aws credentials
3. Check Node.js version is >= 10.13.0, if not update it 
4. Install CDK toolkit `npm install -g aws-cdk` & Check CDK version `cdk --version` is >= 2.0.0
5. Check Python is >= 3.6
## Setup 

1. Git clone the repository

2. Activate the virtualenv

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

3. Sythesize the CloudFormation template
At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

4. Deploy the stack

```
$ cdk deploy
```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
