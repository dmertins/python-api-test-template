import json

from jsonschema.exceptions import SchemaError, ValidationError
from jsonschema.validators import validate

from settings import JSON_SCHEMAS_DIR


def json_matches_schema(instance: dict | list, schema_path: str) -> bool:
    """Validate an instance under the given schema."""
    schema = _load_schema_from_file(schema_path)
    return _json_matches_schema(instance, schema)


def _load_schema_from_file(schema_path: str) -> dict:
    schema_file_path = JSON_SCHEMAS_DIR / schema_path
    schema_text = schema_file_path.read_text("utf-8")
    return json.loads(schema_text)


def _json_matches_schema(instance: dict | list, schema: dict) -> bool:
    try:
        validate(instance, schema)
    except (SchemaError, ValidationError):
        raise

    return True
