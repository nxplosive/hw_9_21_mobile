from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_ios(ios_management):
    with step('Click button'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()

    with step('Verify content found'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).type("hello@browserstack.com" + "\n")
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(have.text("hello@browserstack.com"))