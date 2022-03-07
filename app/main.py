import json


def hello(event, context):
    response_message = 'Hello, world!'
    if event['queryStringParameters']:
        name_from_query_parameter = event['queryStringParameters']['Name']
        response_message = f'Hello, {name_from_query_parameter}!'

    body = {
        "message": response_message,
    }

    return {"statusCode": 200, "body": json.dumps(body)}