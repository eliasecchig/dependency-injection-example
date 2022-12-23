from kfp.v2 import dsl
from kfp.v2.dsl import Artifact
from kfp.v2.dsl import importer
from example_of_a_python_package_outside_of_this_repo.components.generic_training_component import dummy_training_with_artifact_op
from example_of_a_python_package_outside_of_this_repo.components.generic_scoring_component import dummy_scoring_with_artifact_op


def get_pipeline(
        train_op=dummy_training_with_artifact_op,
        scoring_op=dummy_scoring_with_artifact_op
):
    @dsl.pipeline(name='hello-world', description='A simple intro pipeline')
    def pipeline_hello_world(model_file_uri: str):
        """Dummy pipeline to showcase the creation of a component which includes external file"""
        model_file = importer(
            artifact_uri=model_file_uri,
            artifact_class=Artifact
        ).output
        train_task = train_op(
            text="bla",
            model_module_path='file.Model',
            model_file=model_file
        )
        scoring_task = scoring_op(
            text="bla",
            model_module_path='file.Model',
            model_file=model_file
        )

    return pipeline_hello_world
