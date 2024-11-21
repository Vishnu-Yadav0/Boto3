#Use boto3 in python and create the EC2 instance in AWS

import boto3

ec2_resource = boto3.resource('ec2')

Instance_details ={
    'ImageId': 'ami-04b70fa74e45c3917',  # Replace with a valid AMI ID
    'InstanceType': 't2.micro',           # Replace with desired instance type
    'MinCount': 1,
    'MaxCount': 1,
    'TagSpecifications': [{
        'ResourceType': 'instance',
        'Tags': [{
            'Key': 'Name',
            'Value': 'Boto3Instance'
        }]
    }]
}

instances =  ec2_resource.create_instances(**Instance_details)

instance_id  = instances[0].id
print(f'Created instance with ID: {instance_id}')