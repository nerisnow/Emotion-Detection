from emotiondetection.dispatcher import dispatcher


class TestModel:
    def __init__(self, model, engine="SKLEARN", **kwargs):
        self.model = model
        self.engine = engine

    def predict(self, **kwargs):
        test_data = kwargs["test_data"]
        test_label = kwargs["test_label"]

        predictions = self.model
