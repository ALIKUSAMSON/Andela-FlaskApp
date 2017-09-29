import models

yummylists = {'dengima@gmail.com': ['dengima']} 
current_user_DB = []  


class User(object):
    """Initializes user object with the email argument"""

    def __init__(self, email):  
        self.email = email

    def create_user_DB(self, recipe):
        """Implements create user yummylist feature"""
        if recipe and recipe not in yummylists:
            if self.email in yummylists:
                if recipe not in yummylists[self.email]:
                    yummylists[self.email][recipe] = {}  
                else:
                    return False
            else:
                yummylists[self.email] = {}  
                yummylists[self.email][recipe] = {}  
            return yummylists
        else:
            return False

    def delete_DB(self, recipe):
        """Implements delete feature"""
        if recipe:  
            del yummylists[models.logged_in[0]][recipe]
            return yummylists
        else:
            return 'Cannot delete a yummylist with no name'


    def update_DB(self, recipe, new_recipe):
        """Implements the update yummylist feature"""
        if recipe and new_recipe:  
            yummylists[models.logged_in[0]][new_recipe] = yummylists[models.logged_in[0]].pop(recipe) 
            return yummylists

    def view_user_DB(self, email):
        user_DB = []
        if email in yummylists:
            for yummylist in yummylists[email]:
                user_DB.append(yummylist)
            global current_user_DB  
            current_user_DB = user_DB
            return user_DB
        else:
            yummylists[email] = {}
            current_user_DB = user_DB
            current_user_DB = user_DB
            return user_DB