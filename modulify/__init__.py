from .camel_to_snake import camel_to_snake
from .create_package_directory import create_package_directory

CLASS = 'CLASS'
FUNCTION = 'FUNCTION'
IMPORT = 'IMPORT'
DECORATOR = 'DECORATOR'

ENTITIES = {
    CLASS: ['class'],
    FUNCTION: ['def'],
    IMPORT: ['import', 'from'],
    DECORATOR: ['@'],
}
