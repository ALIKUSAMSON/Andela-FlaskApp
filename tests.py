import unittest
from flask_testing import TestCase
from app_run import *

class FlaskTesTCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/home',content_type="html/text")
        self.assertEqual(response.status_code,200)

    ''' def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login')
        self.assertIn(b"Please login",response>data)'''

    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login',content_type="html/text")
        self.assertEqual(response.status_code,200)

    def test_signup(self):
        tester = app.test_client(self)
        response = tester.get('/signup',content_type="html/text")
        self.assertEqual(response.status_code,200)

    def test_dashboard(self):
        tester = app.test_client(self)
        response = tester.get('/dashbord',content_type="html/text")
        self.assertEqual(response.status_code,200)

if __name__ == '__main__':
    unittest.main()






