class User:
    def __init__(self, name, login, password, database_main):
        self.__name = name
        self.__dbname = database_main
        self.__login = login
        self.__password = password
        self.__autorisatiion = False
        self.__state = False

    def get_name(self):
        return self.__name

    def getlogin(self):
        return self.__login

    def get_password(self):
        return self.__password

    def get_dbname(self):
        return self.__dbname

    def getautorization(self):
        return self.__autorisatiion

    def getState(self):
        return self.__state

    def set_state(self, state):
        self.__state = state
        if not state:
            print("You are logged out of your account!")
        else:
            print("Hello, " + self.__name)

    def set_autorization(self, state):
        self.__autorisatiion = state


class IUserManager(User):
    def login(self):
        if self.get_dbname().search_equals_login(self.getlogin()):
            print("A user with this username already exists")
            return False
        else:
            self.autorization()
            return True

    def sing_in(self):
        self.set_state(True)

    def sign_out(self):
        self.set_state(False)

    def autorization(self):
        print("Remember me? ('Yes' or 'No')")
        if Cheker():
            self.set_autorization(True)


class IUser_Repositiry():
    def __init__(self):
        self.__dbnameUsers = []

    def get_database_users(self):
        return self.__dbnameUsers

    def add_on_database(self, user):
        self.__dbnameUsers.append(user)

    def search_equals_login(self, login):
        for user in self.__dbnameUsers:
            if user.getlogin() == login:
                return True
        return False

    def search_user(self, login, password):
        for user in self.__dbnameUsers:
            if user.getlogin() == login:
                if user.get_password() == password:
                    if user.getautorization():
                        user.set_state(True)
                    else:
                        user.autorization()
                        user.set_state(True)
                    return user
        return None

    def get_by_login(self, login):
        for user in self.__dbnameUsers:
            if user.getlogin() == login:
                return user


def Cheker():
    while True:
        answer = str(input())
        if answer == "Yes":
            return True
        if answer == "No":
            return False
        else:
            print('Error')
            return False




if __name__ == '__main__':
    database_main = IUser_Repositiry()
    testuser = IUserManager("Nikita", "afterkita", "qwerty", database_main)
    testuser.set_autorization(True)
    database_main.add_on_database(testuser)

    main_cycle = True
    AdminFlag = False
    UserFlag = False

    while main_cycle:
        step = int(input('1 - admin\n2 - user\n3 - exit'))
        if step == 1:
            AdminFlag = True
        if step == 2:
            UserFlag = True
        if step == 3:
            main_cycle = False
        while AdminFlag:
            step = int(input('Admin panel:\n1 - Withdraw all users\n2 - Find a user by login\n3 - exit\n'))
            if step == 1:
                for i in range(len(database_main.get_database_users())):
                    print(f"{i+1}")
                    print(f" username - {database_main.get_database_users()[i].get_name()} \n login - {database_main.get_database_users()[i].getlogin()}\n password - {database_main.get_database_users()[i].get_password()} \n auth - {database_main.get_database_users()[i].getautorization()} \n state - {database_main.get_database_users()[i].getState()} \n ")

            if step == 2:
                login = str(input('Enter your username!'))
                user1 = database_main.get_by_login(login)
                if user1 is not None:
                    print(f" username - {user1.get_name()}\n login - {user1.getlogin()}\n password - {user1.get_password()} \n auth - {user1.getautorization()} \n state - {user1.getState()}")
                else:
                    print("There is no such user!")
            if step == 3:
                AdminFlag = False
        while UserFlag:
            step = int(input('User panel\n1 - Register\n2 - Enter\n3 - Back'))
            if step == 1:
                name = str(input('Enter your Name!'))
                login = str(input('Enter your Username!'))
                password = str(input('Enter your password!'))
                user = IUserManager(name, login, password, database_main)
                state = user.login()
                if state:
                    database_main.add_on_database(user)
            if step == 2:
                print("Are you logged in? ('Yes' or 'No')")
                if Cheker():
                    users = database_main.get_database_users()
                    mas_id = []
                    a = 0
                    for i in range(len(users)):
                        if users[i].getautorization():
                            mas_id.append(i)
                            print((a + 1), " - ", users[i].getlogin())
                            a += 1
                    step2 = int(input())
                    step2 -= 1
                    users[mas_id[step2]].sing_in()
                    while True:
                        print("1 - exit")
                        if int(input()) == 1:
                            users[mas_id[step2]].sign_out()
                            break
                else:
                    login = str(input('Enter your username!'))
                    password = str(input('Enter your password!'))
                    tempUser = database_main.search_user(login, password)
                    if tempUser is not None:
                        tempUser.sing_in()
                        while True:
                            print("1 - exit")
                            if int(input()) == 1:
                                tempUser.sign_out()
                                break
                    else:
                        print("Incorrectly entered username or password!")
            if step == 3:
                UserFlag = False