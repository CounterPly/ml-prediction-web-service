import json
import logging
import logging.config

from utils import LOGGING_CONFIGS_PATH


class Logger:
    """
    This is a utility to write the web service logs.

    :Author: Pranay Chandekar
    """

    __instance = None

    def __init__(self):
        """
        This method initialized the Logger utility.
        """
        with open(LOGGING_CONFIGS_PATH) as f:
            configs_dict = json.load(f)

        logging.config.dictConfig(configs_dict)

        self.logger = logging.getLogger("fileLogger")
        self.log_err = logging.getLogger("errLogger")

        Logger.__instance = self

    @staticmethod
    def get_instance():
        """
        This method returns an instance of the Logger utility.

        :return: The Logger utility instance.
        """
        if Logger.__instance is None:
            Logger()
        return Logger.__instance
