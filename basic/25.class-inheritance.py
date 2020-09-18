#base class
class user:
    def __init__(self, fname, lname):
        self.__fname = fname
        self.__lname = lname

    def get_full_name(self):
        return self.__fname + " " + self.__lname

    def login(self, username):
        print("Authentication sucessfull")

    def do_work(self):
        print(self.__fname + " is working")

#derived class
class superUser(user):
    def __init__(self, fname, lname, level):
        #call super class initializer
        user.__init__(self, fname, lname)

    def super_user_work(self):
        print("Doing some super work")
