import boto3  # AWS SDK (Software Development Kit) for Python
from botocore.exceptions import ClientError

def create_presigned_url(bucket_name, object_name, expiration=3600):
    """
    Generate a pre-signed URL to share an S3 object.

    Args:
        bucket_name (str): Name of your S3 bucket
        object_name (str): Name of the file inside the bucket
        expiration (int): Time in seconds for the URL to remain valid

    Returns:
        str: Pre-signed URL as a string. If error, returns None.
    """
    # Create an S3 client
    s3_client = boto3.client('s3')

    try:
        # Generate the URL for downloading
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        print(f"Error generating URL: {e}")
        return None

    return response

# Example usage
if __name__ == "__main__":
    bucket = "your-bucket-name"
    file_name = "example.pdf"
    url = create_presigned_url(bucket, file_name)
    if url:
        print("🔗 Pre-signed URL:", url)
