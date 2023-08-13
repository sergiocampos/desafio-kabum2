from flask_restx import Resource
from flask_restx import Namespace
from .models import Transportadora
from .models import Produto
from .models import Cotacao
from .models import Dimensao
from .api_models import transportadora_model
from .api_models import produto_model
from .api_models import dimensao_model
from .api_models import cotacao_model
from .extensions import db
from .api_models import cotacao_input_model
from .api_models import produto_input_model
import json
from flask import jsonify

ns = Namespace("api")

@ns.route("/transportadoras")
class TransportadoraAPI(Resource):
    #@ns.marshal_list_with(transportadora_model)
    def get(self):
        with open("transportadoras.json") as file:
            data = json.load(file)
        return data
    
    @ns.expect(transportadora_model)
    def post(self):
        return {}

@ns.route("/produto")
class ProdutoAPI(Resource):
    @ns.marshal_list_with(produto_model)
    def get(self):
        return Produto.query.all()
    
    @ns.expect(produto_model)
    @ns.marshal_with(produto_model)
    def post(self):
        
        data = ns.payload["dimensao"]
        
        for d in data:
            altura = d['altura']
            largura = d['largura']

        peso = ns.payload["peso"]
        transportadoras = Transportadora.query.all()

        for t in transportadoras:
            if altura >= t.altura_min and altura <= t.altura_max and largura >= t.largura_min and largura <= t.largura_max:
                nome_transportadora = t.nome
                valor_frete = t.constante_frete*peso
                prazo_entrega = t.prazo_entrega


        return {'nome_transportadora':nome_transportadora, 'valor_frete':valor_frete, 'prazo_entrega':prazo_entrega}, 201

@ns.route("/cotacao")
class CotacaoAPI(Resource):
    @ns.marshal_list_with(cotacao_model)
    def get(self):
        return Cotacao.query.all()
    
    @ns.expect(produto_input_model)
    #@ns.marshal_with(cotacao_model)
    def post(self):
        
        #dados vindo do payload
        data = ns.payload["dimensao"]
        peso = ns.payload["peso"]
        
        for d in data:
            altura = d['altura']
            largura = d['largura']

        # acessando o arquivo das transportadoras
        with open("transportadoras.json") as file:
            data = json.load(file)
            total_transportadoras = len(data["transportadoras_db"])
            #definindo lista de cotações
            total_transportadoras = total_transportadoras
            nome_transportadora = [0]*total_transportadoras
            valor_frete = [0]*total_transportadoras
            prazo_entrega = [0]*total_transportadoras
            cotacoes = {"cotacoes": []}

            for i in range(total_transportadoras):
                if altura >= data["transportadoras_db"][i]["altura_min"] and altura <= data["transportadoras_db"][i]["altura_max"] and largura >= data["transportadoras_db"][i]["largura_min"] and largura <= data["transportadoras_db"][i]["largura_max"]:
                    nome_transportadora[i] = data["transportadoras_db"][i]["title"]
                    valor_frete[i] = data["transportadoras_db"][i]["constante_calculo"]*peso
                    prazo_entrega[i] = data["transportadoras_db"][i]["prazo_entrega"]
            for j in range(total_transportadoras):
                if nome_transportadora[j] == None or nome_transportadora[j] == 0 or nome_transportadora[j] == '':
                    cotacoes["cotacoes"].append({})
                else:
                    cotacoes["cotacoes"].append(
                        {
                            "nome_transportadora": nome_transportadora[j],
                            "valor_frete": valor_frete[j],
                            "prazo_entrega": prazo_entrega[j]
                        }
                    )
            
            with open("cotacoes.json", "w") as arquivo:
                json.dump(cotacoes, arquivo, indent=4)
        data = json.dumps(cotacoes, indent=4)
        print(data)

        return (data)