from flask import Flask

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_json("../config/development.json")
    print(f"init app: {app}")

    with app.app_context():
        
        from .dash_app import init_dash
        app = init_dash(app)

        return app