import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('codebuild')
    
    response = client.start_build(
        projectName='YourCodeBuildProjectName'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('CodeBuild started successfully')
    }
