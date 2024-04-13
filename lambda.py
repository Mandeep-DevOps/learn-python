import json
import urllib.parse
import boto3


def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    client = boto3.client('ses', region_name='us-east-1')
    client1 = boto3.client('s3', region_name='us-east-1')
    bucket = s3.Bucket('d77-terraform')
    for obj in bucket.objects.all():
        key = obj.key
        body = obj.get()['Body'].read()
        print(body)
        json_content=json.loads(body)
        emailAddress=json_content["email"]
        name=json_content["name"]
        Data = "Hello " + name + ", \n \n Welcome to DevOps training"
        response = client.send_email(
            Destination={
                'ToAddresses': [emailAddress]
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': Data,
                    }
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': 'Test email',
                },
            },
            Source='raghuk.vit@gmail.com'
        )
        print('Sent email successfully!')

        delete_object = client1.delete_object(
            Bucket='d77-terraform',
            Key=key
        )

        print('Deleted Object Successfully!!')

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


