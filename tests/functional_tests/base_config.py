#coding: utf-8
import time

try:
    from splinter import Browser
except Exception, e:
    install_command = 'sudo pip install selenium splinter'
    print("Error on import - %s" % e)
    print('Tip: You probably forgot to run "%s".' % install_command)
    exit()


class BaseConfig(object):

    """docstring for BaseConfig"""

    def __init__(self):
        self._browser = Browser("chrome")
        self.countries = ("MLA", "MLB", "MLC", "MCO", "MLM", "MLV", "MPE")
        self.currencies = ('ARS', 'BRL', 'MEX', 'CHI', 'PEN', 'VEF', 'COP')

    def visit_url(self, url_to_visit):
        self._browser.visit(url_to_visit)
        return self

    def get_in_page(self, element_id):
        return self._browser.find_by_id(element_id).first
    
    def url(self):
        return self._browser.url
    
    def exit(self):
        self._browser.exit()

    def then(self):
        return self

    def wait(self, seconds):
        time.sleep(seconds)
        return self

    def fill_data_on_field(self, field_id, field_value):
        self._browser.find_by_id(field_id).first.fill(field_value)
        return self

    def select_data_on_field(self, field_id, field_value):
        self._browser.select(field_id, field_value)
        return self

    def click_on_element(self, element_id):
        self._browser.find_by_id(element_id).first.click()
        return self

    def wait_until_element_is_present(self, element_id, time_to_wait=5, maximum_attempts=5):
        for i in xrange(0, maximum_attempts):
            elem = self._browser.find_by_id(element_id).first
            if elem is None:
                time.sleep(time_to_wait)
        return self

if __name__ == '__main__':
    try:
        first_name = "Henrique"
        last_name = u"Juguetón"
        url = "http://www.mercadopago.com.br"
        I = BaseConfig()

        I.visit_url(url).then()\
            .click_on_element("common-register").then()\
            .fill_data_on_field("signupFirstName", first_name).then()\
            .fill_data_on_field("signupLastName", last_name)
    except Exception, e:
        print("Error - %s" % e)
