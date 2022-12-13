# interface defined in the vertex side, commenting out as this requires to create
# from mlops_package_example.model_wrapper_interface import ModelWrapper
# class MyModel(ModelWrapper):


class Model():
    def train(self):
        print("Hi, I am doing my dummy training")

    def transform(self):
        pass

    def predict_batch(self):
        pass
