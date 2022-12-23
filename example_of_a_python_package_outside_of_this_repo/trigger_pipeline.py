from kfp.v2 import compiler
from google.cloud import aiplatform

from example_of_a_python_package_outside_of_this_repo.components.register_asset import register_asset
from example_of_a_python_package_outside_of_this_repo.pipelines.example_pipeline_with_artifact import get_pipeline


if __name__ == "__main__":
    # execute only if run as a script
    compiler.Compiler().compile(
        pipeline_func=get_pipeline(),
        package_path='../hello_world_pipeline.json')

    # In a real life scenario this trigger tool would receive as parameter the path to model wrapper file
    file_uri = register_asset(file_name="my_model/model_wrapper.py")

    # edit the parameters here
    job = aiplatform.PipelineJob(
        project='vertex-ai-test-365213',
        display_name=f"test-pipeline-importer",
        template_path='../hello_world_pipeline.json',
        pipeline_root='gs://vertex-ai-test-365213-vertex-pipelines-us-central1',
        parameter_values={
            "model_file_uri": file_uri
        },
        enable_caching=True
    )
    job.submit()
