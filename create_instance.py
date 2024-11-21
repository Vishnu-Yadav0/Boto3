import boto3

ec2 = boto3.resource('ec2')

#create a new EC2 instance
instances = ec2.create_instances(
    ImageId='ami-04b70fa74e45c3917',
    InstanceType = 't2.micro',
    KeyName="amazonLinux.pem",
    MinCount=1,
    MaxCount=1,

)

for instance in instances:
    print(f'created instance with ID:{instance.id} ')
