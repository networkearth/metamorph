import subprocess
import json

import click

@click.command()
@click.option('--profile', help='AWS profile name', required=True)
def get_creds(profile):
    creds = json.loads(subprocess.getoutput(f'aws configure export-credentials --profile {profile}'))
    with open('/root/.aws/credentials', 'w') as f:
        f.write(f'[{profile}]\n')
        f.write(f'aws_access_key_id = {creds["AccessKeyId"]}\n')
        f.write(f'aws_secret_access_key = {creds["SecretAccessKey"]}\n')
        f.write(f'aws_session_token = {creds["SessionToken"]}\n')
    

if __name__ == '__main__':
    get_creds()