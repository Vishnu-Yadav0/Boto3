#list all the ec2 instances, check and  validate tag of 'environment'
import boto3
import json

def check_tags():
    ec2 = boto3.client('ec2')
    required_tag_key = 'Environment'

    #Describe all instances
    instances = ec2.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            tags = {tag['Key']:tag['Value'] for tag in instance.get('Tags', [])}
            print(f'Checking tags for instance {instance_id}')
            if required_tag_key not in tags:
                print(f'Tag {required_tag_key} is missing from instance {instance_id}\n')
            else:
                print(f'Tag {required_tag_key} is found from instance {instance_id}\n')

if __name__ == '__main__':
    check_tags()