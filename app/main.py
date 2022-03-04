import json


def hello(event, context):
    body = {
        "message": "Hello world!",
        "input": event
    }

    return {"statusCode": 200, "body": json.dumps(body)}