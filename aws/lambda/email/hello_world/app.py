import os

import boto3


def lambda_handler(event, context):
    sns = boto3.client('sns')
    response = sns.publish(
        TopicArn=os.getenv('SNS_TOPIC_ARN'),
        Subject='lambda-email',
        Message='OK')
    return response
