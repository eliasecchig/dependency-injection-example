# Showcase creation of components that accept a file passed by the Data Scientists
Setup:
```commandline
pip install poetry
poetry install
```
Before triggering the pipeline you should edit the `project` and `pipeline_root` in `example_of_a_python_package_outside_of_this_repo/model_wrapper_interface.py`

Trigger pipeline:
```commandline
PYTHONPATH=. poetry run python my_model/pipeline.py    
```