import boto3

def describe_ec2_instances():
    # Create a boto3 session
    session = boto3.Session()

    # Create an EC2 client
    ec2_client = session.client('ec2')

    # Describe EC2 instances
    response = ec2_client.describe_instances()

    # Iterate over the instances and print details
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}")
            print(f"Instance Type: {instance['InstanceType']}")
            print(f"State: {instance['State']['Name']}")
            print(f"Public IP: {instance.get('PublicIpAddress', 'N/A')}")
            print("Tags:")
            if 'Tags' in instance:
                for tag in instance['Tags']:
                    print(f"  {tag['Key']}: {tag['Value']}")
            print("-" * 60)

if __name__ == "__main__":
    describe_ec2_instances()
    #calling describe ec2 instances function in main

