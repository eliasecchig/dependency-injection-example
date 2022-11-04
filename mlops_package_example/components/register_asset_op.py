import hashlib

from google.cloud import storage

from kfp.v2.dsl import Artifact
from kfp.v2.dsl import importer

BUCKET_NAME = 'vertex-ai-test-365213-vertex-pipelines-us-central1'


def register_asset_op(file_name: str):
    client = storage.Client()
    file_content = open(file_name).read()
    checksum = hashlib.md5(file_content.encode()).hexdigest()
    bucket = client.get_bucket(BUCKET_NAME)
    blob = bucket.blob(f'{checksum}/{file_name}')
    blob.upload_from_string(file_content)
    op = importer(
        artifact_uri=f'gs://{BUCKET_NAME}/{checksum}/{file_name}',
        artifact_class=Artifact
    )
    return op
