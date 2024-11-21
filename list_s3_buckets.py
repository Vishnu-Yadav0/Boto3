import boto3

#list S3 Buckets using client

# s3_client = boto3.client('s3')
# response = s3_client.list_buckets()
# for bucket in response['Buckets']:
#     print(bucket['Name'])

s3_resource = boto3.resource('s3')

response = s3_resource.buckets.all()

for bucket in response:
    print(bucket.name)