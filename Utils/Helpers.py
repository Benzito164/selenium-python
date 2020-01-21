from selenium import webdriver

from Utils.folder_structure_builder import FolderStructureBuilder


class Helpers:

    @classmethod
    def take_screenshot(cls, browser, filename):
        location = f'{FolderStructureBuilder.failed_screenshot_folder}/{filename}.png'
        browser.get_screenshot_as_file(location)

