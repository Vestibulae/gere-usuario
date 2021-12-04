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


# class Provas(Model):

#     id = AutoField()
#     prova = CharField(max_length=45, index=True)
#     ano = DecimalField(decimal_places=0, max_digits=4, index=True)
#     fase = DecimalField(decimal_places=0, max_digits=1)
#     descricao = CharField(max_length=45, null=True)

#     class Meta:
#         database = db
#         indexes = (
#             (('prova', 'ano', 'fase'), True),
#         )

#     def __str__(self):
#         return f"Prova: {self.id}; {self.prova}; {self.ano}; {self.fase}; {self.descricao}"


# class Questoes(Model):

#     id = AutoField()
#     prova_id = ForeignKeyField(Provas, backref="questoes")
#     numero = DecimalField(decimal_places=0, max_digits=3)
#     materia = CharField(max_length=45)
#     enunciado = TextField()
#     assunto = CharField(max_length=45, null=True)
#     imagem = CharField(max_length=100, null=True)

#     class Meta:
#         database = db
#         indexes = (
#             (('prova_id', 'numero', 'materia'), True),
#             # (('enunciado'), True),
#         )

#     def __str__(self):
#         return f"Questao: {self.id}; {self.prova_id.id}; {self.numero}; {self.materia}; {self.enunciado}; {self.assunto}; {self.imagem}"


# class Respostas(Model):

#     id = AutoField()
#     prova_id = ForeignKeyField(Provas, backref="respostas")
#     questao_id = ForeignKeyField(Questoes, backref="respostas")
#     enunciado = TextField()
#     alternativa = CharField(max_length=1)
#     imagem = CharField(max_length=100, null=True)

#     class Meta:
#         database = db
#         indexes = (
#             (('prova_id', 'questao_id', 'alternativa'), True),
#         )

#     def __str__(self):
#         return f"Resposta: {self.id}; {self.prova_id.id}; {self.questao_id.id}; {self.enunciado}; {self.alternativa}; {self.imagem}"


# class Gabaritos(Model):

#     prova_id = ForeignKeyField(Provas, backref="gabarito")
#     questao_id = ForeignKeyField(
#         Questoes, backref="gabarito", primary_key=True)
#     resposta_id = ForeignKeyField(Respostas)

#     class Meta:
#         database = db

#     def __str__(self):
#         return f"Gabarito: {self.prova_id.id}; {self.questao_id.id}; {self.resposta_id.id}"
