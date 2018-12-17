import os
from flask import Flask

def create_app(config=None):
    # print("create app.")
    app = Flask(__name__, instance_relative_config=True)

    if config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello world!'

    from . import auth
    from . import api_v1

    app.register_blueprint(auth.blueprint)
    app.register_blueprint(api_v1.blueprint)

    return app
