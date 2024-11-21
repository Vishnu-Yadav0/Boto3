# 3. Boto3 Sessions
# Sessions allow you to manage AWS credentials and configurations. A session represents a connection to AWS, and you can create multiple sessions if you need to manage multiple accounts or regions. Clients and resources are created from sessions. If you don’t explicitly create a session, Boto3 uses the default session.

# Example: Using a Session to Create a Client and Resource

import boto3

# Create a session
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY', #YOUR_ACCESS_KEY
    aws_secret_access_key='YOUR_SECRET_KEY', #YOUR_SECRET_KEY
    region_name='us-west-2'
)

# Create an S3 client from the session
s3_client = session.client('s3')

# Create an S3 resource from the session
s3_resource = session.resource('s3')

# List S3 buckets using the client
response = s3_client.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])

# List S3 buckets using the resource
for bucket in s3_resource.buckets.all():
    print(bucket.name)
