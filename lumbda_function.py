import json
import boto3
import uuid
from datetime import datetime

comprehend = boto3.client('comprehend')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SentimentLogs')

def lambda_handler(event, context):
    body = json.loads(event['body']) if 'body' in event else event
    text = body.get("text", "")

    if not text:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'error': 'No text provided'})
        }

    # Analyze sentiment
    response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    sentiment = response['Sentiment']
    confidence = response['SentimentScore']

    # Log to DynamoDB
    log_item = {
        'id': str(uuid.uuid4()),
        'text': text,
        'sentiment': sentiment,
        'confidence': json.dumps(confidence),
        'timestamp': datetime.utcnow().isoformat()
    }

    try:
        table.put_item(Item=log_item)
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'error': 'DynamoDB write failed', 'details': str(e)})
        }

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps({
            'text': text,
            'sentiment': sentiment,
            'confidence': confidence
        })
    }
