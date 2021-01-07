from emotiondetection.dispatcher import dispatcher
from emotiondetection.features import build_features


class TrainModel:
    def __init__(self, model_name, engine="SKLEARN", **kwargs):
        # kwargs contains the model specific arguments with train data and labels
        self.engine = engine
        self.model = dispatcher.MODELS[model_name](**kwargs)

    def fit(self, **kwargs):
        # Havent specified which processor to use: SKELARN OR KERAS
        train_data = kwargs["train_data"]
        train_label = kwargs["train_label"]

        print("[INFO]: Training on {} model".format(self.model))

        clf = self.model.fit(train_data, train_label)

        return clf

    @classmethod
    def sklearn(cls, model_name, **kwargs):
        return cls(model_name, engine="SKLEARN", **kwargs)

    @classmethod
    def keras(cls, model_name, **kwargs):
        return cls(model_name, engine="KERAS", **kwargs)


if __name__ == "__main__":
    trainer = TrainModel.sklearn(model_name="multinominal_naive_bayes")
