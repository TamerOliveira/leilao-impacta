
import json
import boto3
from boto3.dynamodb.conditions import Key



dynamodb = boto3.resource('dynamodb')
tb_users = dynamodb.Table('tb_users')


def lambda_handler(event, context):
    
    email = str(event['email'])
    password = str(event['password'])
    name = str(event['name'])
    
    try:
        response = tb_users.query(
            KeyConditionExpression=Key('email').eq(email))
        retorno = response['Items']
        if not retorno:
            tb_users.put_item(
            Item={
                'name': name,
                'password': password,
                'email': email
            }
            )
            return {
            'statusCode': 200,
            'body': json.dumps('Usuario ' + name + ' Cadastrado com sucesso!')
            }
        else:
            return {
            'statusCode': 200,
            'body': json.dumps('E-mail ' + email + ' ja cadastrado!')
            }


    except ValueError:
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar recuperar mensagens ' + log.exception)
        }