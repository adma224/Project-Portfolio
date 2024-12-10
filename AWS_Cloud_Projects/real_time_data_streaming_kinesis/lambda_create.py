import boto3
import lambda_function.py

# Initialize a boto3 client for Lambda
lambda_client = boto3.client('lambda', region_name='your-region')

# Define your Lambda function code
lambda_function_code = """
def lambda_handler(event, context):
    # Your code goes here
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
"""

# Create the Lambda function
response = lambda_client.create_function(
    FunctionName='MyLambdaFunction',
    Runtime='python3.8',  # Specify the Python runtime
    Role='arn:aws:iam::your-account-id:role/your-lambda-role',  # Specify the ARN for the IAM role
    Handler='lambda_function.lambda_handler',  # The file name and method name
    Code={
        'ZipFile': b'your zipped code'  # Your zipped code
    },
    Description='My new Lambda function',
    Timeout=15,  # Function timeout
    MemorySize=128,  # Memory size
)

print(response)
