import boto3
from botocore.exceptions import ClientError

# Connect to local S3 (in LocalStack)
s3 = boto3.client('s3',
    endpoint_url="http://localhost:4566",        # LocalStack S3 port
    aws_access_key_id="test",                    # Dummy key
    aws_secret_access_key="test",                # Dummy secret
    region_name="us-east-1"
)

bucket_name = "ahmed-bucket"
file_name = "hello.txt"
file_content = b"Hello from Ahmed's secure S3 bucket!"

# Step 1: Create a bucket
s3.create_bucket(Bucket=bucket_name)

# Step 2: Upload a file
s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)

# Step 3: Generate pre-signed URL
def create_presigned_url(bucket, key, expiration=3600):
    try:
        url = s3.generate_presigned_url("get_object",
                                        Params={"Bucket": bucket, "Key": key},
                                        ExpiresIn=expiration)
        return url
    except ClientError as e:
        print("Error generating URL:", e)
        return None

# Step 4: Use the function
url = create_presigned_url(bucket_name, file_name)
print(f"\n🔗 Pre-signed URL:\n{url}\n")
