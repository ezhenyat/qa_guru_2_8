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
def test_issue_name_decorator_steps():
    allure.attach('Тест', name='Text', attachment_type=attachment_type.TEXT)
    open_main_page()
    find_repository('yashaka/selene')
    go_to_repository('yashaka/selene')
    open_issues_tab()
    should_see_issue_with_name('Docs for Selene? :D')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Ищем репозиторий {repo}')
def find_repository(repo):
    browser.element('.header-search-input').set_value(repo).press_enter()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Переходим в таб Issues')
def open_issues_tab():
    browser.element('#issues-tab').click()


@allure.step('Проверяем наличие Issue с названием {name}')
def should_see_issue_with_name(name):
    browser.element(by.link_text(name)).should(be.visible)
