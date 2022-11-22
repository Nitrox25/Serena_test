from BaseApp import BasePage
from selenium.webdriver.common.by import By


class SirenaLocators:
    LOCATOR_FILD_ENTER_ZIP_CODE = (By.CSS_SELECTOR, ".zip--container label")
    LOCATOR_ENTER_ZIP_CODE = (By.ID, "zipCode")
    LOCATOR_RIGHTICON = (By.CSS_SELECTOR, "#zip_header .rightIcon")
    LOCATOR_BUTTON_GET_ESTIMATE = (By.CSS_SELECTOR, ".BtnPrimary")
    LOCATOR_QUESTION_1 = (By.CSS_SELECTOR, ".mb-2.mb-md-6:nth-child(1)")
    LOCATOR_QUESTION_2 = (By.CSS_SELECTOR, ".mb-2.mb-md-6:nth-child(2)")
    LOCATOR_NOT_SURE = (By.CSS_SELECTOR, ".mb-4.mb-md-6")
    LOCATOR_BUTTON_NEXT = (By.CSS_SELECTOR, ".Btn:nth-child(1)")
    LOCATOR_BUTTON_YES = (By.CSS_SELECTOR, ".mb-2.mb-md-6.mx-md-2")
    LOCATOR_BUTTON_NO = (By.CSS_SELECTOR, ".mb-4.mb-md-6.mx-md-2")
    LOCATOR_ALLERT = (By.CSS_SELECTOR, '.mt-2.mt-md-0')
    LOCATOR_CONFIRMATION_YES = (By.CSS_SELECTOR, ".Btn.mx-2:nth-child(2)")
    LOCATOR_CONFIRMATION_NO = (By.CSS_SELECTOR, ".Btn.mx-2:nth-child(1)")
    LOCATOR_FULL_NAME = (By.NAME, "fullName")
    LOCATOR_EMAIL = (By.NAME, "email")
    LOCATOR_ALLERTS = (By.CSS_SELECTOR, ".h6")
    LOCATOR_PHONE_NUMBER = (By.NAME, "phoneNumber")
    LOCATOR_BUTTON_SUBMIT_MY_REQUEST = (By.CSS_SELECTOR, ".mt-md-0")
    LOCATOR_BUTTON_CORRECT_PHONE = (By.CSS_SELECTOR, "button.Btn.BtnPrimary.mx-0.mx-sm-3.Button")
    LOCATOR_THANK_YOU = (By.CSS_SELECTOR,".font-weight-bold")
    LOCATOR_BUTTON_EXIT = (By.CSS_SELECTOR, ".eEpPJ7gu18iJu2l3wW5F")
    LOCATOR_ALLERT_EXIT = (By.CSS_SELECTOR, "#StepBodyId .text-center.mb-2")
    LOCATOR_BUTTON_RETURN_TO_PROJECT = (By.CSS_SELECTOR,"#StepBodyId .Btn.BtnPrimary.Button")
    LOCATOR_BUTTON_CONTRACTOR = (By.CSS_SELECTOR, ".defaultLink.defaultLink_orange.mt-2")
    LOCATOR_CONTRACTOR_PAGE = (By.CSS_SELECTOR, ".ctrHeader__content .Btn")




class SearchHelper(BasePage):
    def enter_zip_code(self, words):
        self.find_element_to_click(SirenaLocators.LOCATOR_FILD_ENTER_ZIP_CODE).click()
        return self.find_element_to_click(SirenaLocators.LOCATOR_ENTER_ZIP_CODE).send_keys(words)

    def get_estimate_button(self):
        return self.find_element_to_click(SirenaLocators.LOCATOR_BUTTON_GET_ESTIMATE)

    def check_rightIcon(self):
        return self.find_element(SirenaLocators.LOCATOR_RIGHTICON)

    def question_1(self):
        return self.find_element_to_click(SirenaLocators.LOCATOR_QUESTION_1)

    def question_2(self):
        return self.find_element_to_click(SirenaLocators.LOCATOR_QUESTION_2)

    def question_not_sure(self):
        return self.find_element_to_click(SirenaLocators.LOCATOR_NOT_SURE)

    def next_button(self):
        return self.find_element_to_click(SirenaLocators.LOCATOR_BUTTON_NEXT)

    def yes_button(self):
        return self.find_element_to_click(SirenaLocators.LOCATOR_BUTTON_YES)

    def no_button(self):
        return self.find_element_to_click(SirenaLocators.LOCATOR_BUTTON_NO)

    def alert(self):
        return self.find_element(SirenaLocators.LOCATOR_ALLERT)

    def confirmation_yes(self):
        return self.find_element_to_click(SirenaLocators.LOCATOR_CONFIRMATION_YES)

    def enter_full_name(self, words):
        self.find_element_to_click(SirenaLocators.LOCATOR_FULL_NAME).click()
        return self.find_element_to_click(SirenaLocators.LOCATOR_FULL_NAME).send_keys(words)

    def enter_email(self, words):
        self.find_element_to_click(SirenaLocators.LOCATOR_EMAIL).click()
        return self.find_element_to_click(SirenaLocators.LOCATOR_EMAIL).send_keys(words)

    def allerts(self):
        value = self.find_elements(SirenaLocators.LOCATOR_ALLERTS)
        value_lst = [elem.text for elem in value]
        return value_lst

    def enter_phone_number(self, words):
        self.find_element_to_click(SirenaLocators.LOCATOR_PHONE_NUMBER).click()
        return self.find_element_to_click(SirenaLocators.LOCATOR_PHONE_NUMBER).send_keys(words)

    def submit_my_request(self):
        return self.find_element_to_click(SirenaLocators.LOCATOR_BUTTON_SUBMIT_MY_REQUEST)

    def phone_number_is_correct(self):
        return self.find_element_to_click(SirenaLocators.LOCATOR_BUTTON_CORRECT_PHONE)

    def thank_you_page(self):
        return self.find_element(SirenaLocators.LOCATOR_THANK_YOU)

    def exit_button(self):
        return self.find_element_to_click(SirenaLocators.LOCATOR_BUTTON_EXIT)

    def allet_in_exit(self):
        return self.find_element(SirenaLocators.LOCATOR_ALLERT_EXIT)

    def return_to_project(self):
        return self.find_element_to_click(SirenaLocators.LOCATOR_BUTTON_RETURN_TO_PROJECT)

    def i_am_contractor(self):
        return self.find_element_to_click(SirenaLocators.LOCATOR_BUTTON_CONTRACTOR)

    def i_am_contractor_button(self):
        return self.find_element(SirenaLocators.LOCATOR_CONTRACTOR_PAGE)


