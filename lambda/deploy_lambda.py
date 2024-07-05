import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('lambda')
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_key = event['Records'][0]['s3']['object']['key']
    
    response = client.update_function_code(
        FunctionName='YourLambdaFunctionName',
        S3Bucket=s3_bucket,
        S3Key=s3_key,
        Publish=True
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function updated successfully')
    }
