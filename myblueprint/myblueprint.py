import flask

myblueprint = flask.Blueprint(
    'myblueprint', __name__, template_folder='templates')

@myblueprint.route('/')
def home():
    return flask.render_template(
        'index.html')
