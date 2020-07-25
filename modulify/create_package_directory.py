import os
from pathlib import Path


def create_package_directory(file_address: str) -> tuple:
	directory, file_name = os.path.split(file_address)
	working_directory = directory + os.sep + file_name.split('.')[0]
	Path(working_directory).mkdir(parents=True, exist_ok=True)
	_, package_name = os.path.split(directory)
	return package_name, working_directory
