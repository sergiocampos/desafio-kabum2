from flask_restx import Resource
from flask_restx import Namespace
from .models import Transportadora
from .models import Produto
from .models import Cotacao
from .models import Dimensao
from .api_models import transportadora_model
from .api_models import produto_model

ns = Namespace("api")

@ns.route("/hello")
class Hello(Resource):
    def get(self):
        return {"dimensao": {"altura": 10, "largura": 30}, "peso": 30}

@ns.route("/transportadoras")
class TransportadoraAPI(Resource):
    @ns.marshal_list_with(transportadora_model)
    def get(self):
        return Transportadora.query.all()
    
    @ns.expect(transportadora_model)
    def post(self):
        return {}

@ns.route("/produto")
class ProdutoAPI(Resource):
    @ns.marshal_list_with(produto_model)
    def get(self):
        return Produto.query.all()
    
    @ns.expect(produto_model)
    def post(self):
        return {}