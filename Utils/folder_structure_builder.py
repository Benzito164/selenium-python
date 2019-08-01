import errno
import os
from Utils.constant import CONFIG_BUILD_FOLDER_STRUCTURE

from Utils.config_reader import read_config_file

reader = read_config_file()


class FolderStructureBuilder:
    path = os.path.expanduser("~/Desktop")
    main_folder = os.path.join(path, 'Python')
    failed_screenshot_folder = os.path.join(main_folder, 'FailedScreenshot')
    logfile_folder = os.path.join(main_folder, 'Logs')

    paths = [
        main_folder,
        failed_screenshot_folder,
        logfile_folder
    ]

    def build_folder_structure(self):
        if reader[CONFIG_BUILD_FOLDER_STRUCTURE] == 'True':
            try:
                self.create_path()
            except OSError as exception:
                if exception.errno != errno.EEXIST:
                    raise

    @classmethod
    def delete_folder_structure(cls):
        for names in cls.paths:
            os.remove(names)

    def create_path(self):
        for names in self.paths:
            os.makedirs(names)

