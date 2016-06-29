# coding: utf-8
import unittest
import os.path
import json
import sys
import os
sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path
from functional_tests.admin_data import AdminData



class AdminTest(unittest.TestCase):

    def setUp(self):
        json_file = open('../../admin_data.json', 'r').read()
        navigation_file = open(
            os.path.dirname(__file__) + '../../config_admin.json', 'r').read()
        self.config = json.loads(json_file)
        self.navigation_data = json.loads(navigation_file)
        self.browser = AdminData()
        print("rodoooooou")
        self.browser.visit_url('http://5b750f26.ngrok.io/octeste/admin/')
        for field in self.navigation_data['admin']['login_data']['fields']:
            self.browser.fill_data_on_field(
                field['field_name'], field['field_value'])

        self.browser.click_on_element("botao_login").wait(5)
        self.token = self.browser.url.split("token").split("=")[-1]
        self.browser.visit_url(
            "http://5b750f26.ngrok.io/octeste/admin/index.php?route=payment/mp_transparente&token=%s" % self.token)

    def test_must_load_payment_methods(self):
        pass

    def test_must_save_admin_data(self):
        pass

    def test_must_reload_payment_methods_according_to_country(self):
        pass

if __name__ == '__main__':
    unittest.main()
