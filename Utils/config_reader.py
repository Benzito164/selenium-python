import json

CONFIG_PATH = '~/python-ui-framework/tests/config.json'


class ConfigReader:
    pass


def read_config_file():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
        return data
