import logging
import pytest
from selenium.webdriver import Chrome, Firefox


from Utils.Helpers import Helpers
from Utils.config_reader import read_config_file
from Utils.constant import CONFIG_BROWSER, CONFIG_WAIT_TIME, CONFIG_CHROME_DRIVER_PATH
from Utils.folder_structure_builder import FolderStructureBuilder
from Utils.log_helper import LogHelper

DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']

folder = FolderStructureBuilder()
folder.build_folder_structure()
logging = LogHelper.setup_logs()


@pytest.fixture(scope='session')
def read_config():
    return read_config_file()


@pytest.fixture(scope='session')
def config_browser(read_config):
    if CONFIG_BROWSER not in read_config:
        raise Exception('The config file doesnt contain "browser"')
    elif read_config[CONFIG_BROWSER] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{read_config[CONFIG_BROWSER]}" is not supported')
    return read_config[CONFIG_BROWSER]


@pytest.fixture(scope='session')
def config_chrome_driver_path(read_config):
    if CONFIG_CHROME_DRIVER_PATH not in read_config:
        raise Exception('The config file doesnt contain the chromedriver path')
    else:
        return read_config[CONFIG_CHROME_DRIVER_PATH]


@pytest.fixture(scope='session')
def config_wait_time(read_config):
    return read_config[CONFIG_WAIT_TIME] if CONFIG_WAIT_TIME in read_config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def browser(config_browser, config_chrome_driver_path, config_wait_time):
    if config_browser == 'chrome':
        driver = Chrome(config_chrome_driver_path)
    elif config_browser == 'firefox':
        driver = Firefox()
    else:
        raise Exception(f'"{read_config[CONFIG_BROWSER]}" is not supported')
    driver.implicitly_wait(config_wait_time)
    yield driver
    driver.quit()


@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope='function', autouse=True)
def before_after_each_test(request, browser):
    logging.info(f'executing {request.node.name}')
    yield
    if request.node.rep_call.passed:
        Helpers.take_screenshot(browser, request.node.name)
        logging.info(f'Test Pass => {request.node.name}')
    elif request.node.rep_call.failed:
        yield
        logging.info(f'Test Failed => {request.node.name}')


@pytest.fixture(scope='class', autouse=True)
def before_after_each_class(request):
    module_name = request.module.__name__
    logging.info(f'==== Executing test in {module_name} class ====')
    yield
    logging.info(f'==== Completed executing test in {module_name} class ====')
