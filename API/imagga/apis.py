import requests as r
from flask import Flask, jsonify, Blueprint


bp = Blueprint('imaggabp', __name__)
api_key = 'acc_69c87cf817b99c6'
api_secret = '5167a3b7835d9973d72e7018dd8b5f10'
image_url = 'https://imagga.com/static/images/tagging/wind-farm-538576_640.jpg'


response = r.get(
    'https://api.imagga.com/v2/colors?image_url=%s' % image_url,
    auth=(api_key, api_secret))


@bp.route('/', methods=['GET'])
def index():
    return response.json()
