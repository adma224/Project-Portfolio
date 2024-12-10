import boto3
import json

# Initialize the IAM client
iam_client = boto3.client('iam')

# Create an IAM role
role_name = 'stream-role'
assume_role_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Effect': 'Allow',
        'Principal': {'Service': 'ec2.amazonaws.com'},
        'Action': 'sts:AssumeRole'
    }]
}

role_response = iam_client.create_role(
    RoleName=role_name,
    AssumeRolePolicyDocument=json.dumps(assume_role_policy)
)

# Attach a policy to the role (using a pre-defined AWS managed policy for demonstration)
policy_arn = 'arn:aws:iam::aws:policy/AmazonKinesisFullAccess'
iam_client.attach_role_policy(
    RoleName=role_name,
    PolicyArn=policy_arn
)

print("IAM Role Created:", role_name)
