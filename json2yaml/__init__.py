import json
import yaml


def json2yaml(json_string):
    data = json.loads(json_string)
    yaml_string = yaml.dump(data, default_flow_style=False)
    return yaml_string
