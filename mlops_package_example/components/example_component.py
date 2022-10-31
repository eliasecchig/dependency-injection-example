from mlops_package_example.utils.create_component_with_files import create_component_from_func_with_files


def dummy_training(text: str, model_module_path: str) -> str:

    # MLOps shared logic
    from importlib import import_module
    print('Dummy Loading data')
    package, module = model_module_path.rsplit(".", 1)
    Model = getattr(import_module(package), module)
    model = Model()
    # Data science specific logic called inside train
    model.train()

    # MLOps shared logic
    print('Doing something else after')

    return text


def dummy_training_op(**kwargs):
    task = create_component_from_func_with_files(
        files_to_be_included=[
            # Hardcoding here, in real life the file path would be dynamically extracted based on the model_module_path value
            'my_model/dummy_model.py'
        ],
        component_from_func_args={
            "func": dummy_training,
            "base_image": "python:3.7"
        },
        component_args=kwargs,
    )
    return task
