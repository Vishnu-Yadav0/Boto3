import boto3
import time

def list_iam_users():
    # Create an IAM client
    iam_client = boto3.client('iam')
    
    # List IAM users
    paginator = iam_client.get_paginator('list_users')
    users = []
    for page in paginator.paginate():
        for user in page['Users']:
            users.append(user['UserName'])
    
    return users

def get_user_access_details(user_name):
    iam_client = boto3.client('iam')
    
    # Generate service last accessed details for the user
    response = iam_client.generate_service_last_accessed_details(
        Arn=f'arn:aws:iam::851725540108:user/{user_name}'
    )
    
    job_id = response['JobId']
    
    # Wait for the job to complete
    while True:
        job_status = iam_client.get_service_last_accessed_details(JobId=job_id)['JobStatus']
        if job_status == 'COMPLETED':
            break
        time.sleep(1)  # wait for 1 second before checking the status again
    
    # Get the service last accessed details
    details = iam_client.get_service_last_accessed_details(JobId=job_id)
    return details['ServicesLastAccessed']

def main():
    # List IAM users
    users = list_iam_users()
    
    # For each user, get their access advisor details
    for user in users:
        print(f"User: {user}")
        access_details = get_user_access_details(user)
        for detail in access_details:
            print(f"  Service: {detail['ServiceName']}, Last Accessed: {detail.get('LastAuthenticated', 'N/A')}")
        print()

if __name__ == "__main__":
    main()
