from sqlalchemy import ForeignKey
from app.config_db import db
# from datetime import date

class ProjectEntity(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    centro_custo = db.Column(db.String(50))
    data_inicio = db.Column(db.String(10))
    data_fim = db.Column(db.String(10))
    status = db.Column(db.String(50))
    flag = db.Column(db.Enum('vermelho', 'amarelo', 'verde'))
    id_gerente = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    
    def __init__(self, nome, centro_custo, data_inicio, data_fim, status, flag, id_gerente):
        self.nome = nome
        self.centro_custo = centro_custo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = status
        self.flag = flag
        self.id_gerente = id_gerente

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'centro_custo': self.centro_custo,
            'data_inicio': self.data_inicio,
            'data_fim': self.data_fim,
            'status': self.status,
            'flag': self.flag,
            'id_gerente': self.id_gerente
        }

    @classmethod
    def find_project(cls, id):
        # SELECT * FROM projects WHERE id(do db) = id(do parametro)
        project = cls.query.filter_by(id=id).first()
        if project:
            return project
        return None
    
    def save_project(self):
        db.session.add(self)
        db.session.commit()

    def update_project(self, nome, centro_custo, data_inicio, data_fim, status, flag, id_gerente):
        self.nome = nome
        self.centro_custo = centro_custo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = status
        self.flag = flag
        self.id_gerente = id_gerente
    
    def delete_project(self):
        db.session.delete(self)
        db.session.commit()

# User Entity
class UsersEntity(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    primeiro_nome = db.Column(db.String(100))
    ultimo_nome = db.Column(db.String(50))
    data_nascimento = db.Column(db.String(10))
    cargo = db.Column(db.String(10))
    matricula = db.Column(db.String(50))
    status = db.Column(db.String(50))
    # id_centro_custo = db.Column(db.Integer)

    gerente = db.relationship (ProjectEntity)

    def __init__(self, primeiro_nome, ultimo_nome, data_nascimento, cargo, matricula, status):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.data_nascimento = data_nascimento
        self.cargo = cargo
        self.matricula = matricula
        self.status = status
        # self.id_centro_custo = id_centro_custo

    def json(self):
        return {
            'id': self.id,
            'primeiro_nome': self.primeiro_nome,
            'ultimo_nome': self.ultimo_nome,
            'data_nascimento': self.data_nascimento,
            'cargo': self.cargo,
            'matricula': self.matricula,
            'status': self.status,
            # 'id_centro_custo': self.id_centro_custo
        }

    @classmethod
    def find_user(cls, id):
        # igual a SELECT * FROM users WHERE id(do db) = id(do parametro)
        user = cls.query.filter_by(id=id).first()
        if user:
            return user
        return None
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def update_user(self, primeiro_nome, ultimo_nome, data_nascimento, cargo, matricula, status):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.data_nascimento = data_nascimento
        self.cargo = cargo
        self.matricula = matricula
        self.status = status
        # self.id_centro_custo = id_centro_custo
    
    def delete_user(self):
        db.session.delete(self)
        db.session.commit()