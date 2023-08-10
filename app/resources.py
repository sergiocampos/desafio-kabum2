from flask_restx import Resource
from flask_restx import Namespace

ns = Namespace("api")

@ns.route("/hello")
class Hello(Resource):
    def get(self):
        return {"hello": "restx"}