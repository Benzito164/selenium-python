import json
import logging

from Utils.config_reader import read_config_file
from Utils.constant import CONFIG_ENABLE_LOGGING, CONFIG_BUILD_FOLDER_STRUCTURE, CONFIG_LOGGING_METHOD
from Utils.folder_structure_builder import FolderStructureBuilder

config = read_config_file()


class LogHelper:

    @staticmethod
    def setup_logs():
        if config[CONFIG_ENABLE_LOGGING] == "True" and config[CONFIG_BUILD_FOLDER_STRUCTURE] == "True":
            if config[CONFIG_LOGGING_METHOD] == 'file':
                logging.basicConfig(filename=FolderStructureBuilder.logfile_folder + '/info.log',
                                    format='%(asctime)s:%(message)s',
                                    level=logging.INFO)
            else:
                logging.basicConfig(
                    format='%(asctime)s:%(message)s',
                    level=logging.INFO)
        return logging

    @staticmethod
    def initialize_logger():
        logging.basicConfig(filename=FolderStructureBuilder.logfile_folder + '/info.log',
                            format='%(levelname)s:%(message)s',
                            level=logging.INFO)
        return logging
