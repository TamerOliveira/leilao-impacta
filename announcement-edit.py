import json

def lambda_handler(event, context):
    # TODO implement
    name = str(event['name'])

    try:
        return {
        # Sucesso
            'statusCode': 200,
            'body': json.dumps('Anuncio ' + name + ' Alterado com Sucesso! ')
        }

    except:

        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar processar mensagem')
        }