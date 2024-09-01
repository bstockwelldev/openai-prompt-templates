import json
import yaml

def parse_json(json_string):
    return json.loads(json_string)

def to_json(data):
    return json.dumps(data, indent=4)

def parse_yaml(yaml_string):
    return yaml.safe_load(yaml_string)

def to_yaml(data):
    return yaml.safe_dump(data)
