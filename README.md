# metamorph

## Setup

You'll need to grab the `aws-glue-libs` repo (I typically put it in the `metamorph` directory):

```bash
git clone git@github.com:awslabs/aws-glue-libs.git
```

Then you'll need to install `metamorph` and its dependencies:

```bash
nvm install 22
pip install -r requirements.txt
pip install -e .
```

## Creating and Testing a Glue Transform 

You'll need two things for the transform - a python file and json config of the same name. 
You can checkout `metamorph/transforms/add_depth_class.py` and `metamorph/transforms/add_depth_class.json` for an example.

Similarily you can create a test file. See `metamorph/tests/test_add_depth_class.py` for an example.

To run a test you'll first need to be signed into AWS.

```bash
aws configure sso
export AWS_PROFILE=admin
watercycle login admin
```

(Note that you can choose a different profile name than `admin`)

Once you're signed in you can run a command like the following (assuming you are in the `aws-glue-libs` directory):

```bash
./bin/gluesparksubmit ..metamorph/tests/test_add_depth_class.py
```

## Deploying a Glue Transform

You'll need to have a bucket setup to store the transforms. You can use the `bucket` directory to create a bucket with the necessary permissions.

Update the `cdk.json` in the `buckets` directory and then run:

```bash
cd bucket
cdk deploy
```

Then go create the `transforms` folder in the bucket created. 

Deploying a transform is now as simple as uploading your `.py` and `.json` files to the `transforms` folder in the bucket which you can do through the AWS console. 

