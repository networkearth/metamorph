# metamorph

## Setting Up the Bucket

Update the `cdk.json` then run:

```bash
pip install aws-cdk-lib==2.154.1
nvm install 22
cd bucket
cdk deploy
```

Then go create the `transforms` folder in the bucket created. 

## Getting Setup

```bash
aws configure sso
```

Make sure you set the default region for the CLI as well as sso. Also keep track of the profile name (I chose `admin` in the following).

```bash
pip install click
python get_creds.py --profile admin
```

That python script will just move your sso creds where glue is expecting them.

```bash
export AWS_PROFILE=admin
```

```
git clone git@github.com:awslabs/aws-glue-libs.git
cd aws-glue-libs
./bin/gluesparksubmit ../sample.py
```

The last command there will take a while as it is setting everything up for the first time.
