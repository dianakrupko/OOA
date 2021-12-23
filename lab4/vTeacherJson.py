import jsonschema
import simplejson as json

with open('jsonSchemaTeacher.json', 'r') as f:
    schema_data = f.read()
schema = json.loads(schema_data)

json_obj = {"name": "Diana Krupko",
            "qualification": "senior teacher",
            "phone": 380971337911}
jsonschema.validate(json_obj, schema)
