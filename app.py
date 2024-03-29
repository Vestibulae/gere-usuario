from flask import Flask, request, jsonify
from peewee import DatabaseError, DoesNotExist
from util.controller import alteraUsuario, insereUsuario, realizaLogin, deletaUsuario
from flask_cors import CORS
from util.models import Usuarios

DADOS_INVALIDOS = {"success": False, "message": "Dados Invalidos!"}
DUPLICADO = {"success": False, "message": "Email ja cadastrado!"}

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route('/api/v1/inserir/usuario', methods=['POST'])
def inserirUsuario():
    json_data = request.get_json(force=True)
    try:
        nome = json_data['nome']
        email = json_data['email']
        senha = json_data['senha']
        usuario = insereUsuario(nome, email, senha)
    except DatabaseError:
        return jsonify(DUPLICADO), 400
    except Exception:
        return jsonify(DADOS_INVALIDOS), 400

    return jsonify({"id": usuario.id, "nome": usuario.nome, "email": usuario.email})


@app.route('/api/v1/login', methods=['GET', 'POST'])
def login():
    json_data = request.get_json(force=True)
    try:
        email = json_data['email']
        senha = json_data['senha']
        usuario = realizaLogin(email, senha)
    except DoesNotExist:
        return jsonify(DADOS_INVALIDOS), 404
    except Exception:
        return jsonify(DADOS_INVALIDOS), 400

    return jsonify({"id": usuario.id, "nome": usuario.nome, "email": usuario.email})


@app.route('/api/v1/alterar/usuario', methods=['PUT'])
def alterarUsuario():
    json_data = request.get_json(force=True)
    try:
        nome = None if not 'nome' in json_data else json_data['nome']
        emailAntigo = json_data['email_antigo']
        emailNovo = None if not 'email_novo' in json_data else json_data['email_novo']
        senhaAntiga = json_data['senha_antiga']
        senhaNova = None if not 'senha_nova' in json_data else json_data['senha_nova']

        usuario = alteraUsuario(nome=nome, emailAntigo=emailAntigo,
                                senhaAntiga=senhaAntiga, emailNovo=emailNovo, senhaNova=senhaNova)
    except DoesNotExist:
        return jsonify(DADOS_INVALIDOS), 404
    except Exception:
        return jsonify(DADOS_INVALIDOS), 400

    return jsonify({"id": usuario.id, "nome": usuario.nome, "email": usuario.email})


@app.route('/api/v1/deletar/usuario', methods=['DELETE'])
def deletarUsuario():
    json_data = request.get_json(force=True)
    try:
        email = json_data['email']
        senha = json_data['senha']
        usuario = realizaLogin(email, senha)
        if usuario:
            deletaUsuario(usuario)

    except DoesNotExist:
        return jsonify(DADOS_INVALIDOS), 404
    except Exception:
        return jsonify(DADOS_INVALIDOS), 400

    return jsonify({"success": True})


Usuarios.create_table()
app.run(port=8080)
