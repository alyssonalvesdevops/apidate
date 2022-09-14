from logging import error
import logging
from flask import Flask, request, jsonify, json
from flask_restful import Resource, Api
from elasticapm.contrib.flask import ElasticAPM
from datetime import datetime
import requests
import os

app = Flask(__name__)
api = Api(app)

from elasticapm.contrib.flask import ElasticAPM

try:
  app.config['ELASTIC_APM'] = {
  'SERVICE_NAME': 'apidate',
  'SECRET_TOKEN': os.environ['SECRET_TOKEN'],
  'SERVER_URL': os.environ['SECRET_URL'],
  'ENVIRONMENT': 'production'
  }

  apm = ElasticAPM(app, logging=logging.ERROR)
except:
  print("Conexão com Elastic falhou")

    
class Date(Resource):
  def get(self):
    try:
      timezone = request.headers.get('timezone')
      url = 'http://worldtimeapi.org/api/timezone/' + timezone
      resposta = requests.get(url)
      try:
        hora = datetime.fromisoformat(resposta.json()['datetime']).strftime("%a, %d/%m/%y %H:%M:%S")
        response = {"Data UTC" : hora}
        return jsonify(response)

      except:
        text = {"Error" : "Timezona não encontrada"}
        menssage = app.response_class(
          response=json.dumps(text),
          status=404,
          mimetype='application/json')
        logging.error(text)  
        return menssage

    except :
      text = {"Error" : "falta o header com Timezone desejado"}
      menssage = app.response_class(
        response=json.dumps(text),
        status=422,
        mimetype='application/json')
      logging.error(text) 
      return menssage
    
api.add_resource(Date, '/') 

if __name__ == '__main__':
    app.run()