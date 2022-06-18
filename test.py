from selene import have, be
from selene.support.shared import browser


def test_search_git():
    browser.open('https://google.com')
    browser.element('[name=q]').should(be.blank).type('git').press_enter()
    browser.element('#search').should(have.text('https://git-scm.com'))
