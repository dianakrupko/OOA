import jsonschema
import simplejson as json

with open('jsonSchemaCourse.json', 'r') as f:
    schema_data = f.read()
schema = json.loads(schema_data)

json_obj={
    "type": "OffsiteCourse",
    "title": "Python Programming",
    "program": [
      "Data types",
      "Variables",
      "Standard input / output",
      "Logic operations"
    ],
    "description": "In this Python programming course, you will learn the basics of programming"}
jsonschema.validate(json_obj, schema)