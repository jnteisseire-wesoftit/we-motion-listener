import configparser


class Config(object):
    def __init__(self, config_file):
        self.config_obj = configparser.ConfigParser()
        self.config_obj.read(config_file)
