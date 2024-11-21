import boto3

# Initialize a session using Amazon EC2
ec2 = boto3.client('ec2')

# Specify the instance IDs you want to check the status for
instance_ids = ["i-0851d3e20686e4e69","i-0ce91ad117bab4c50","i-0ebbd798687fb256b","i-0d59cb15002ec6133"]

# Describe the instance status
response = ec2.describe_instances(InstanceIds=instance_ids)

# Print the status of each instance
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        status = instance['State']['Name']
        print(f'Instance ID: {instance_id}, State: {state}, Status: {status}')
