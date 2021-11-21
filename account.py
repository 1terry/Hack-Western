from person import person 
from tinydb import TinyDB
from tinydb import Query
from tinydb.operations import delete

# We only need a single one of these json files.
db = TinyDB ('C:\WAT\db.json')

User = Query()

class account:

    def __init__(self):
        pass

    def add_user (self, new_user_name, new_password):
        if self.__check_user(new_user_name):
            db.insert ({'name': new_user_name, 'password': new_password})
            return 0
        else:
            return -1

    def __check_user (self, user_name):
        if (db.get (User.name == user_name)) == None:
            return None
        else:
            return (db.search (User.name == user_name))
    
    def change_password (self, user_name, new_password):
        if self.__check_user(user_name) != None:
            # We need to find the given item and change it  
            thing = db.get (User.name == user_name)
            thing.doc_id

            db.remove(thing.doc_id)
            db.insert ({'name': user_name, 'password': new_password})
            return 0
        else:
            return -1
    
    def delete_user (self, user_name):
        if self.__check_user (user_name) != -1:
            db.remove (self.__check_user(user_name))
            return 0
        else:
            return -1


def main():

    new_account = account()
    
    new_account.add_user ("wow", 12353)

    print (new_account.change_password ("wow", 39807324098))

if __name__ == "__main__":
    main()






    
