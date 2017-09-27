import unittest
import context
from models import YummyRecipeApp
# users = {'xr': ['X', '1920', 'asd']} The user dictionary is initialized with this value

class UserModelTest(unittest.TestCase):

    def test_yummyrecipeApp_Instance(self): #this test ensures that the object is always properly initialized
        user = YummyRecipeApp('dengima@gmail.com', 'abc', 'sd')
        self.assertIsInstance(user, YummyRecipeApp, msg='object missing parameters')

    def test_signup_user_added_to_user_dictionary(self):#user dictionary exists in app.models file
        user = YummyRecipeApp('dengima@gmail.com','Lorna', 'abc')
        self.assertEqual({'xr': ['X', 'asd'], 'dengima@gmail.com': ['Lorna', 'abc']}, user.signup())

    def test_return_error_msg_if_user_exists_and_should_not_be_added_to_user_dictionary_again(self):
        user = YummyRecipeApp('xr', 'asd')
        self.assertEqual(user.signup(), 'User already exists')

    def test_empty_users_should_not_be_added_to_user_dictionary(self):
        user = YummyRecipeApp('', '')
        self.assertEqual(user.signup(), 'No user name given')

    def test_attempt_to_login_only_existing_users(self):
        user = YummyRecipeApp('xx', 'asd')
        self.assertEqual(user.login(), 'Unknown user')

    def test_add_users_to_logged_in_list_if_correct_password(self):
        user = YummyRecipeApp('xr', 'asd')
        self.assertEqual(user.login(), 'Logged in')

    def test_wrong_password_on_logged_in(self):
        user = YummyRecipeApp('xr', 'asdd')
        self.assertEqual(user.login(), 'Incorrect password')

if __name__=='__main__':
    unittest.main()