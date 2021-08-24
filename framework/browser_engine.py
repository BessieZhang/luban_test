# -*- coding: utf-8 -*-
import ConfigParser
import os.path
from selenium import webdriver
from framework.logger import Logger
from selenium.webdriver.chrome.options import Options
import time

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):

    chrome_driver_path = os.path.dirname(os.path.abspath('.')) + '/tools/chromedriver'

    def __init__(self, driver):
        self.driver = driver

    # read the browser type from config.ini file,return the driver
    def open_browser(self, driver):
        config = ConfigParser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" %url)

        # # 禁止加载图片，提高执行效率
        # chrome_opt = Options()
        # No_Image_loading = {"profile.managed_default_content_settings.images": 2}
        # chrome_opt.add_experimental_option("prefs", No_Image_loading)
        #
        # driver = webdriver.Chrome(self.chrome_driver_path, chrome_options=chrome_opt)

        # chrome_options = Options()
        # chrome_options.add_argument("--headless")

        # driver = webdriver.Chrome(self.chrome_driver_path, chrome_options=chrome_options)
        driver = webdriver.Chrome(self.chrome_driver_path)
        logger.info("Starting Chrome browser.")
        driver.get(url)
        logger.info("Open url: %s" % url)
        time.sleep(3)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()




















