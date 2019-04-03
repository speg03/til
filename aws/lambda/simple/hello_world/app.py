import os
import json


def lambda_handler(event, context):
    env = dict(os.environ)
    print(json.dumps(env, indent=2))
    return 'OK'
