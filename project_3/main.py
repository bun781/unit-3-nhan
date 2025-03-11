from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from database import DatabaseManager
from kivy_garden.mapview import MapMarker, MapLayer
from kivy.graphics import Color, Line
from math import radians, cos, sin, asin, sqrt
Window.size = (432, 936)
from kivy.metrics import dp
from datetime import datetime
from secure_password import generate_confirmation_string
from secure_password import check_hash
from secure_password import encrypt_password
import re

class LoginScreen(MDScreen):
    current_user = None
    current_user_id = None
    def try_login(self):
        username = self.ids.username.text
        password = self.ids.password.text
        query = f"SELECT * from users where username='{username}'"
        db = DatabaseManager(name="database.db")
        result = db.execute(query=query)
        if len(result) == 1:
            # user exist
            user_id, username, name, email_address, password_hash, address_list, is_employee, confirmation_hash = result[0]
            if check_hash(hashed_password=password_hash, user_password=password):
                if check_hash(confirmation_hash, generate_confirmation_string( user_id, username, name, email_address, password_hash, 'None', 0)):
                    LoginScreen.current_user = username
                    LoginScreen.current_user_id = db.execute(f"SELECT user_id FROM users WHERE username='{username}'")[0][0]

                    if is_employee == 1:
                        self.parent.current = "EmployeeDashboard"


                    else:
                        self.parent.current = "CustomerDashboard"


                else:
                    print("User data is incorrect, please contact support")
            else:
                print("Username or Password is incorrect")
        else:
            print("User does not exist")
        print("user tried to login")
        print(LoginScreen.current_user_id)
class RegistrationScreen(MDScreen):
    def try_register(self):
        username = self.ids.username.text
        email_address = self.ids.email.text
        name = self.ids.name.text
        password = self.ids.password.text
        repassword = self.ids.repassword.text

        # Checks and validation
        # 1 - Is Username and Email unique?
        check1_query = f"""SELECT * from users where
            username = '{username}' or email_address = '{email_address}'
            """

        db = DatabaseManager(name="database.db")
        results = db.execute(query=check1_query)
        if len(results) > 0:
            # username or email already used
            self.ids.username.error = True
            self.ids.username.helper_text = "Username or Email already in use"
            return

        # 2 - Check if password match
        if password != repassword:
            self.ids.password.error = True
            self.ids.password.helper_text = "Passwords do not match"
        else:
            # 3 get latest userid
            query = f"SELECT MAX(user_id) from users"
            user_id = db.execute(query=query)[0][0] + 1 # current user id

            encrypted_password = encrypt_password(password)
            confirmation_hash = encrypt_password(generate_confirmation_string(user_id, username, name, email_address, encrypted_password, 'None', 0))
            if len(password) * len(repassword) * len(username) * len(email_address) != 0:
                insert_query = f"""INSERT into users(username, name, email_address, password_hash, address_list, is_employee, confirmation_hash)
        values('{username}','{name}','{email_address}', '{encrypted_password}','None',0,'{confirmation_hash}')"""

                db.run_save(query=insert_query)


                self.parent.current = "LoginScreen"


from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.fitimage import FitImage
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField

class CustomerDashboard(MDScreen):
    order = []
    def on_pre_enter(self, *args):
        print(LoginScreen.current_user)
        if LoginScreen.current_user:
            self.ids.CustomerDashboard_title.text = f"Welcome {LoginScreen.current_user.title()}!"
            print(LoginScreen.current_user)
        self.ids.container.clear_widgets()  # Avoid duplication when re-entering
        db = DatabaseManager(name = "database.db")
        query = f'''select * from food_listing'''
        foods = db.execute(query=query)
        for food in foods:
            card = self.create_card(food)
            self.ids.container.add_widget(card)
        db.close()

    def place_order(self, food_id):
        db = DatabaseManager(name = "database.db")
        query = f'''
        SELECT * FROM food_listing
        WHERE food_id = {food_id}
        '''
        food = db.execute(query=query)
        CustomerDashboard.order.append(food)
        print(CustomerDashboard.order)
        self.ids.cart.text = f'View cart: {len(CustomerDashboard.order)} items, ¥{sum(float(re.sub(r"[^0-9.]", "", str(food[0][1]))) for food in CustomerDashboard.order):.2f}'
        print(CustomerDashboard.order)

    def create_card(self, food):
        card = MDCard(
            size_hint=(None, None),
            size=("350dp", "110dp"),
            radius=[30],
            elevation=2,
            pos_hint={"center_x": 0.5},
            on_release = lambda x: self.place_order(food[0])
        )

        layout = MDBoxLayout(
            orientation="horizontal",
            spacing="8dp",
            padding=("10dp", "5dp"),
            size_hint_y=None,
            height=card.height,
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        # Image container
        image_card = MDCard(
            size_hint=(None, None),
            size=("80dp", "80dp"),
            radius=[35],
            elevation=0,
            pos_hint={"center_y": 0.5}
        )

        # FitImage without invalid properties
        image = FitImage(
            source=f"{food[4]}",
            size_hint=(1, 1),
        )

        image_card.add_widget(image)


        right_section = MDBoxLayout(
            orientation="vertical",
            spacing="4dp",
            size_hint_y=None,
            adaptive_height=True,
            pos_hint={"center_y": 0.5}
        )

        title_label = MDLabel(
            text=f"{food[6]}",
            bold=True,
            font_style="H5",
            halign="left",
            size_hint_y=None,
            adaptive_height=True,
            font_size="18sp",
            valign="middle",
        )

        description_container = MDBoxLayout(
            orientation="horizontal",
            spacing="6dp",
            size_hint_y=None,
            adaptive_height=True
        )

        description_label = MDLabel(
            text=f"{food[2]}",
            theme_text_color="Hint",
            size_hint_y=None,
            adaptive_height=True,
            valign="middle",
        )

        price_label = MDLabel(
            text=f'¥{float(re.sub(r"[^0-9.]", "", str(food[1])))}',
            theme_text_color="Secondary",
            font_size="12sp",
            size_hint=(None, None),
            size=("60dp", "20dp"),
            valign="middle",
            halign="right",
        )


        # Add description and price to the container
        description_container.add_widget(description_label)
        description_container.add_widget(price_label)

        # Add elements to right section
        right_section.add_widget(title_label)
        right_section.add_widget(description_container)

        layout.add_widget(image_card)
        layout.add_widget(right_section)
        card.add_widget(layout)

        return card

class EmployeeTemplate(MDScreen):
    data_table = None
    dialog = None
    selected_row_index = None

    def __init__(self, name, column_data, row_query, id_name, screen_name, **kwargs):
        super().__init__(**kwargs)
        self.name_ = name
        self.screen_name = screen_name
        self.KV = '''
FitImage:
    source: "back.webp"
    allow_stretch: True
    keep_ratio: False
    '''
        #KV only allows 1 top level class per string
        self.KV_ = f'''
MDBoxLayout:
    id: screen_main
    orientation: 'vertical'
    BoxLayout:
        size_hint_y: None
        height: "56dp"
        padding: "10dp"
        spacing: "10dp"
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1  # Toolbar color
            Rectangle:
                size: self.size
                pos: self.pos

        # Burger Menu Button (Opens Dropdown)
        MDIconButton:
            icon: "menu" 
            size_hint_x: None
            width: "50dp"
            on_release: app.root.get_screen("{self.screen_name}").open_menu(self)
        MDLabel:
            id: label
            text: "{self.name_}"
            pos_hint: {{"center_y": 0.70}}
            font_size: "20sp"
            bold: True
            color: 0, 0, 0, 1  # White text

    Widget: '''
        self.load_kv() #
        self.column_data = column_data
        self.row_query = row_query
        self.id_name = id_name
        self.row_data = self.get_row_data()
        print(f'row data is {self.row_data}')
        self.create_data_table()

    def load_kv(self):
        if self.KV:
            self.add_widget(Builder.load_string(self.KV))
            self.add_widget(Builder.load_string(self.KV_))

    def open_menu(self, button):
        print(button)
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "Dashboard",
                "height": dp(56),
                "on_release": lambda: self.switch_screen("EmployeeDashboard"),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Orders",
                "height": dp(56),
                "on_release": lambda: self.switch_screen("EmployeeOrderArchive"),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Food",
                "height": dp(56),
                "on_release": lambda: self.switch_screen("EmployeeFoodListings"),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Restaurants",
                "height": dp(56),
                "on_release": lambda: self.switch_screen("EmployeeRestaurantList"),
            },
        ]


        self.menu = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=4
        )
        self.menu.open()
    def switch_screen(self, screen_name):
        app = MDApp.get_running_app()
        app.root.current = screen_name  # Switches to the correct screen
        self.menu.dismiss() # Close the dropdown

    def get_row_data(self):
        db = DatabaseManager('database.db')
        row_data = db.execute(self.row_query)
        print(len(row_data))
        db.close()
        return row_data

    def create_data_table(self):
        self.table_box = MDBoxLayout(orientation="vertical", size_hint_y=0.7, pos_hint={"center_y": 0.5}, spacing=10)
        if self.data_table:
            self.remove_widget(self.data_table)

        self.data_table = MDDataTable(
            size_hint=(0.9, 0.8),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            column_data=self.column_data,
            use_pagination=True,
            row_data=self.row_data,
            rows_num=10
        )

        self.data_table.bind(on_row_press=self.on_row_press) # apparently the correct way to bind
        self.table_box.add_widget(self.data_table)
        self.table_box.add_widget(MDRaisedButton(text="Add new row", pos_hint={"center_x": 0.2, "center_y": 0.5}, on_release=self.show_add_dialog))
        self.add_widget(self.table_box)

    def on_row_press(self, instance_table, instance_row):
        row_text = instance_row.text  # Get text from clicked row
        print(f'row {row_text}')
        print(f'data {self.row_data}')
        for i, row in enumerate(self.row_data):
            print(row)
            for j in range(len(row)):
                if str(row_text) == str(row[j]):
                    self.selected_row_index = i
                break
            else:
                print("no")
        self.show_edit_dialog()

    def show_add_dialog(self, not_needed_data):
        self.dialog_content_add = MDBoxLayout(orientation="vertical", spacing=10, size_hint_y=None, height=600)
        self.text_fields_add = []
        for i, column in enumerate(self.column_data[:-1]): # id is wexcluded
            text_field = MDTextField(hint_text=f"{column[0]}")
            self.text_fields_add.append(text_field)
            self.dialog_content_add.add_widget(text_field)
        self.dialog_add = MDDialog(
            type="custom",
            content_cls=self.dialog_content_add,
            buttons=[
                MDRaisedButton(text="Save", on_release=self.add_row),
                MDRaisedButton(text="Cancel", on_release=lambda x: self.dialog_add.dismiss()),
            ],
        )
        self.dialog_add.open()
    def add_row(self, not_needed_data):
        db = DatabaseManager('database.db')
        query = f'SELECT MAX({self.id_name}) from {self.name_}'
        current_id = db.execute(query)[0][0]
        values = list(text_field.text for text_field in self.text_fields_add)
        values.append(current_id+1)
        self.row_data.append(values)
        self.create_data_table()

        query = f'insert into {self.name_}('
        for i in range(len(self.column_data)-1):
            query += f'{self.column_data[i][0]},'
        query = query[:-1] +') values ('
        for i in range(len(values)-1):
            query += f'"{values[i]}",'
        query = query[:-1] + ');'
        db.run_save(query)
        db.close()
        self.dialog_add.dismiss()
        MDDialog(title="Item successfully added!").open()


    def show_edit_dialog(self):
        self.dialog_content = MDBoxLayout(orientation="vertical", spacing=10, size_hint_y=None, height=600)
        self.text_fields = []
        self.row_values = self.row_data[self.selected_row_index]  # Get selected row values
        for i, column in enumerate(self.column_data[:-1]): # id is excluded
            text = str(self.row_values[i]) # # make sure eveyrthing is a stirng
            text_field = MDTextField(hint_text=f"{column[0]}", text=text)
            self.text_fields.append(text_field)
            self.dialog_content.add_widget(text_field)
        self.dialog = MDDialog(
            type="custom",
            content_cls=self.dialog_content,
            buttons=[
                MDRaisedButton(text="Save", on_release=self.save_data),
                MDRaisedButton(text="Cancel", on_release=lambda x: self.dialog.dismiss()),
            ],
        )
        self.dialog.open()
    def save_data(self, a): # extra argument because on_release gives 2?
        db = DatabaseManager('database.db')
        new_values = list(text_field.text for text_field in self.text_fields)
        new_values.append(self.row_values[-1]) #add the id back
        self.row_data[self.selected_row_index] = new_values
        self.create_data_table()
        query = f'''
        update {self.name_}
        set
        '''
        for column, data in zip(self.column_data, new_values): #looks easier on the eye unpacking the values this way
            column = column[0]
            query += f' {column} = "{data}",'
        query = query[:-1]
        query += f' where {self.id_name} = {self.row_values[-1]}'
        print(query)
        db.run_save(query)
        db.close()

        self.dialog.dismiss()
class EmployeeDashboard(MDScreen):
    pass
class EmployeeOrderArchive(EmployeeTemplate):
    def __init__(self, **kwargs):
        kwargs["name"] = "order_list"
        kwargs["screen_name"] = "EmployeeOrderArchive"
        kwargs["column_data"] = [
            ("order_id", dp(20)),
            ("receipt_id", dp(20)),
            ("food_id", dp(20)),
            ("order_date", dp(20)),
            ("status", dp(20)),
            ("order_id", dp(20))
        ]
        kwargs["row_query"] = '''select order_id, receipt_id, food_id, order_date, status, order_id from order_list'''
        kwargs["id_name"] = "order_id"
        super().__init__(**kwargs)
class EmployeeFoodListings(EmployeeTemplate):
    def __init__(self, **kwargs):
        kwargs["name"] = "food_listing"
        kwargs["screen_name"] = "EmployeeFoodListings"
        kwargs["column_data"] = [
            ("food_name", dp(40)),
            ("description", dp(60)),
            ("cost", dp(20)),
            ("image", dp(20)),
            ("user_id", dp(22)),
            ("food_id", dp(20))
        ]
        kwargs["row_query"] = '''select food_name, description, cost, image, user_id, food_id from food_listing'''
        kwargs["id_name"] = "food_id"
        super().__init__(**kwargs)
class EmployeeRestaurantList(EmployeeTemplate):
    def __init__(self, **kwargs):
        kwargs["name"] = "restaurant"
        kwargs["screen_name"] = "EmployeeRestaurantList"
        kwargs["column_data"] = [
            ("name", dp(50)),
            ("location", dp(50)),
            ("restaurant_id", dp(40)),
        ]
        kwargs["row_query"] = '''select name, location, restaurant_id from restaurant'''
        kwargs["id_name"] = "restaurant_id"
        super().__init__(**kwargs)
class LineLayer(MapLayer):
    def __init__(self, point_a, point_b, **kwargs):
        super().__init__(**kwargs)
        self.point_a = point_a
        self.point_b = point_b
    def reposition(self):
        self.canvas.clear()
        mapview = self.parent
        if not mapview:
            return
        with self.canvas:
            Color(1, 0, 0, 1)  # Red color line
            x1, y1 = mapview.get_window_xy_from(lat=self.point_a[0], lon=self.point_a[1], zoom=mapview.zoom)
            x2, y2 = mapview.get_window_xy_from(lat=self.point_b[0], lon=self.point_b[1], zoom=mapview.zoom)
            Line(points=[x1, y1, x2, y2], width=4)  # Increased line thickness


from kivymd.uix.button import MDIconButton
from kivymd.uix.dialog import MDDialog

class CustomerOrder(MDScreen):
    def add_marker(self, instance, touch):
        print(instance)
        print(touch)
        if instance.collide_point(*touch.pos):
            map_view = self.ids.map_view

            # Convert touch pos to map-relative pos
            rel_x = touch.x - map_view.pos[0]
            rel_y = touch.y - map_view.pos[1]

            lat, lon = map_view.get_latlon_at(rel_x, rel_y)
            self.lat = lat
            self.lon = lon

            print(f"Touch at {touch.pos}, converted to map lat/lon: {lat}, {lon}")

            if self.current_marker: # remove marker if it already exists
                map_view.remove_widget(self.current_marker)
            self.current_marker = MapMarker(lat=lat, lon=lon)
            map_view.add_widget(self.current_marker)

            if self.current_marker:
                map_view.remove_widget(self.current_marker)
            if self.current_line:
                map_view.remove_widget(self.current_line)

            self.current_marker = MapMarker(lat=lat, lon=lon)
            map_view.add_widget(self.current_marker)

            self.closest_point = []

            for i in range(len(self.restaurants)):
                print(self.closest_point)
                lat_r, lon_r = self.restaurants[i][2].split(";")
                lon_r = float(lon_r)
                lat_r = float(lat_r)
                n = self.haversine(lon, lat, lon_r, lat_r)
                if not self.closest_point:
                    self.closest_point = [n, self.restaurants[i][1], (lat_r, lon_r)]
                elif n < self.closest_point[0]:
                    self.closest_point = [n, self.restaurants[i][1], (lat_r, lon_r)]
            self.draw_path(lat, lon,self.closest_point[2])

            self.ids.map_view_closest_store.text = f'{self.closest_point[0]:.2f}Km away, closest to {self.closest_point[1]}'
    def draw_path(self, lat, lon, closest_point):
        map_view = self.ids.map_view
        self.current_line = LineLayer(point_a=(lat, lon), point_b=closest_point)
        map_view.add_widget(self.current_line)

    def haversine(self, lon1, lat1, lon2, lat2):
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371  # Radius of Earth in km
        return c * r

    def on_pre_enter(self, *args):
        self.ids.container.clear_widgets()  # Avoid duplication when re-entering
        self.current_marker = None
        self.current_line = None
        self.lat = None
        self.lon = None
        self.cards = []
        for food in CustomerDashboard.order:
            card = self.create_card(food)
            self.ids.container.add_widget(card)
            self.cards.append(card)

        db = DatabaseManager("database.db")
        query = "select * from restaurant"
        self.restaurants = db.execute(query)
        for restaurant in self.restaurants:
            lat, lon = restaurant[2].split(";")
            self.ids.map_view.add_widget(MapMarker(lat=lat, lon=lon))


    def create_card(self, food):
        food_info = food[0]
        card = MDCard(
            size_hint=(None, None),
            size=("350dp", "110dp"),
            radius=[30],
            elevation=2,
            pos_hint={"center_x": 0.5},

        )

        layout = MDBoxLayout(
            orientation="horizontal",
            spacing="8dp",
            padding=("10dp", "5dp"),
            size_hint_y=None,
            height=card.height,
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        # Image container
        image_card = MDCard(
            size_hint=(None, None),
            size=("80dp", "80dp"),
            radius=[35],
            elevation=0,
            pos_hint={"center_y": 0.5}
        )

        image = FitImage(
            source=f"{food_info[4]}",
            size_hint=(1, 1),
        )

        image_card.add_widget(image)

        # Right section (Text)
        right_section = MDBoxLayout(
            orientation="vertical",
            spacing="4dp",  # Slightly more space
            size_hint_y=None,
            adaptive_height=True,
            pos_hint={"center_y": 0.5}
        )

        title_label = MDLabel(
            text=f"{food_info[6]}",
            bold=True,
            font_style="H5",
            halign="left",
            size_hint_y=None,
            adaptive_height=True,
            font_size="18sp",
            valign="middle",
        )

        title_container = MDBoxLayout(
            orientation="horizontal",
            spacing="8dp",
            size_hint_y=None,
            adaptive_height=True
        )

        icon_button = MDIconButton(
            icon="minus",
            theme_text_color="Secondary",
            font_size="18sp",
            size_hint=(None, None),
            size=("30dp", "30dp"),
            md_bg_color=(0.9, 0.9, 0.9, 1),  # Light gray background
            on_release = lambda x: self.remove_order(food, card)
        )

        # Description and price in one line
        description_container = MDBoxLayout(
            orientation="horizontal",
            spacing="6dp",
            size_hint_y=None,
            adaptive_height=True
        )

        description_label = MDLabel(
            text=f"{food_info[2]}",
            theme_text_color="Hint",
            size_hint_y=None,
            adaptive_height=True,
            valign="middle",
        )

        price_label = MDLabel(
            text=f"¥{food_info[1]}",
            theme_text_color="Secondary",
            font_size="12sp",
            size_hint=(None, None),
            size=("60dp", "20dp"),
            valign="middle",
            halign="right",
        )

        title_container.add_widget(title_label)
        title_container.add_widget(icon_button)
        # Add description and price to the container
        description_container.add_widget(description_label)
        description_container.add_widget(price_label)

        # Add elements to right section
        right_section.add_widget(title_container)
        right_section.add_widget(description_container)

        layout.add_widget(image_card)
        layout.add_widget(right_section)
        card.add_widget(layout)

        return card

    def place_order(self):
        db = DatabaseManager("database.db")
        receipt_id = db.execute("SELECT receipt_id FROM order_list ORDER BY order_id DESC LIMIT 1")# fetch the last inserted value
        if not receipt_id:
            receipt_id = '1'
        else:
            receipt_id = receipt_id[0][0] + 1
        print(receipt_id)
        user_id = LoginScreen.current_user_id

        print(user_id)
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # for sqlite
        if self.lat and self.lon:
            for order in CustomerDashboard.order:
                food_id_ = order[0][0]
                query = f'''
                INSERT INTO order_list(user_id, status, order_date, food_id, receipt_id, location)
                VALUES({user_id}, 'Preparing', {food_id_}, DATETIME('{now}'),{receipt_id}, "{self.lat};{self.lon}")
                '''
                db.run_save(query=query)

            CustomerDashboard.order = []
            self.parent.current = "CustomerDashboard"
            MDDialog(title="Order successfully placed!").open()

            # get screen named customerdashboard, get the id cart, change the text in that id to view cart :)
            self.manager.get_screen("CustomerDashboard").ids.cart.text = "View Cart"
        else:
            MDDialog(title="Please select your location",).open()



    def remove_order(self, food, card):
        print(CustomerDashboard.order)
        CustomerDashboard.order.remove(food)
        self.ids.container.remove_widget(card)
        print('```')
        print(CustomerDashboard.order)

class main(MDApp):
    def build(self):
        pass

t = main()
t.run()
