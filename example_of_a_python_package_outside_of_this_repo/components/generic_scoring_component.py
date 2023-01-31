from kfp.v2.components.component_factory import create_component_from_func
from kfp.v2.dsl import Artifact, Input, Output, Model


def dummy_scoring_with_artifact(
        text: str,
        model_module_path: str,
        model_file: Input[Artifact],
        model: Input[Model]
) -> str:
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
    #
    # Data would be loaded here
    #
    # Data science specific logic called inside train
    model = Model()
    model.transform()
    model.predict()

    # MLOps shared logic
    print('Doing something else after')

    return text


def dummy_scoring_with_artifact_op(**kwargs):
    base_image = kwargs.pop('base_image', 'python:3.7')
    component = create_component_from_func(
        func=dummy_scoring_with_artifact,
        base_image=base_image
    )
    task = component(**kwargs)
    return task
