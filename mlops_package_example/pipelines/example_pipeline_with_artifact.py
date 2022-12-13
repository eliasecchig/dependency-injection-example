from kfp.v2 import dsl
from kfp.v2.dsl import Artifact
from kfp.v2.dsl import importer
from mlops_package_example.components.example_component_with_artifact import dummy_training_with_artifact_op



@dsl.pipeline(name='hello-world', description='A simple intro pipeline')
def pipeline_hello_world_with_artifact(model_file_uri: str):
    """Dummy pipeline to showcase the creation of a component which includes external file with artifact"""

    # file_name hardcoded here, in real life this would be dynamically imported by the model_module_path
    model_file = importer(
        artifact_uri=model_file_uri,
        artifact_class=Artifact
    ).output
    consume_task = dummy_training_with_artifact_op(
        text="bla",
        model_module_path='file.Model',
        model_file=model_file
    )
