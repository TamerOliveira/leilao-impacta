
import json
import boto3
from boto3.dynamodb.conditions import Key



dynamodb = boto3.resource('dynamodb')
tb_announcement = dynamodb.Table('tb_announcement')


def lambda_handler(event, context):
    idannouncement = str(event['idannouncement'])
    try:
        response = tb_announcement.query(
            KeyConditionExpression=Key('id_announcement').eq(idannouncement))
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