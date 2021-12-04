from util.db import db
from peewee import *
from util.models import Usuarios
from hashlib import md5


def criptografa(senha):
    senha_criptografada = md5(senha.encode())

    return senha_criptografada.hexdigest()


def insereUsuario(nome, email, senha):
    with db.atomic() as trans:
        try:
            senha_criptografada = criptografa(senha)
            usuario = Usuarios(nome=nome, email=email,
                               senha=senha_criptografada)
            usuario.save()
            trans.commit()
            return usuario
        except DatabaseError as err:
            print(err, f"data: {usuario}")
            trans.rollback()
            raise DatabaseError("Erro no banco de dados!")


def realizaLogin(email, senha):
    senha_criptografada = criptografa(senha)
    with db.atomic() as trans:
        try:
            usuario = Usuarios.get(
                Usuarios.email == email, Usuarios.senha == senha_criptografada)
            trans.commit()
            return usuario
        except Usuarios.DoesNotExist:
            raise DoesNotExist("Dados inválidos!")


def alteraUsuario(nome, emailAntigo, senhaAntiga, emailNovo, senhaNova):
    usuario = realizaLogin(emailAntigo, senhaAntiga)
    with db.atomic() as trans:
        try:
            if senhaNova:
                senha_criptografada = criptografa(senhaNova)
                usuario.senha = senha_criptografada
            if emailNovo:
                usuario.email = emailNovo
            if nome:
                usuario.nome = nome

            usuario.save()
            trans.commit()
            return usuario
        except DatabaseError as err:
            print(err, f"data: {usuario}")
            trans.rollback()
            raise DatabaseError("Erro no banco de dados!")


def deletaUsuario(usuario):
    with db.atomic() as trans:
        try:
            usuario.delete_instance(recursive=True)
            trans.commit()
        except DatabaseError:
            trans.rollback()
            raise DatabaseError("Erro no banco de dados!")
