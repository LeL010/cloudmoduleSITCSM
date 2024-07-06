import json

def lambda_handler(event, context):
    # Extract the fulfillment state and message from the Lex event
    fulfillment_state = event['currentIntent']['fulfillmentState']
    message = event['currentIntent']['message']
    
    # Prepare the response for the website
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'fulfillmentState': fulfillment_state,
            'message': message
        })
    }
    
    return response
