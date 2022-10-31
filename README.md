# Showcase component creation with files

This repo aims to showcase an utility tool function that is able to create components with files included in it. 

<b>The utility tool code can be found in [utils_create_component_with_files.py](mlops_package_example/utils/create_component_with_files.py)</b>

### Why this is important? 
KFP and VAI pipelines users, have currently 2 ways to create components:
- Via a function based component, where the content of a function gets serialized as component
- Via the creation of a "reusable" component. This requires the creation of a container which contains the files and the 
  environment for the component to run. 

Both approaches have pros and cons. The function based one, allows users to iterate really quickly so it's typically preferred
but to the other side, it doesn't allow users to add any other python file to it, resulting in a major cause of duplication of code in the best scenario. A
Additionally, this means that ML model logic is coupled together with the component logic. It will be difficult for a Data Scientist to take the ML model logic and run it somewhere else.

The "reusable" component approach allows users to split the code of your component in different files, but to the other side
has a slower development process as for any change to the code it requires the user to build and push a new container image.

### Including files as part of function based components

Because of the mentioned pros and cons, I wanted to find a 3rd way, which can potentially keep all the benefits of the 
lightweight components but solving the pain point it has on adding external files. 

I created a small utility function, which leverages the same mechanism of the function based components: the code of the 
function gets read and stored as command in the container spec of the component. With the only difference that here we are 
not only doing it for the component function, but we are also doing it for external files. 

###  Results
This mechanism here, is being in production for 1 full year in my previous company. All the pipelines in production there use this approach
to add external files. What I typically saw, is that most of the time this gets used to import into the component the ML model logic,
which doesn't need to be stored in the component itself. 

### Caveats
There is some small additional logic required to support `google_cloud_pipeline_components.experimental.custom_job.components.create_custom_training_job_op_from_component` function,
nothing too complex to do, it should be ~5/6 additional lines of code. 

### Alternatives
- An alternative I used for long YAML configuration files, which can be used for python files too is to:
  - upload the file you want to import to GCS
  - download the artifact at runtime. I used a checksum to invalidate the caching mechanism in case the file changed
  This approach works well for configuration files, but using it for a python files has 2 limitations:
  - it adds overhead as the artifact needs to be downloaded and imported on the fly by the author of the component
  - might make the unit testing experience really painful
  - it adds overhead in the inputs the component requires
- We could do something similar alternative with the exception of not saving the file as artifact. This approach has similar
  cons to the above, it has the pros that it makes it easier to download a full folder but to the other side access to GCS is always required or during unit test it needs to be mocked. 

### Running the example
Install poetry:
```commandline
pip install poetry
```

Setup the poetry environment:
```commandline
poetry install
```

Before triggering the pipeline, you should change the `project` parameter and the `pipeline_root` in the `pipeline.py` file.
Trigger pipeline:
```commandline
poetry run python pipeline.py
```




  