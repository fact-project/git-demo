import json
import yaml


def json2yaml(json_string):
    data = json.loads(json_string)
    yaml_string = yaml.dump(data)
    return yaml_string
