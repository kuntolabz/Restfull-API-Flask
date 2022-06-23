#import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
#import sql sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import os
#inisiai object flask
app = Flask(__name__)

#inisiasi object flask_restful
api = Api(app)

CORS (app)

#inisialisasi db
db = SQLAlchemy(app)

basedir = os.path.dirname(os.path.abspath(__file__))
database = "sqlite:///"+ os.path.join(basedir,"db.sqlite")
app.config["SQLALCHEMY_DATABASE_URI"] = database

#membuat database model
class ModelDatabase(db.Model):
    #membuat kolom
    id = db.Column(db.Integer,primary_key=True)
    nama = db.Column(db.String(100))
    umur = db.Column(db.Integer)
    alamat = db.Column(db.TEXT)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False


db.create_all()

#inisiasi variabel 
identitas = {}

class ContohResource(Resource):
    def get(self):
        query = ModelDatabase.query.all()

        # melakukan iterasi pada modelDatabase dengan teknik 
        output = [
            {
                "id":data.id,
                "nama":data.nama, 
                "umur":data.umur, 
                "alamat":data.alamat
            } 
            for data in query
        ]

        response = {
            "code" : 200, 
            "msg"  : "Query data sukses",
            "data" : output
        }

        return response, 200
    
    def post(self):
        DataNama = request.form["nama"]
        DataUmur = request.form["umur"]
        DataAlamat = request.form["alamat"]
        
        model = ModelDatabase(nama=DataNama,umur=DataUmur,alamat=DataAlamat)
        model.save()
        response = {"msg":"data berhasil masuk","code":200}
        return response

api.add_resource(ContohResource,"/api",methods=["GET","POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)