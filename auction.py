import json

def lambda_handler(event, context):
    # TODO implement
    valor = str(event['valor'])
    id_anuncio = str(event['id-announcement'])

    try:
        return {
        # Sucesso
            'statusCode': 200,
            'body': json.dumps('Lance realizado no anuncio ' + id_anuncio + ' no valor de ' + valor)
        }

    except:

        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar processar mensagem')
        }