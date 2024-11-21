import boto3
ec2 = boto3.client('ec2')

instance_id="i-0ce91ad117bab4c50"

response = ec2.terminate_instances(InstanceIds=[instance_id])

for instance in response['TerminatingInstances']:
      print(f'Instance ID: {instance["InstanceId"]}, Previous State: {instance["PreviousState"]["Name"]}, Current State: {instance["CurrentState"]["Name"]}')



  
