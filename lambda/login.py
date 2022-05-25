
import json
import boto3
from boto3.dynamodb.conditions import Key



dynamodb = boto3.resource('dynamodb')
tb_users = dynamodb.Table('tb_users')


def lambda_handler(event, context):
    
    email = str(event['email'])
    password = str(event['password'])
    
    try:
        response = tb_users.query(
            KeyConditionExpression=Key('email').eq(email))

        for i in response['Items']:
            print(i['name'], ":", i['password'])
            
            if email==i['email'] and password==i['password']:
                return {
                'statusCode': 200,
                'body': json.dumps(response['Items'])
                }
            else:
                return {
                'statusCode': 401,
                'body': json.dumps('E-mail e/ou senha incorreto')
                }
                


    except ValueError:
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar recuperar mensagens ' + log.exception)
        }