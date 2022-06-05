import storage.config as cfg

class Token():
    def __init__(self):
        self.jsonObject = cfg.Config(cfg.tokenConfigPath).get_json_object()

    def get_token_list(self):
        return self.jsonObject

    def add(self, name, token, prefix):
        cfg.Config(cfg.tokenConfigPath).add_json_section(self.jsonObject, name)
        cfg.Config(cfg.tokenConfigPath).edit_json_value_double(self.jsonObject, name, "token", token)
        cfg.Config(cfg.tokenConfigPath).edit_json_value_double(self.jsonObject, name, "prefix", prefix)

    def remove(self, name):
        cfg.Config(cfg.tokenConfigPath).remove_json_section(self.jsonObject, name)

    def get_property(self, name, property):
        return cfg.Config(cfg.tokenConfigPath).get_json_value_double(self.jsonObject, name, property)