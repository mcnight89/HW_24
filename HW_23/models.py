from typing import Any, Dict

from marshmallow import Schema, ValidationError, fields, validates_schema

VALID_CMD_COMMANDS = ('filter', 'unique', 'map', 'limit', 'sort')


class RequestSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)
    file_name = fields.Str()

    @validates_schema
    def check_all_cmd_valid(self, values: Dict[str, str], *args: Any, **kwargs: Any) -> None:
        if values['cmd'] not in VALID_CMD_COMMANDS:
            raise ValidationError('"cmd" contain invalid value')


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestSchema, many=True)
