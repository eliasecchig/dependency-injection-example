from abc import ABC


class ModelWrapper(ABC):
    def train(self):
        pass

    def transform(self):
        pass

    def predict_batch(self):
        pass