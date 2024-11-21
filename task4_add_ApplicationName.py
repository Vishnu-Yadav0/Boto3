#update ApplicationName tag with name tag
import boto3
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_and_add_tags():
    ec2 = boto3.client('ec2')
    required_tag_key = 'ApplicationName'
    

    # Describe all instances
    instances = ec2.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}

            logger.info(f'Checking tags for instance {instance_id}')
            if required_tag_key not in tags:
                logger.info(f'Tag {required_tag_key} is missing from instance {instance_id}. Adding tag.')
                # Add the missing tag
                required_tag_value = tags['Name']
                ec2.create_tags(
                    Resources=[instance_id],
                    Tags=[{'Key': required_tag_key, 'Value': required_tag_value}]
                )
                logger.info(f'Tag {required_tag_key}={required_tag_value} added to instance {instance_id}.')
            else:
                logger.info(f'Tag {required_tag_key} already present on instance {instance_id}.')

if __name__ == '__main__':
    check_and_add_tags()
