from kfp.v2 import dsl
from mlops_package_example.components.example_component_with_artifact import dummy_training_with_artifact_op
from mlops_package_example.components.register_asset_op import register_asset_op


@dsl.pipeline(name='hello-world', description='A simple intro pipeline')
def pipeline_hello_world_with_artifact(model_module_path: str, text: str = 'hi there'):
    """Dummy pipeline to showcase the creation of a component which includes external file with artifact"""

    # file_name hardcoded here, in real life this would be dynamically imported by the model_module_path
    model_file = register_asset_op(file_name='my_model/dummy_model.py').output

    consume_task = dummy_training_with_artifact_op(
        text="bla",
        model_module_path=model_module_path,
        model_file=model_file
    )
