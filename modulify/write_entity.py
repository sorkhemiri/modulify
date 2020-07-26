import os

from . import camel_to_snake


def write_entity(
    working_directory,
    current_entity_name,
    imports,
    current_entity_result,
    current_entity_dependencies,
    file_name,
    app_name,
):
    snake_case_name = camel_to_snake(current_entity_name)

    with open("__init.tmp", "a") as init_file:
        init_file.write(
            f"from .{snake_case_name} import {current_entity_name}{os.linesep}"
        )

    with open(
        working_directory + os.sep + snake_case_name + ".py", "w"
    ) as new_entity_file:
        head, module = os.path.split(working_directory)
        _, package = os.path.split(head)
        for current_entity_dependency in current_entity_dependencies:
            print(
                module,
                package,
                current_entity_name,
                f"from {package}.{module}.{camel_to_snake(current_entity_dependency)} import {current_entity_dependency}",
            )
            new_entity_file.write(
                f"from {package}.{module}.{camel_to_snake(current_entity_dependency)} import {current_entity_dependency}{os.linesep}"
            )

        new_entity_file.write(imports)
        new_entity_file.write(current_entity_result)

        if (
            "class Meta" not in current_entity_result
            and "class" in current_entity_result
            and file_name == "models.py"
        ):
            new_entity_file.write(f"\tclass Meta:\n\t\t\tapp_label = '{app_name}'")
