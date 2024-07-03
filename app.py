from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r'/api-subs/*': {'origin': '*'}})

from componentes.vistas_api import *

if __name__ == "__main__":
    app.run()