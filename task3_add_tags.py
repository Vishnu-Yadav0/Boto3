#update tags to all the ec2 instances based on name tag

import boto3

def check_and_add_tags():
    ec2_client = boto3.client('ec2')

    required_tag_key = 'Name'

    #Describe all instances
    instances = ec2_client.describe_instances()
    
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
            print(f'Printing tags for instance {instance_id}')
            print(f'before: {tags}')

            if required_tag_key in tags:
                required_tag_value=tags[required_tag_key].split('-')[0]
                ec2_client.create_tags(
                    Resources=[instance_id],
                    Tags=[{'Key': required_tag_key, 'Value': required_tag_value}]
                )
                print(f'after: {tags}\n')
if __name__=='__main__':
    check_and_add_tags()