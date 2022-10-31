from kfp.v2 import dsl
from mlops_package_example.components.example_component import dummy_training_op


@dsl.pipeline(name='hello-world', description='A simple intro pipeline')
def pipeline_hello_world(model_module_path: str, text: str = 'hi there'):
    """Dummy pipeline to showcase the creation of a component which includes external file"""
    consume_task = dummy_training_op(text="bla", model_module_path=model_module_path)

