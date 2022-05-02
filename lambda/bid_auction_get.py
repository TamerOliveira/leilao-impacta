
import json
import boto3
from boto3.dynamodb.conditions import Key



dynamodb = boto3.resource('dynamodb')
tb_bid_auction = dynamodb.Table('tb_bid_auction')


def lambda_handler(event, context):
    id_bid = str(event['id_bid'])
    try:
        response = tb_bid_auction.query(
            KeyConditionExpression=Key('id_bid').eq(id_bid))
        return {
        # Sucesso
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }

    except ValueError:
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar recuperar mensagens ' + log.exception)
        }