
#!/usr/bin/python
from pathlib import Path
import sys
import os
import re

from modulify import camel_to_snake, create_package_directory, get_entity, write_entity, ENTITIES, IMPORT, DECORATOR



init_file_content = ''



for file_address in sys.argv[1:]:
    app_name, working_directory, file_name = create_package_directory(file_address=file_address)
    with open(file_address, 'r') as working_file:
        processed_entities = set()
        current_entity_dependencies = set()

        init_file_content = ''
        imports = ""
        current_entity_type = ""
        current_entity_name = None
        current_entity_result = ''

        previous_entity = IMPORT
        line_number = 0

        for line in working_file:
            line_number += 1
            current_entity_type = get_entity(line)

            print(line_number, current_entity_type, previous_entity, current_entity_name, line, end='')

            if current_entity_type is not None and previous_entity is not None:
                if previous_entity not in [IMPORT, DECORATOR] and current_entity_name is not None:
                    write_entity(
                        working_directory=working_directory, current_entity_name=current_entity_name, imports=imports, current_entity_result=current_entity_result, current_entity_dependencies=current_entity_dependencies, file_name=file_name, app_name=app_name
                    )
                    current_entity_result = ''
                    current_entity_name = None
                    current_entity_dependencies = set()

                if current_entity_type != DECORATOR:
                    current_entity_name = line.split(' ')[1].split('(')[0]
                    processed_entities.add(current_entity_name)
                previous_entity = current_entity_type

            if previous_entity == IMPORT:
                imports += line
            else:
                for processed_entity in processed_entities:
                    if processed_entity in line and processed_entity != current_entity_name:
                        current_entity_dependencies.add(processed_entity)

                current_entity_result += line
                
                if file_name == 'models.py' and 'class Meta' in line:
                    current_entity_result += line.split('class Meta')[0] + f"\tapp_label = '{app_name}'\n"


        write_entity(
            working_directory=working_directory, current_entity_name=current_entity_name, imports=imports, current_entity_result=current_entity_result, current_entity_dependencies=current_entity_dependencies, file_name=file_name, app_name=app_name
        )

        with open(working_directory + os.sep + '__init__.py', 'w') as init_file:
            init_file.write(init_file_content)
