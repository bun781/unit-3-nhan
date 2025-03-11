[^6]: KivyMD. (n.d.-b). Welcome to KivyMD’s documentation! — KivyMD 0.104.2.dev0 documentation. Kivymd.readthedocs.io. https://kivymd.readthedocs.io/en/latest/
# Criterion C: Development

## Success Criteria 4 & 5: Inheriting template classes to allow user-friendly access to the database.
As stated in the proposed solution, data about user orders, food listings, and restaurants are stored in an SQLite database. Additionally, success critera 4 & 5 requires that employee accounts can modify customer orders, in addition to modify information about food listings and retaurants. Therefore, to complete these two success criteria, the software needs to provide a way for the users to edit the database via its graphic interface.

Firstly, to view the data, the kivyMD framework provides a table widget through the MDDataTable class. When initialized, this class requires a list containing the column name as well as another list containing the data of each row, which can be retrieved from the database. The code belows shows the initialization of the data table in the software.

```.py
self.data_table = MDDataTable(
    column_data = self.column_data, # self.column_data is a list of column name, should be written in manually by the developer, as not every column stored in the database, such as confirmation hashes or id need or should be displayed.
    row_data = self.row_data, # self.row_data is a list of row data, retrieved via a query to the application's database

    # formatting code that does not depend on information inserted
    size_hint = (0.9, 0.8),
    pos_hint = {"center_x": 0.5, "center_y": 0.5},
    use_pagination = True, # data is cleanly divided into pages
    rows_num = 10  # show 10 rows per page
)
```

This is great way to display the database information because the code for the graphic widget is independent of the table data, meaning that each data table that the employee need access to (orders, food listing, and restaurants), can easily be deployed through changing the column name list, `self.column_data`, and the row data list, `self.row_data`. 

Constructing the tables through this method not only allows for the current tables to have a consistent style, it also allows developers to easily add additional tables by simply changing the column and row data, while also maintaining consistency in design.

`self.row_data` can be retrieved directly from the SQLite database through the `get_row_data` method, which queries the database on the row data.
```.py
    def get_row_data(self):
        db = DatabaseManager('database.db') # connect with the database
        row_data = db.execute(self.row_query) # self.row_query is inputted by the user
        db.close()
        return row_data
```

To keep the style consistent and limit the number of possible error points, the screens that display the data for employees can each be a class that inherits from a template class that allows them to display different data by having different values for keyword arguments upon initialization.

Inherited classes were used instead of class instances because kivyMD requires that each screen needs to be initialized by a python class of the same name [^6]. Therefore, an instance would possibly cause errors with kivyMD, and class that inherits from template were used instead.

```.py
class EmployeeRestaurantList(EmployeeTemplate):
    def __init__(self, **kwargs):
        kwargs["name"] = "restaurant" 
        kwargs["screen_name"] = "EmployeeRestaurantList"
        kwargs["column_data"] = [ # column names
            ("name", dp(50)), # tuple is in the format of (column name, column display width)
            ("location", dp(50)),
            ("restaurant_id", dp(40)),
        ]
        kwargs["row_query"] = '''select name, location, restaurant_id from restaurant''' # this query retrieves the data needed for the table

        kwargs["id_name"] = "restaurant_id" # define the column that contains the priary key to the database table
        super().__init__(**kwargs)
```

## Success criteria 3: Creating an interactive map that shows restaurants and allows user to select their location
```.kv
MapView:
    id: map_view
    size_hint: 1, 1
    pos_hint_x: 0.5

    #this is the center of the current restaurants, but future developers can 
    lat: 35.653798
    lon: 139.816640

    zoom: 8
    double_tap_zoom: False
    min_zoom: 10
    on_touch_down: root.add_marker(*args) # *args passes the information about the touch event
```

Kivy can generates a blank interactive map using the openstreetmap application programming interface (API) through the MapView class. The code above defines a map that is centered round `lat` latitude and `lon` longitude, and the `root.add_marker()` method will be called upon the map being touched.

This method again highlights the benefits of using kivy. Instead of manually requesting an API key from openstreetmap and creating the code necessary to display the map, kivy can do that with a short piece of code without the developer ever needing to directly communicate with openstreetmap.

```.py
def on_pre_enter(self, *args):
    self.ids.container.clear_widgets()  # clear map if the user already placed their order once and needs to come back to the screen

    db = DatabaseManager("database.db") # connect with the database
    query = "select * from restaurant" # select every restaurant from restaurant
    self.restaurants = db.execute(query)
    db.close()

    for restaurant in self.restaurants:
        lat, lon = restaurant[2].split(";") # retrieve the latitude and longitude of the restaurant
        self.ids.map_view.add_widget(MapMarker(lat=lat, lon=lon)) # add a marker to the map at the coordinates retrieved
```

The code above shows that upon entering the screen that has the map, the program will retrieve the position of each restaurant from the database and create a corresponding MapMarker object on the map.

To save space on the database by having less columns and data points, the coordinate of the restaurants are stored togther in one column in the form of "latitude;longitude". Once retrieve from the database, this information will be split into the `lat` and `lon` variable through the built-in `split()` method for python strings to be used to generat the map marker for the restaurant.

```.py
    def add_marker(self, instance, touch):
        if instance.collide_point(*touch.pos): # if the touch is within the map

        # creating the map marker
            map_view = self.ids.map_view

            # touch is the position where the screen was touched, map_view.pos is where the map is placed within the screen
            rel_x = touch.x - map_view.pos[0] 
            rel_y = touch.y - map_view.pos[1]

            # convert the screen coordinate to map coordinate
            lat, lon = map_view.get_latlon_at(rel_x, rel_y)
            self.lat = lat
            self.lon = lon

            # remove marker and line if it already exists, as one order cannot be delivered to two separate locations
            if self.current_marker: 
                map_view.remove_widget(self.current_marker)
            if self.current_line:
                map_view.remove_widget(self.current_line)

            # create the map marker object and add it to the map
            self.current_marker = MapMarker(lat=lat, lon=lon)
            map_view.add_widget(self.current_marker)

        # finding the closest restaurant
            self.closest_point = []
            for i in range(len(self.restaurants)): # for every restaurant

                # retrieve the latitude and longitude of the restaurants and convert them from strings to floats
                lat_r, lon_r = self.restaurants[i][2].split(";") 
                lon_r = float(lon_r)
                lat_r = float(lat_r)

                # find the closest restaurant to the user's location
                n = self.haversine(lon, lat, lon_r, lat_r) # use the haversine formula because the earth is not flat.

                if not self.closest_point: # set the current restaurant as the closest one if there is nothing in the closest_point list yet
                    self.closest_point = [n, self.restaurants[i][1], (lat_r, lon_r)]
                elif n < self.closest_point[0]: # first index of self.closest_point is the distance
                    self.closest_point = [n, self.restaurants[i][1], (lat_r, lon_r)]

            # after the loop, the restaurant that is closest to the marker remains in the self.closest_point list. Draw line to that point
            self.draw_path(lat, lon,self.closest_point[2])

            self.ids.map_view_closest_store.text = f'{self.closest_point[0]:.2f}Km away, closest to {self.closest_point[1]}'
```

The code above describes the `add_marker()` method, which is called when a user's touch is recorded on the map. It adjust coordinate of the user's touch event based on the position of the map on the screen in order to accurate change it into the correct map coordinate.

As one order cannot go to multiple location, the code uses simple if statement to check whether or not a marker already exists and removes it; a basic statement that minimizes any unexpected behaviour.

For a similar reason, a basic for loop that loops through the list of restaurants allows the code to find the closest restaurant to the marker in linear time. Attempting to minimize unexpected bahaviour like these two example is important because kivyMD is a framework that has a high level of abstraction, making it difficult and impractical for developers to account for every possible behaviour of the framework. Therefore, keeping the code's logic simple is important.

Additionally, code separation is important for the ease of further expansion of the program. The line drawn between the customer's location and the closest restaurant is in its separate class, it is a MapLayer class that specifically create a line on the map. By separating it into its own class, if the method that creates this class successfully executes but the line does not show up, the develop will know that it is a problem with their kivyMD code, not the program's logic, aiding in debugging.

```.py
class LineLayer(MapLayer):
    def __init__(self, point_a, point_b, **kwargs):
        super().__init__(**kwargs)
        self.point_a = point_a
        self.point_b = point_b
    def draw_line(self):
        self.canvas.clear()
        mapview = self.parent
        if not mapview:
            return
        with self.canvas:
            Color(1, 0, 0, 1)
            x1, y1 = mapview.get_window_xy_from(lat=self.point_a[0], lon=self.point_a[1], zoom=mapview.zoom)
            x2, y2 = mapview.get_window_xy_from(lat=self.point_b[0], lon=self.point_b[1], zoom=mapview.zoom)
            Line(points=[x1, y1, x2, y2], width=4)  # Increased line thickness
```

## Food card
```.py
def on_pre_enter(self, *args):
    db = DatabaseManager(name = "database.db") # connect with the database
    query = f'''select * from food_listing'''
    foods = db.execute(query=query) # retrieve food listings from the database
    db.close() # close the connection with the database to save resources

    for food in foods: # create a card for each food
        card = self.create_card(food)
        self.ids.container.add_widget(card)
```

The code above shows how the program creates cards for food listing by querying the database on the information about every food listing and make a card for each of the retrieved food listings using the `self.create_card()` method. The code below shows how such cards are created. The method `food` argument is a list that contains information about each food listing. Generating food cards based on the information stored in the database, as opposed to storing it in the code itself, allows for information of each food card to consistently update with the employee account's modification to the food data.

```.py
    def create_card(self, food:list):
        card = MDCard( # creates a main MDCard to nest everything in
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
        image_card = MDCard( # image of the food
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

        title_label = MDLabel( # name of the food
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

        description_label = MDLabel( # description of the food
            text=f"{food[2]}",
            theme_text_color="Hint",
            size_hint_y=None,
            adaptive_height=True,
            valign="middle",
        )

        price_label = MDLabel( # price of the food
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
```

A limitation of SQLite is that even if the type of data stored in a cell is declared, users can still insert values that are not of that data type. This is extremely detrimental when strings are inserted into values that are expected to be float, such as the price of a food listing. For the price of the food listing, the statement `float(re.sub(r"[^0-9.]", "", str(food[1])))` was used to make sure that the information is a float. If the user mistakenly enter '12e3.5t' as the price, then the statement would correct it to '123.5'. the `re.sub()` method replaces any character that is not in `0123456789.` with an empty string, removing any non-numerical character in `str(food[1])`, allowing it to be safely converted back to a float again. Converting `food[1]`, where the price is stored, to a string is necessary because the `re.sub()` takes string as an argument.

The reason why the check is implemented in the code while executing instead of when the data is entered is because if the software were to expand in the future, there are no guarantees that the developer would add a filter in data input, nor the effectiveness of that filter. Therefore, to prevent the code logic from breaking from receving the wrong data type, a filter must exist when the code is executing.

The code below shows another instance of how the check is added to convert from strings to floats that are suitable as an argument to the `place_order()` method.
```.py
    def place_order(self, food_id):
        db = DatabaseManager(name = "database.db")
        query = f'''
        SELECT * FROM food_listing
        WHERE food_id = {food_id}
        '''
        food = db.execute(query=query)
        db.close()

        CustomerDashboard.order.append(food)
        self.ids.cart.text = f'View cart: {len(CustomerDashboard.order)} items, ¥{sum(float(re.sub(r"[^0-9.]", "", str(food[0][1]))) for food in CustomerDashboard.order):.2f}'
```
