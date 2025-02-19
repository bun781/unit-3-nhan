from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from database import DatabaseManager
Window.size = (432, 936)

from secure_password import check_hash
from secure_password import encrypt_password

class LoginScreen(MDScreen):
    current_user = None
    def try_login(self):
        username = self.ids.username.text
        password = self.ids.password.text
        query = f"SELECT * from users where username='{username}'"
        db = DatabaseManager(name="database.db")
        result = db.execute(query=query)
        if len(result) == 1:
            # user exist
            hash_column = 4
            is_employee = 6
            hash = result[0][hash_column]
            if check_hash(hashed_password=hash, user_password=password):
                if is_employee == 1:
                    self.parent.current = "EmployeeDashboard"
                else:
                    self.parent.current = "CustomerDashboard"
            else:
                print("Username or Password is incorrect")
            print(result)
        else:
            print("User does not exist")
        print("user tried to login")

class RegistrationScreen(MDScreen):
    def try_register(self):
        username = self.ids.username.text
        email = self.ids.email.text
        name = self.ids.name.text
        password = self.ids.password.text
        repassword = self.ids.repassword.text

        # Checks and validation
        # 1 - Is Username and Email unique?
        check1_query = f"""SELECT * from users where
            username = '{username}' or email_address = '{email}'
            """

        db = DatabaseManager(name="database.db")
        results = db.execute(query=check1_query)
        if len(results) > 0:
            # username or email already used
            self.ids.username.error = True
            self.ids.username.helper_text = "Username or Email already in use"
            return

        # 2 - CHeck if password match
        print(password, repassword)
        if password != repassword:
            self.ids.password.error = True
            self.ids.password.helper_text = "Passwords do not match"

        if len(password) * len(repassword) * len(username) * len(email) != 0:
            insert_query = f"""INSERT into users(username, name, email_address, password_hash, is_employee)
    values('{username}','{name}','{email}','{encrypt_password(password)}',0)"""
            db.run_save(query=insert_query)

            LoginScreen.current_user = username
            self.parent.current = "LoginScreen"

            print(encrypt_password(password), LoginScreen.current_user)


class CustomerDashboard(MDScreen):
    pass

class EmployeeDashboard(MDScreen):
    pass

class CustomerOrder(MDScreen):
    pass

class CustomerMap(MDScreen):
    pass

class CustomerOrderConfirmation(MDScreen):
    pass

class EmployeeOrderArchive(MDScreen):
    pass

class EmployeeFoodListings(MDScreen):
    pass

class EmployeeRestaurantList(MDScreen):
    pass

class main(MDApp):

    def build(self):
        pass

t = main()
t.run()
