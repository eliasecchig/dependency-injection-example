from kfp.v2 import compiler, dsl
from example_component import example_hello_world_op
from google.cloud import aiplatform


@dsl.pipeline(name='hello-world', description='A simple intro pipeline')
def pipeline_hello_world(text: str = 'hi there'):
    """Dummy pipeline to showcase the creation of a component which includes external file"""
    consume_task = example_hello_world_op(text="bla")  # Passing pipeline parameter as argument to consumer opxw


if __name__ == "__main__":
    # execute only if run as a script
    compiler.Compiler().compile(
        pipeline_func=pipeline_hello_world,
        package_path='hello_world_pipeline.json')

    job = aiplatform.PipelineJob(
        project='vertex-ai-test-365213',
        display_name=f"test-pipeline-importer",
        template_path='hello_world_pipeline.json',
        pipeline_root='gs://vertex-ai-test-365213-vertex-pipelines-us-central1'
    )
    job.submit()
