import boto3
import json
import time

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

try:
    # Create the role
    iam_client.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(assume_role_policy)
    )

    # Attach a policy to the role
    policy_arn = 'arn:aws:iam::aws:policy/AmazonKinesisFullAccess'
    iam_client.attach_role_policy(
        RoleName=role_name,
        PolicyArn=policy_arn
    )

    print("IAM Role Created:", role_name)

    # Create an IAM instance profile
    instance_profile_name = role_name
    iam_client.create_instance_profile(InstanceProfileName=instance_profile_name)
    print("IAM Instance Profile Created:", instance_profile_name)

    # Add role to the instance profile
    iam_client.add_role_to_instance_profile(
        InstanceProfileName=instance_profile_name,
        RoleName=role_name
    )

except Exception as e:
    print(f"Error creating IAM role or instance profile: {e}")

# Wait for the instance profile to be available
time.sleep(10)  # Adjust the timing as necessary