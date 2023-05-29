import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Read HTML file
    with open('index.html', 'rb') as f:
        html_file = f.read()

    # Set S3 bucket and object names
    bucket_name = "adithyasiva.shop"
    object_name = "index.html"
    
    # Upload file to S3
    s3.put_object(
        Bucket=bucket_name,
        Key=object_name,
        Body=html_file,
        ContentType="text/html"
    )
    
    return {
        'statusCode': 200,
        'body': 'HTML file uploaded to S3 successfully!'
    }