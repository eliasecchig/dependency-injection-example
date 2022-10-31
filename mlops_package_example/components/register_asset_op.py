import hashlib

from google.cloud import storage
from kfp.v2.dsl import Artifact, Output
from kfp.v2.dsl import PIPELINE_JOB_NAME_PLACEHOLDER, Output
from kfp.v2.components.component_factory import create_component_from_func

BUCKET_NAME = 'vertex-ai-test-365213-vertex-pipelines-us-central1'


def register_asset(
        bucket: str,
        blob_name: str,
        artifact_output: Output[Artifact],
        # Forces to invalidate cache when file has changed
        checksum: str,
        # Forces to invalidate cache for different pipeline names
        job_id: str = PIPELINE_JOB_NAME_PLACEHOLDER
):
    from google.cloud import storage

    client = storage.Client()
    bucket = client.get_bucket(bucket)
    blob = bucket.blob(blob_name)
    blob.download_to_filename(artifact_output.path)


def register_asset_op(file_name: str):
    file_content = open(file_name).read()
    checksum = hashlib.md5(file_content.encode()).hexdigest()
    client = storage.Client()
    bucket = client.get_bucket(BUCKET_NAME)
    blob = bucket.blob(file_name)
    blob.upload_from_string(file_content)
    component = create_component_from_func(
        register_asset,
        packages_to_install=['google-cloud-storage']
    )
    op = component(
        blob_name=file_name, checksum=checksum, bucket=BUCKET_NAME
    )
    return op
