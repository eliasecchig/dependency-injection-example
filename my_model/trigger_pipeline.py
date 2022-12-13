import yaml

from kfp.v2 import compiler
from google.cloud import aiplatform

from mlops_package_example.components.register_asset import register_asset
from mlops_package_example.pipelines.example_pipeline_with_artifact import pipeline_hello_world_with_artifact

model_config = yaml.safe_load(open('my_model/config.yaml'))

if __name__ == "__main__":
    # execute only if run as a script
    compiler.Compiler().compile(
        pipeline_func=pipeline_hello_world_with_artifact,
        package_path='../hello_world_pipeline.json')

    file_uri = register_asset(file_name="my_model/model.py")

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
