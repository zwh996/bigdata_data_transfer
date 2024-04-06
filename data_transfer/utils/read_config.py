import json
import yaml

global subscriber_sys_config


# Extract the config data form yaml file
def init_config_file(config):
    with open(config, 'r') as stream:
        try:
            global subscriber_sys_config
            subscriber_sys_config = json.loads(json.dumps(yaml.safe_load(stream)))
            print(subscriber_sys_config)

        except yaml.YAMLError as exc:
            stream.close()
            print(exc)
        except json.JSONDecodeError as exc:
            stream.close()
            print(exc)

        finally:
            stream.close()
            return subscriber_sys_config


def load_sys_config_value(key):
    return subscriber_sys_config[key]
