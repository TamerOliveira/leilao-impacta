import json

from datetime import datetime
import boto3

import os
import base64

dynamodb = boto3.resource('dynamodb')

tb_announcement = dynamodb.Table('tb_announcement')

def lambda_handler(event, context):
    
    id_announcement=base64.b64encode(os.urandom(6)).decode('ascii')
    active=True
    date_announcement = str(event['date-announcement'])
    description = str(event['description-announcement'])
    insertion_date = (datetime.now()).strftime("%Y-%m-%dT%H:%M")
    min_value = str(event['min-value'])
    name = str(event['name'])
    
    
    
    try:
        # Uma role deve ser configurada para a esta função,
        # permitindo PutItem para DynamoDB
        tb_announcement.put_item(
            Item={
                'id_announcement': id_announcement,
                'active': active,
                'date_announcement': date_announcement,
                'description': description,
                'insertion_date': insertion_date,
                'min_value': min_value,
                'name': name
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Anúncio '
                               + name
                               + ' inserido no Banco de Dados')
        }

    except ValueError:
        # Erro: print() coloca mensagem de erro no log da função lambda
        print('Erro: lambda function terminada sem sucesso')
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar processar mensagem, ID: ' + id_announcement + ' ' + log.exception())
        }


    