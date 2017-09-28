import models

yummylists = {'dengima@gmail.com': ['dengima']}  # dictionary stores all the yummylists and items for the signed users.
current_user_DB = []  # list that holds the current users yummylists


class User(object):
    """Initializes user object with the email argument"""

    def __init__(self, email):  # email belongs to the logged in user
        self.email = email

    def create_user_DB(self, recipe):
        """Implements create user yummylist feature"""
        if recipe and recipe not in yummylists:
            if self.email in yummylists:
                if recipe not in yummylists[self.email]:
                    yummylists[self.email][recipe] = {}  # creates empty dictionary in bucketlists with bucketlist name as key
                else:
                    return False
            else:
                yummylists[self.email] = {}  # creates empty dictionary in bucketlists dictionary with current user as key
                yummylists[self.email][recipe] = {}  # creates empty dictionary in current user dictionary with bucketlist name as key
            return yummylists
        else:
            return False

    def delete_DB(self, recipe):
        """Implements delete feature"""
        if recipe:  # makes sure the name field is not empty and
            del yummylists[models.logged_in[0]][recipe]
            return yummylists
        else:
            return 'Cannot delete a buckelist with no name'

    def update_DB(self, recipe, new_recipe):
        """Implements the update bucketlist feature"""
        if recipe and new_recipe:  # makes sure the name field is not empty and
            yummylists[models.logged_in[0]][new_recipe] = yummylists[models.logged_in[0]].pop(recipe) # updating a dict key
            return yummylists

    def view_user_DB(self, email):
        user_DB = []
        if email in yummylists:
            for yummylist in yummylists[email]:
                user_DB.append(yummylist)
            global current_user_DB  # to ensure that current_user_bucketlists can be manipulated in the scope
            current_user_DB = user_DB
            return user_DB
        else:
            yummylists[email] = {}
            current_user_DB = user_DB
            # global current_user_bucketlists
            current_user_DB = user_DB
            return user_DB