from . import ENTITIES


def get_entity(value: str):
    for entity, values in ENTITIES.items():
        if any([True if value.startswith(item) else False for item in values]):
            return entity
    return None
