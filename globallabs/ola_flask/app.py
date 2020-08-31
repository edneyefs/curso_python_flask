from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/<int:numero>", methods=['GET', 'POST'])
def ola(numero):
    return f'Olá mundo. {numero}'

@app.route('/<int:id>')
def pessoa(id):
    soma = 1 + id
    return jsonify({'id':id, 'nome': 'Edney', 'profissão': 'Desenvolvedor'})

@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = request.data
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10 + 10
    return jsonify({'soma': total})

if __name__ == '__main__':
    app.run(debug=True)
