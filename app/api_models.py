from flask_restx import fields
from .extensions import api

transportadora_model = api.model("Transportadora", {
    "id": fields.Integer,
    "nome": fields.String,
    "altura_max": fields.Integer,
    "altura_min": fields.Integer,
    "largura_max": fields.Integer,
    "largura_min": fields.Integer,
    "constante_frete": fields.Integer,
    "prazo_entrega": fields.Integer
    })

dimensao_model = api.model("Dimensao", {
    #"id": fields.Integer,
    #"nome": fields.String,
    "altura": fields.Integer,
    "largura": fields.Integer
    })

produto_model = api.model("produto", {
    #"id": fields.Integer,
    "dimensao": fields.List(fields.Nested(dimensao_model)),
    "peso": fields.Integer
    })

cotacao_model = api.model("Cotacao", {
    #"id": fields.Integer,
    "nome_transportadora": fields.String,
    "valor_frete": fields.Float,
    "prazo_entrega": fields.Integer
    })

produto_input_model = api.model("ProdutoInput", {
    "dimensao": fields.List(fields.Nested(dimensao_model)),
    "peso": fields.Integer
    })

cotacao_input_model = api.model("CotacaoInput", {
    "nome_transportadora": fields.String,
    "valor_frete": fields.Float,
    "prazo_entrega": fields.Integer
    })