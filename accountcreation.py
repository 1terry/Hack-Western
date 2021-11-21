"""
This class is responsible for keeping a textfile database of users.

November 20, 2021 
- Created class
"""

# Shared text file name
database_name = "account.txt"

class accountcreation:

    # We don't need anything in the constructor 
    def __init__ (self):
        pass

    # Adding a user to the database
    def add_user (self, new_user, new_password):
        if (not(self.find_user (new_user))):
            f = open (database_name, "a+")

            f.write (new_user + "," + new_password)

            f.close()

            return 0
        
        else:
            return -1

       
    # Method used to find a given user
    def find_user (self, user_name):
        f = open (database_name, "r")
        a = True
        while a:
            file_line = f.readline()
            # We need to parse this line to determine if there a username of the same kind 
            new_line = file_line.split(",")
            if (new_line[0] == user_name):
                f.close()
                return True
            if not file_line:
                f.close()
                return False

    # Deleting a user
    def delete_user (self, user_name):
        if (self.find_user (user_name)):
            with open ("account.txt", "r") as f:
                lines = f.readlines()
            with open ("account.txt", "w") as f:
                for line in lines:
                    if ((line.strip("\n").split(","))[0]) != user_name:
                        f.write (line)
            f.close()
            return 0
        else:
            return -1

    # Changing the password for a user
    def change_password (self, user_name, new_password):
        if (self.find_user (user_name)):
            # We can delete the entry and make a new one
            self.delete_user (user_name)
            self.add_user (user_name, new_password)
            return 0
        else:
            return -1


