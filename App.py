__author__ = "Isaac Cárdenas"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Isaac Cárdenas"
__email__ = "is_cardenas@hotmail.com"
__status__ = "Development"
__date__ = "29/Agosto/2021"

import json
from werkzeug.exceptions import HTTPException
from flask import Flask, render_template, request
from flask_cors import CORS

from project.service.DataService import DataService
from project.utils.Logger import Logger
from project.utils.Status import Status

log = Logger().getLogger("APP")
dataService = DataService()

app = Flask("TareaWebApp",
            static_url_path='/static',
            static_folder='web/static',
            template_folder='web/templates'
            )
app.config['JSON_SORT_KEYS'] = False
UPLOAD_FOLDER = 'web/static/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/data', methods=["POST"])
def dataPost():
    response = {}
    try:
        data = request.get_json()
        if data:
            response["data"] = dataService.getData(data)
            response["message"] = "Datos generados con éxito"
            response["statusCode"] = Status.HTTP_200_OK.value
            return json.dumps(response), Status.HTTP_200_OK.value
        else:
            response["message"] = "Se requiere los datos de consulta [ticker]"
            response["statusCode"] = Status.HTTP_400_BAD_REQUEST.value
            return json.dumps(response), Status.HTTP_400_BAD_REQUEST.value
    except Exception as e:
        response["message"] = "Se produjo un error al procesar la petición"
        response["statusCode"] = Status.HTTP_500_INTERNAL_SERVER_ERROR.value
        return json.dumps(response), Status.HTTP_200_OK.HTTP_500_INTERNAL_SERVER_ERROR.value

@app.route('/data', methods=["GET"])
def dataGet():
    response = {}
    try:
        data = dict(
            ticker="tsla",
            start="2017-01-01",
            end="2017-12-31"
        )
        response["data"] = dataService.getData(data)
        response["message"] = "Datos generados con éxito"
        response["statusCode"] = Status.HTTP_200_OK.value
        return json.dumps(response), Status.HTTP_200_OK.value
    except Exception as e:
        response["message"] = "Se produjo un error al procesar la petición"
        response["statusCode"] = Status.HTTP_500_INTERNAL_SERVER_ERROR.value
        return json.dumps(response), Status.HTTP_200_OK.HTTP_500_INTERNAL_SERVER_ERROR.value


@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "status": e.code,
        "name": e.name,
        "message": e.description,
    })
    response.content_type = "application/json"
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
