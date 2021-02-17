from flask import Flask
from os import makedirs

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
        # SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    # assets = Environment()
    # assets.init_app(app)

    # ensure the instance folder exists
    try:
        makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        # blueprint
        from . import hello
        app.register_blueprint(hello.bp)

        return app
