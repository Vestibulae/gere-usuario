from peewee import *
from util.db import db


class Usuarios(Model):

    id = AutoField()
    nome = CharField(max_length=30)
    email = CharField(max_length=100, index=True, unique=True)
    senha = CharField(max_length=40)

    class Meta:
        database = db

    def __str__(self):
        return f"Usuario: {self.id}; {self.nome}; {self.email}"
