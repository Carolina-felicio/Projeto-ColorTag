import requests
from flask import Flask, Blueprint


'''
Criação do Blueprint [imaggabp]
'''
bp = Blueprint('colorbp', __name__)


'''
Inserindo a API_Key e a API_SECRET para a autenticação
Inserindo a IMAGE_URL para a requisição
'''
api_key = 'acc_29b91702e9312af'
api_secret = '5b0adf0e4e980fd3f55dfd78a064b5c2'
image_url = 'https://imagga.com/static/images/tagging/wind-farm-538576_640.jpg'


'''
Resposta para a requisição na URL, contendo a url da imagem,
api_key e a api_secret para fazer a autenticação na requisição.
'''
response = requests.get(
    'https://api.imagga.com/v2/colors?image_url=%s' % image_url,
    auth=(api_key, api_secret))

'''
Criação de rota com o método [GET]
que retornará a resposta da imagem no formato Json
'''
@bp.route('/', methods=['GET'])
def fix():
    return response.json() 
