# interface defined in the vertex side, commenting out as this requires to create
# from example_of_a_python_package_outside_of_this_repo.model_wrapper_interface import ModelWrapper
# class MyModel(ModelWrapper):


class Model():
    def train(self, ):
        print("Hi, I am doing my dummy training")

    def transform(self):
        pass

    def predict(self):
        print("Hi, I am doing my dummy scoring")
        pass

    def validation_logic(self):
        return "validate"

    def champion_challenger_logic(self, champion_metrics: dict, challenger_metrics: dict):
        return "promote"

    def save(self):
        pass