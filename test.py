from selene import have
from selene.support.shared import browser


def test_search_git():
    browser.open('https://google.com')
    browser.element('[name=q]').type('git').press_enter()
    browser.element('#search').should(have.text('https://git-scm.com'))
