#import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

#inisiai object flask
app = Flask(__name__)

#inisiasi object flask_restful
api = Api(app)

CORS (app)

#inisiasi variabel 
identitas = {}

class ContohResource(Resource):
    def get(self):
        #response = {"msg":"Hallo cuk"}
        return identitas
    
    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg":"data berhasil masuk"}
        return response

api.add_resource(ContohResource,"/api",methods=["GET","POST"])

if __name__ == "__main__":
    app.run(debug=True, port=2300)