
import json
import boto3
from boto3.dynamodb.conditions import Key



dynamodb = boto3.resource('dynamodb')
tb_generator = dynamodb.Table('tb_generator')


def lambda_handler(event, context):
    id_generator = str(event['id_generator'])
    try:
        response = tb_generator.query(
            KeyConditionExpression=Key('id_generator').eq(id_generator))
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