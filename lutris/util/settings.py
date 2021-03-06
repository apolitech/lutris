import os
import configparser


class SettingsIO(object):
    """ConfigParser abstraction."""
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        if os.path.exists(self.config_file):
            self.config.read([self.config_file])

    def read_setting(self, key, section='lutris'):
        try:
            value = self.config.get(section, key)
        except configparser.NoOptionError:
            value = None
        except configparser.NoSectionError:
            value = None
        return value

    def write_setting(self, key, value, section='lutris'):
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, str(value))

        with open(self.config_file, 'w') as config_file:
            self.config.write(config_file)
