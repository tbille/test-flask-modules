import flask
from myblueprint.myblueprint import myblueprint


def create_app():
    app = flask.Flask(__name__)
    app.register_blueprint(myblueprint)

    return app
