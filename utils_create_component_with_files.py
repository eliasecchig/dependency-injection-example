from pathlib import Path
from kfp.v2.components.component_factory import create_component_from_func


def create_component_from_func_with_files(
    files_to_be_included: list, component_from_func_options: dict, component_args: dict
):
    """
    This function creates and initialize a component in KFP, by adding to it's context a list of files
    that can be used at runtime by the component itself. It will do it by:
     1) reading the content of the files they need to be included
     2) create a bash command so that these files can be saved in the local disk of the task at runtime and available as
        part of the PYTHONPATH
     3) initialize the component with the orchestrator parameters
     4) place the bash command that will create the files inside the command which echoes the function code.
     This way here, before the component runs, the files required by the component will be saved in disk and they will
     be available at runtime
    :param files_to_be_included: list of relative paths of the files to be imported
    :param component_from_func_options: dictionary containing any argument that needs to be passed to the create_component_from_func in kfp.
    :param component_args: dictionary containing any argument that needs to be passed to the component itself.
    :return: a component initialized with the parameters
    """
    component = create_component_from_func(**component_from_func_options)
    task = component(**component_args)

    command_prefix = 'export PYTHONPATH="${PYTHONPATH}:${PWD}" && '
    for file_path_str in files_to_be_included:
        file_path = Path(file_path_str)
        file_content = file_path.read_text()
        # remove double quotes as they might clash with the echo command
        file_content = file_content.replace('"', "'")
        file_name = file_path.name
        folder_path = file_path.parent
        command_prefix = (
            command_prefix + f'mkdir -p {folder_path} && echo """{file_content}""" >  {folder_path}/{file_name} && '
        )
    command = task.container_spec.command
    command[2] = command_prefix + command[2]
    task.command = command
    return task
