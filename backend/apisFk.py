import flask
import flask_cors
import json
import apis

from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def post():
    titulo = request.json
    print(titulo)
    try:
        array = apis.apiGoogle(titulo)
        return json.dumps(array)
    except Exception as e:
        print(e)
        return e

if __name__ == "__main__":
    app.run(debug=True)