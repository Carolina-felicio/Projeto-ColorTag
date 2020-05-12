from flask import Flask, request, jsonify
from imagga import imagga_blueprint


app = Flask('app')
@app.route('/')
def index():
    return 'Seja bem vindo a nossa API de ColorTag'


app.register_blueprint(imagga_blueprint, url_prefix='/imagga/')


app.url_map.strict_slashes=False
print(app.url_map)
if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)
