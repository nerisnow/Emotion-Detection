from flask import Flask

from api.urls import app_routes


def init_app():
    app = Flask(__name__)

    app_routes(app)

    return app


if __name__ == "__main__":
    app = init_app()
    app.run(debug=True)