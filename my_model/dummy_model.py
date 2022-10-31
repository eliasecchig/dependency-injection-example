# it would extend an interface defined in the mlops side, commenting out as this requires to create
# a component with the package installed
# from mlops_package_example.model_wrapper_interface import ModelWrapper
# class MyModel(ModelWrapper):


class MyModel():
    def train(self):
        print("Hi, I am doing my dummy training")

    def transform(self):
        pass

    def predict_batch(self):
        pass
