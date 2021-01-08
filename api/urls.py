from api.services import predictor


def app_routes(app):
    app.add_url_rule(rule="/", view_func=predictor.home, methods=["GET"])
    app.add_url_rule(rule="/data", view_func=predictor.data, methods=["POST", "GET"])
    app.add_url_rule(rule="/predict", view_func=predictor.predict, methods=["POST"])
