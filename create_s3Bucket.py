import boto3
s3 = boto3.client('s3')

#create a new s3 bucket
bucket_name = "dev9381"

response = s3.create_bucket(Bucket=bucket_name)

print(f'Bucket {bucket_name} created')