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
def test_issue_name_pure_selene():
    allure.attach('Тест', name='Text', attachment_type=attachment_type.TEXT)
    browser.open('https://github.com')

    browser.element('.header-search-input').set_value('yashaka/selene').press_enter()
    browser.element(by.link_text('yashaka/selene')).click()
    browser.element('#issues-tab').click()

    browser.element(by.link_text('Docs for Selene? :D')).should(be.visible)
