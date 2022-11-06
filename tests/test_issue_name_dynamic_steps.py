import allure
from allure import attachment_type
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


@allure.tag('web', 'smoke')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'ezhenyat')
@allure.feature('Задачи в репозитории')
@allure.story('Авторизованный пользователь может создать задачу в репозитории')
@allure.link('https://github.com', name='Testing')
def test_issue_name_dynamic_steps():
    allure.attach('Тест', name='Text', attachment_type=attachment_type.TEXT)

    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий'):
        browser.element('.header-search-input').set_value('yashaka/selene').press_enter()

    with allure.step('Переходим по ссылке из репозитория'):
        browser.element(by.link_text('yashaka/selene')).click()

    with allure.step('Переходим в таб Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие Issue'):
        browser.element(by.link_text('Docs for Selene? :D')).should(be.visible)
