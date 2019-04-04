import os


def lambda_handler(event, context):
    return os.getenv('SNS_TOPIC_ARN', 'N/A')
