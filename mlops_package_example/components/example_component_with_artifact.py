from kfp.v2.components.component_factory import create_component_from_func
from kfp.v2.dsl import Artifact, Input


def dummy_training_with_artifact(text: str, model_module_path: str, model_file: Input[Artifact]) -> str:
    import importlib.util

    # This function would be installed in the container in a real life scenario
    def import_module_from_string(module_path: str, module_definition: str):
        package_path, module = module_path.rsplit(".", 1)
        spec = importlib.util.spec_from_loader(package_path, loader=None)
        package = importlib.util.module_from_spec(spec)
        exec(module_definition, package.__dict__)
        module_imported = getattr(package, module)
        return module_imported

    Model = import_module_from_string(module_path=model_module_path, module_definition=open(model_file.path).read())
    model = Model()
    # Data science specific logic called inside train
    model.train()

    # MLOps shared logic
    print('Doing something else after')

    return text


dummy_training_with_artifact_op = create_component_from_func(
    dummy_training_with_artifact
)
