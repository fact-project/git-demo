def test_json2yaml():
    from json2yaml import json2yaml

    json = '{"test": 2}'

    yaml = json2yaml(json)

    assert yaml == 'test: 2\n'


def test_json2yaml2():
    from json2yaml import json2yaml

    json = '{"foo": 5}'

    yaml = json2yaml(json)

    assert yaml == 'foo: 5\n'
