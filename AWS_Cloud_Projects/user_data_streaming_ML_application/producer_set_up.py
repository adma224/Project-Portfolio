import requests
import json
import boto3
import uuid
import time
import random

# Replace 'your-region' with your AWS region and 'your-stream-name' with your Kinesis stream name
region_name = 'us-east-1'
stream_name = 'my-user-stream'

client = boto3.client('kinesis', region_name=region_name)
partition_key = str(uuid.uuid4())
number_of_results = 500

while True:
    r = requests.get(f'https://randomuser.me/api/?exc=login&results={number_of_results}')
    data = r.json()['results']

    random_user_index = int(random.uniform(0, (number_of_results - 1)))
    random_user = json.dumps(data[random_user_index])
    
    response = client.put_record(StreamName=stream_name, Data=random_user, PartitionKey=partition_key)
    time.sleep(random.uniform(0, 1))
