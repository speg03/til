import json
import os


def lambda_handler(event, context):
    env = dict(os.environ)
    print(json.dumps(env, indent=2))
    return 'OK'
