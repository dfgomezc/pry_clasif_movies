#!/usr/bin/python

from flask import Flask
from flask_restx import Api, Resource, fields
import joblib
from model_deployment import predict_category
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

api = Api(
    app, 
    version='1.0', 
    title='Clasificar peliculas',
    description='Evaluar la probabilidad de que una pelicula este en diferentes generos')

ns = api.namespace('predict', 
     description='Predecir el genero de una pelicula')
   
parser = api.parser()

parser.add_argument(
    'Plot', 
    type=str, 
    required=True, 
    help='Descripcion de la pelicula', 
    location='args',
    # action='append'
    )


resource_fields = api.model('Resource', {
    'result': fields.String,
})


@ns.route('/')
class ClassMovies(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        return {
         "result":  predict_category(args.Plot) 
        }, 200
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
