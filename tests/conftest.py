import allure
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser

from utils import attach
from settings import config


@pytest.fixture()
def setup_android():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",
            "userName": config.login,
            "accessKey": config.access_key
        }
    })

    with allure.step("Open browserstack"):
        browser.config.driver = webdriver.Remote('http://hub.browserstack.com/wd/hub', options=options)

    yield
    attach.add_screenshot(browser)
    attach.add_xml(browser)
    attach.add_video(browser)

    with allure.step("Tear down"):
        browser.quit()


@pytest.fixture()
def setup_ios():
    options = XCUITestOptions().load_capabilities({
        # Set URL of the application under test
        "app": "bs://sample.app",

        # Specify device and os_version for testing
        "deviceName": "iPhone 11 Pro",
        "platformName": "ios",
        "platformVersion": "13",

        # Set other BrowserStack capabilities
        "bstack:options": {
            "userName": config.login,
            "accessKey": config.access_key,
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test"
        }
    })

    with allure.step("Open browserstack"):
        browser.config.driver = webdriver.Remote('http://hub.browserstack.com/wd/hub', options=options)

    yield
    attach.add_screenshot(browser)
    attach.add_xml(browser)
    attach.add_video(browser)

    with allure.step("Tear down"):
        browser.quit()
