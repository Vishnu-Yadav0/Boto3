import boto3
def list_iam_users():
    iam_client = boto3.client('iam')
    paginator = iam_client.get_paginator('list_users')
    users=[]
    for page in paginator.paginate():
        for user in page['Users']:
            users.append([user['UserName'],user['UserId'],user['Arn']])
    return users

iam_users = list_iam_users()
for user_details in iam_users:
    for _ in user_details:
        print(f'Username: {user_details[0]} ; UserID: {user_details[1]} ; ARN: {user_details[2]}')
        break


# import boto3
# aws_management_console = boto3.session.Session(profile_name = "default")
# iam_console = aws_management_console.resource('iam')

# for each_user in iam_console.users.all():
#     print(each_user.name)