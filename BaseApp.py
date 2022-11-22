from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException,StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://hb-beta.stage.sirenltd.dev/walk-in-showers"

    def find_element_to_click(self, locator, time=120):
        try:
            return WebDriverWait(self.driver, time,
                                 ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                     StaleElementReferenceException]).until(
                EC.element_to_be_clickable(locator))
        except TimeoutError:
            print(f"Can't find element by locator")

    def find_element(self, locator, time=120):
        try:
            return WebDriverWait(self.driver, time,
                                 ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                     StaleElementReferenceException]).until(
                EC.presence_of_element_located(locator),
                message=f"Can't find element by locator {locator}")
        except TimeoutError:
            print(f"Can't find element by locator")

    def find_elements(self, locator, time=120):
        try:
            return WebDriverWait(self.driver, time,
                                 ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                     StaleElementReferenceException]).until(
                EC.presence_of_all_elements_located(locator),
                message=f"Can't find elements by locator {locator}")
        except TimeoutError:
            print(f"Can't find element by locator")

    def go_to_site(self):
        return self.driver.get(self.base_url)



    # def go_screenshot(self):
    #     self.capture_path = '/Users/leokhanin/Downloads/screen/your_desired_filename.png'
    #     self.driver.save_screenshot(self.capture_path)
