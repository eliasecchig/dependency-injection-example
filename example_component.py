from utils_create_component_with_files import create_component_from_func_with_files


def hello_world(text: str) -> str:
    from my_model.dummy_model import Model
    Model.hello_world()
    return text


def example_hello_world_op(**kwargs):
    task = create_component_from_func_with_files(
        files_to_be_included=['my_model/dummy_model.py'],
        component_from_func_args={
            "func": hello_world,
            "base_image": "python:3.7"
        },
        component_args=kwargs,
    )
    return task
