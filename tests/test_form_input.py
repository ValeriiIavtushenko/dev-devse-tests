from selene import by, be
from selene.support.shared import browser
import time


def test_user_info_input():

    browser.open('https://dev.devse.xyz/register')
    browser.element(by.name('first_name')).should(be.blank).type('Sergey')
    browser.element(by.name('last_name')).should(be.blank).type('Yurchenko')
    browser.element(by.name('email')).should(be.blank).type('testtest@mail.com')
    browser.element(by.name('phone')).should(be.blank).type('+380664443332')
    browser.element(by.name('password')).should(be.blank).type('qwerty23')
    browser.element(by.name('password_confirmation')).should(
        be.blank).type('qwerty23')
    browser.element(by.name('terms')).click()
    browser.element(by.xpath('/html/body/div/div/div[2]/form/div[8]/button'))\
        .click()
    time.sleep(4)
