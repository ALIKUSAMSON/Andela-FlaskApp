import unittest
import context
from yummymodel import User, yummylists, models

class YummyModelTest(unittest.TestCase):
    def setUp(self):
        """Initialisation before each test """
        self.user = User('dengima@gmail.com')
        self.yummmylists = yummylists

    def test_user_Instance(self): #this test ensures that the object is always properly initialized
        self.assertIsInstance(self.user, User, msg='object missing parameters')

    def test_bucketlist_is_added_to_bucketlists_dictionary_and_can_be_deleted(self): # test ensures that bucketlist is added
        models.logged_in = ['dengima@gmail.com']
        self.assertEqual({'dengima@gmail.com': {'avs':{},'deng':['dengima']}},self.user.create_user_DB("avs"))
        self.assertEqual({'dengima@gmail.com':{'deng': ['dengima']}},self.user.delete_DB('avs'))

     
    def test_return_false_if_bucketlist_to_be_added_is_empty(self):
        self.assertEqual(False, self.user.create_user_DB(''))
    #
    def test_return_false_if_bucketlist_to_be_added_exists(self):
        self.assertEqual(False, self.user.create_user_DB('dengima'))

    def test_delete_non_existent_bucketlist(self):
        models.logged_in = ['dengima@gmail.com']
        self.assertEqual('Cannot delete a buckelist with no name', self.user.delete_DB(''))


if __name__=='__main__':
    unittest.main()