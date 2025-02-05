# Adding Swagger UI to local 
# https://dev.to/sanjan/how-to-add-swagger-ui-to-a-plain-flask-api-project-with-an-openapi-specification-file-1jl8
# https://flask.palletsprojects.com/en/stable/api/#flask.send_from_directory

from flask import Flask
from flask_smorest import Api

from resources.items import blp as ItemBlueprint
from resources.stores import blp as StoreBlueprint

app = Flask(__name__, static_folder='dist')

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v0.7"
app.config["OPENAPI_VERSION"]= "3.1.0"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "/dist/"

api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)