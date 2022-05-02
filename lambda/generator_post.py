import json

from datetime import datetime
import boto3

import os
import base64

dynamodb = boto3.resource('dynamodb')

tb_generator = dynamodb.Table('tb_generator')

def lambda_handler(event, context):
    
    id_generator=base64.b64encode(os.urandom(6)).decode('ascii')
    insertion_date = (datetime.now()).strftime("%Y-%m-%dT%H:%M")
    
    name = str(event['name'])
    url_image = str(event['url_image'])
    user = str(event['user'])
    password = str(event['password'])


    try:
        tb_generator.put_item(
            Item={
                'id_generator': id_generator,
                'name': name,
                'url_image': url_image,
                'insertion_date': insertion_date,
                'password': password,
                'user': user
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Profile '
                               + name
                               + ' inserido no Banco de Dados')
        }

    except ValueError:
        # Erro: print() coloca mensagem de erro no log da função lambda
        print('Erro: lambda function terminada sem sucesso')
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar processar mensagem, ID: ' + id_generator + ' ' + log.exception())
        }


    