import random
import string
import time
from selenium import webdriver
import allure
import pytest

from SIrenaPage import SearchHelper


@pytest.mark.parametrize("zip_code,expected",
                         [("00001", True), ("00002", True), ("125167", False),
                          ("012", False), ("test", False)])
def test_1(browser, zip_code, expected):
    with allure.step(f"Проверка окна zip_code c параметрами {zip_code, expected}"):
        main_page = SearchHelper(browser)
        main_page.go_to_site()
        main_page.enter_zip_code(zip_code)
        assert main_page.check_rightIcon().is_displayed() == expected


def test_2(browser):
    with allure.step(f"Проверка ввода ответов на вопросы с вариантами ответа"):
        with allure.step("Вход со стандартным zip_code "):
            main_page = SearchHelper(browser)
            main_page.go_to_site()
            main_page.enter_zip_code("00001")
            main_page.get_estimate_button().click()
            assert main_page.question_1().text == "Ease of use"

        with allure.step(f"Ввод ответа на первый вопрос Which feature is most important to you? Множественный выбор "):
            '''
            пердпоготовка блока отвечающего за проверку изменения в __dict__["_id"] проверяем по первому вопросу
            '''
            q1_past = q1_future = main_page.question_1().__dict__["_id"]
            print(f'\nСтарый id  {q1_past}')
            '''
            выход из предпоготовки
            '''
            main_page.question_1().click()
            main_page.question_2().click()
            main_page.question_not_sure().click()
            assert main_page.question_1().is_enabled() is True
            assert main_page.question_2().is_enabled() is True
            assert main_page.question_not_sure().is_enabled() is True
            main_page.next_button().click()

        with allure.step(f"Ввод ответа на второй вопрос Describe your project, переменный выбор"):
            '''
            блок отвечающий за смену  __dict__["_id"]
            '''
            start = time.monotonic()
            end = time.monotonic()
            while q1_past == q1_future or end - start < 50:
                q1_future = main_page.question_1().__dict__["_id"]
                end = time.monotonic()

            print(f'id сменился на q1_future {q1_future}')

            q1_past = q1_future = main_page.question_1().__dict__["_id"]

            main_page.question_1().click()
            assert main_page.question_1().is_enabled() is True

            main_page.question_2().click()
            assert main_page.question_2().is_enabled() is True

            main_page.question_not_sure().click()
            assert main_page.question_not_sure().is_enabled() is True
            main_page.next_button().click()

        with allure.step(f"Ввод ответа на 3й вопрос Select your shower layout., переменный выбор"):
            print(f'Старый id  {q1_future}')
            start = time.monotonic()
            end = time.monotonic()
            while q1_past == q1_future or end - start < 50:
                q1_future = main_page.question_1().__dict__["_id"]
                end = time.monotonic()
            print(f'id сменился на q1_future {q1_future}')

            main_page.question_1().click()
            assert main_page.question_1().is_enabled() is True

            main_page.question_2().click()
            assert main_page.question_2().is_enabled() is True

            main_page.question_not_sure().click()
            assert main_page.question_not_sure().is_enabled() is True
            main_page.next_button().click()


def test_3(browser):
    with allure.step(f"Проверка ввода YES NO вопросов и ввода даных клиента"):
        with allure.step("Вход со стандартным zip_code и ответами на вопросы c выбором ответа , до YES NO вопросов"):
            main_page = SearchHelper(browser)
            main_page.go_to_site()
            main_page.enter_zip_code("00001")
            main_page.get_estimate_button().click()

            '''
            пердпоготовка блока отвечающего за проверку изменения в __dict__["_id"] проверяем по первому вопросу
            '''

            q1_past = q1_future = main_page.question_1().__dict__["_id"]
            print(f'\nСтарый id  {q1_past}')

            '''
            выход из предпоготовки
            '''

            main_page.question_1().click()
            assert main_page.question_1().is_enabled() is True
            main_page.next_button().click()

            '''
            блок отвечающий за смену  __dict__["_id"]
            '''

            start = time.monotonic()
            end = time.monotonic()
            while q1_past == q1_future or end - start < 50:
                q1_future = main_page.question_1().__dict__["_id"]
                end = time.monotonic()
            print(f'id сменился на q1_future {q1_future}')
            q1_past = q1_future = main_page.question_1().__dict__["_id"]
            main_page.question_1().click()
            assert main_page.question_1().is_enabled() is True
            main_page.next_button().click()
            print(f'Старый id  {q1_future}')
            start = time.monotonic()
            end = time.monotonic()
            while q1_past == q1_future or end - start < 50:
                q1_future = main_page.question_1().__dict__["_id"]
                end = time.monotonic()
            print(f'id сменился на q1_future {q1_future}')
            main_page.question_1().click()
            assert main_page.question_1().is_enabled() is True
            main_page.next_button().click()

        with allure.step(f"Первый вопрос: Are you the homeowner or authorized to make property changes?"):

            yes_past = yes_future = main_page.yes_button().__dict__["_id"]

            print(f'\nСтарый id yes_past {yes_past}')

            start = time.monotonic()
            end = time.monotonic()
            while yes_past == yes_future or end - start < 50:
                yes_future = main_page.yes_button().__dict__["_id"]
                end = time.monotonic()
            yes_past = yes_future = main_page.yes_button().__dict__["_id"]
            print(f'id сменился на yes_future {yes_future}')

            main_page.yes_button().click()
            assert main_page.next_button().is_enabled() is True
            main_page.no_button().click()
            assert main_page.alert().text == "Our installers require the homeowner or someone authorized to make property changes be present during the estimate. Would you like to continue?"
            main_page.confirmation_yes().click()

        with allure.step(f"Второй вопрос: Is it a mobile, modular or manufactured home?"):
            print(f'\nСтарый id yes_past  {yes_past}')
            start = time.monotonic()
            end = time.monotonic()
            while yes_past == yes_future or end - start < 50:
                yes_future = main_page.yes_button().__dict__["_id"]
                end = time.monotonic()
            print(f'id сменился на yes_future {yes_future}')
            yes_past = yes_future = main_page.yes_button().__dict__["_id"]

            main_page.no_button().click()
            assert main_page.next_button().is_enabled() is True
            main_page.yes_button().click()
            assert main_page.alert().text == "Unfortunately, our installers do not work with mobile, modular or manufactured homes. Would you still like to continue?"
            main_page.confirmation_yes().click()

        with allure.step(f"Третий вопрос: Is there an existing bathtub or shower that we would be replacing?"):
            print(f'\nСтарый id yes_past  {yes_past}')
            start = time.monotonic()
            end = time.monotonic()
            while yes_past == yes_future or end - start < 50:
                yes_future = main_page.yes_button().__dict__["_id"]
                end = time.monotonic()
            print(f'id сменился на yes_future {yes_future}')
            yes_past = yes_future = main_page.yes_button().__dict__["_id"]
            main_page.yes_button().click()
            assert main_page.next_button().is_enabled() is True
            main_page.no_button().click()
            assert main_page.alert().text == "Unfortunately, our installers can only replace an existing bathtub or shower. Would you still like to continue?"
            main_page.confirmation_yes().click()

        with allure.step(f"Четвертый вопрос: Is this request covered by an insurance or VA claim?"):
            print(f'\nСтарый id yes_past  {yes_past}')
            start = time.monotonic()
            end = time.monotonic()
            while yes_past == yes_future or end - start < 50:
                yes_future = main_page.yes_button().__dict__["_id"]
                end = time.monotonic()
            print(f'id сменился на yes_future {yes_future}')
            yes_past = yes_future = main_page.yes_button().__dict__["_id"]
            main_page.no_button().click()
            assert main_page.next_button().is_enabled() is True
            main_page.yes_button().click()
            assert main_page.alert().text == "Unfortunately, our installers do not currently work with insurance or VA claims. Would you still like to continue?"
            main_page.confirmation_yes().click()

        # with allure.step(f"Акция !!! Seniors and the military (active/retired/spouses) get an extra 10% OFF!"):
        #     not_sure_past = not_sure_future = main_page.question_not_sure().__dict__["_id"]
        #     print(f'\nСтарый id not_sure {not_sure_past}')
        #     start = time.monotonic()
        #     end = time.monotonic()
        #     while not_sure_past == not_sure_future or end - start < 50:
        #         not_sure_future = main_page.yes_button().__dict__["_id"]
        #         end = time.monotonic()
        #     print(f'id сменился на not_sure_future {not_sure_future}')
        #     main_page.question_not_sure().click()
        #     main_page.next_button().click()

        with allure.step(f"Ввод FullName и Email"):
            def randomword(length):
                letters = string.ascii_lowercase
                return ''.join(random.choice(letters) for i in range(length))

            main_page.enter_full_name("Khanin")
            main_page.enter_email(randomword(10))
            main_page.next_button().click()
            lst = main_page.allerts()
            assert 'Your full name should contain both first and last name' in lst
            assert 'Wrong email' in lst

            main_page.enter_full_name(" Leonid")
            main_page.enter_email("@yandex.rus")
            main_page.next_button().click()

        with allure.step(f"Ввод и подтверждение телефонного номера"):

            main_page.enter_phone_number("555")
            main_page.submit_my_request().click()
            lst = main_page.allerts()
            assert "Invalid Phone number" in lst
            main_page.enter_phone_number("5551234")
            main_page.submit_my_request().click()
            main_page.phone_number_is_correct().click()


def test_4(browser):
    with allure.step(f"Проверка кнопки закрытия "):
        with allure.step("Вход со стандартным zip_code и ответами на вопросы c выбором ответа , до YES NO вопросов"):
            main_page = SearchHelper(browser)
            main_page.go_to_site()
            main_page.enter_zip_code("00001")
            main_page.get_estimate_button().click()
            print(main_page.exit_button())
            main_page.exit_button().click()
            assert main_page.allet_in_exit().text == "We just need to confirm your information to get you a quote."
            main_page.return_to_project().click()
            main_page.question_1().click()
            assert main_page.question_1().is_enabled() is True


def test_5(browser):
    with allure.step(f"Проверка кннопки I'm a contractor"):
        main_page = SearchHelper(browser)
        main_page.go_to_site()
        main_page.i_am_contractor().click()
        print( main_page.i_am_contractor_button().text)
        assert main_page.i_am_contractor_button().text == 'Book a call'

