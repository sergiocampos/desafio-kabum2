from .extensions import db

class Transportadora(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=False)
    altura_max = db.Column(db.Integer)
    altura_min = db.Column(db.Integer)
    largura_max = db.Column(db.Integer)
    largura_min = db.Column(db.Integer)
    constante_frete = db.Column(db.Float)
    prazo_entrega = db.Column(db.Integer)


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dimensao = db.relationship("Dimensao", back_populates="produto")
    peso = db.Column(db.Integer)


class Dimensao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    altura = db.Column(db.Integer)
    largura = db.Column(db.Integer)
    produto_id = db.Column(db.ForeignKey("produto.id"))
    produto = db.relationship("Produto", back_populates="dimensao")


class Cotacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_transportadora = db.Column(db.String(100), unique=False)
    valor_frete = db.Column(db.Float)
    prazo_entrega = db.Column(db.Integer)
