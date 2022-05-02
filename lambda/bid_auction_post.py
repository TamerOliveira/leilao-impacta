import json

from datetime import datetime
import boto3

import os
import base64

dynamodb = boto3.resource('dynamodb')

tb_bid_auction = dynamodb.Table('tb_bid_auction')

def lambda_handler(event, context):
    
    id_bid=base64.b64encode(os.urandom(6)).decode('ascii')
    generator=str(event['generator'])
    bid_value = str(event['bid_value'])
    id_announcement = str(event['id_announcement'])
    insertion_date = (datetime.now()).strftime("%Y-%m-%dT%H:%M")

    
    
    try:
        # Uma role deve ser configurada para a esta função,
        # permitindo PutItem para DynamoDB
        tb_bid_auction.put_item(
            Item={
                'id_bid': id_bid,
                'generator': generator,
                'bid_value': bid_value,
                'id_announcement': id_announcement,
                'insertion_date': insertion_date
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Lance '
                               + id_bid
                               + ' inserido no Banco de Dados')
        }

    except ValueError:
        # Erro: print() coloca mensagem de erro no log da função lambda
        print('Erro: lambda function terminada sem sucesso')
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar processar mensagem, ID: ' + id_bid + ' ' + log.exception())
        }


    