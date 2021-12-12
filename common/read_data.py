import yaml
import json

from configparser import ConfigParser
# configparser 用来读取配置文件的包
from common.logger import logger


class MyConfigParser(ConfigParser):
    # 重构 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr: str) -> str:
        return optionstr


class ReadFileData():
    def __init__(self):
        pass

    def load_yaml(self, file_path):
        logger.info("加载 {} 文件中....".format(file_path))
        with open(file_path, encoding='UTF-8') as f:
            data = yaml.safe_load(f)
        logger.info("读取数据 ===> {}".format(data))
        return data

    def load_json(self, file_path):
        logger.info("加载 {} 文件....".format(file_path))
        with open(file_path, encoding="UTF-8") as f:
            data = json.load(f)
        logger.info("读取数据 ===> {}".format(data))
        return data

    def load_ini(self, file_path):
        logger.info("加载 {} 文件....".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        logger.info(data)
        return data


data = ReadFileData()
