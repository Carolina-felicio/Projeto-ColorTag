from flask import Flask
from color import color_blueprint


app = Flask(__name__)
'''
Criação da rota [GET], para a rota principal da API
que retornará uma mensagem
'''
@app.route('/')
def index():
    return f'<h3>Seja bem vindo a nossa api de Colortag</h3>', 200


'''
Registrando o Blueprint
'''
app.register_blueprint(color_blueprint, url_prefix='/colortag/')


'''
Mapeando as chamadas de endpoint 
E printando no console
'''
app.url_map.strict_slashes=False
print(app.url_map)


'''
Startando o servidor local na porta 5000, com o debug ativado
'''
if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)
