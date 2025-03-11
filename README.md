[^1]: Juviler, J. (2023, August 30). What Is GUI? Graphical User Interfaces, Explained. Hubspot. https://blog.hubspot.com/website/what-is-gui
[^2]: GeeksforGeeks. (2017, October 23). Python Language Advantages and Applications - GeeksforGeeks. GeeksforGeeks. https://www.geeksforgeeks.org/python-language-advantages-applications/
[^3]: KivyMD. (n.d.-b). Welcome to KivyMD’s documentation! — KivyMD 0.104.2.dev0 documentation. Kivymd.readthedocs.io. https://kivymd.readthedocs.io/en/latest/
[^4]: IBM. (2021, October 20). Relational Databases. Ibm.com. https://www.ibm.com/think/topics/relational-databases
[^5]: SQLite. (2024, December 7). SQLite Home Page. Www.sqlite.org. https://www.sqlite.org/

# Criterion A: Planning
## Problem Definition
My client is an old local restaurateur with a chain of restaurants around the city. Lately, he noticed that the number of customers visiting his restaurants are decreasing since online food ordering and delivering services are on the rise. My client wants to be able to update his service so that the restaurant can compete with these platforms. The restaurant currently only has food delivery via orders done through the phone, but my client said that they refrain from doing so because it provides no written record of the orders. He also said that it generally hurts the relationship between the restaurants and customers because there is nothing recording the order. Furthermore, he said that these disagreements usually start because customers do not know what the dishes look like, nor which ingredients were in it. And as users usually underestimate the cost of delivery to their location, they usually disagree at the food delivery fees. The problem also expands to staff’s reliability in pricing through phones, as they might read the wrong price. He said that whether or not it is accidentally or deliberately, a situation like such should never happen. My client said that most importantly, the restaurant can’t keep track of who is making the calls. He said that the restaurant chain prides on having the best customer service program. Lastly, he requested that the solution should accommodate for his ever expanding restaurant network and food listings.

## Proposed Solution
I propose an application that has a graphic user interface (GUI)[^1] allowing users to order their food without the compromises of ordering through phone calls; meaning that the restaurant can reliably keep track of the orders, and users can order food knowing exactly what they ordered and where to deliver to. Additionally, it also allows the restaurants employee to edit food listing and restaurant informations to accomodate for the expanding restaurant network.

Python is an interpreted language that is compatible with both Intel x86 and ARM across multiple operating systems[^2]. This in addition to Python robust community support and wide range of available libraries allows it to be a great choice for efficiently creating applications that work across multiple platforms.

The graphic framework Kivy and the extension KivyMD will be used to create the GUI for the application. One reason was because Kivy allows responsive design, an important feature when customer’s devices can have varying aspect ratios[^3]. Another reason was that KivyMD has Kivy elements that follows Google’s Material Design language, allowing it to appear native and professional[^3]. Moreover, Kivy and KivyMD were specifically designed to be implemented with Python, making the development more efficient, streamlined, and minimize unexpected behaviour.

The data storage solution will use SQLite. Relational database tools like SQL are preferred over simple storage options such as CSV or JSON files[^4], as data stored is relatively complex and interrelated. SQLite was selected because it is lightweight and embedded, allowing users to quickly access data even when not having stable connections[^5]. It also does not require a lot of storage nor a dedicated server, resources that are excessive for the application and require additional operating cost for my client.

## Success Criteria
1. The application has a login function both users and employees and a register function for users.
   
   **Quote from problem defintion:** "My client said that most importantly, the restaurant can’t keep track of who is making the calls", "there is no one or nothing recording the order"
   
2. The application allows users to see every detail about food listing.
   
   **Quote from the problem definition:** "disagreements usually start because customers do not know what the dishes look like, nor which ingredients were in it"

3. The application allows users to select their location through a map
   
   **Quote from the problem definition:** "And as users usually underestimate the cost of delivery to their location, they usually disagree at the food delivery fees"
   
4. The application allows users to send their orders to a database which employees have access to.
   
    **Quote from the problem definition:** "it [order through phones] generally hurts the relationship between the restaurants and customers because there is no one or nothing recording the order"
   
5. The employee accounts can add or modify food listings to the software and restaurant locations to the map.
   
    **Quote from the problem definition:** "requested that the solution should accommodate for his ever expanding restaurant network and food listings"

# Criterion B: Design

## Test Plan
| Test Case | Procedure | Planned Outcome | Success Criteria |
|:----------|:----------|:----------------|:-----------------|
| 1 | 1. Run the program and enter `"a"` into `username` on log in screen, and `"a"` into `password`. <br> 2. Stop the program and rerun it. <br> 3. Run the program and register a new account. <br> 4. Use the credentials created in the previous step to log in. | - After the first step, the tester should see a screen with a menu that leads to order lists, food listings, and restaurant list. <br> - When the test ends, the tester is on the user screen with cards that display food listings. | 1 - The application has a login function both for users and employees and a register function for users. |
| 2 | 1. Run the program, log in or register then log in into the application. | - The tester can see every food listing organized into cards on the screen. | 2 - The application allows users to see every detail about food listings. |
| 3 | 1. Run the program, log in or register then log in into the application. <br> 2. Click on the items that the testers want to add to the order. <br> 3. Click the `View Cart` button at the bottom of the screen. <br> 4. Click `Confirm Order`. <br> 5. Dismiss the dialog. <br> 6. Select location on the map. <br> 7. Select a different location on the map. <br> 8. Click confirm order. | - After completing step 2, the tester should be moved into a screen with a map. <br> - After completing step 3, a dialog appears and states that the user needs to select their location. <br> - After completing step 8, a dialog appears and states that the order has been successfully placed. | 3 - The application allows users to select their location through a map. |
| 4 | 1. Complete test case 3. <br> 2. Stop the program. <br> 3. Run the program again and input `"a"` as username and `"a"` as password. <br> 4. Click on the button that says `Order archive`. | - The order placed by the tester appears in the table shown in the order archive screen. | 4 - The application allows users to send their orders to a database which employees have access to. |
| 5 | 1. Run the program and input `"a"` as username and `"a"` as password. <br> 2. Click the button that says `Restaurant list`. <br> 3. Click on any row, modify the data in the row. <br> 4. Stop the program. <br> 5. Run the program and input `"a"` as username and `"a"` as password. <br> 6. Click the button that says `Restaurant list`. <br> 7. Add a new restaurant via the `Add new` button. <br> 8. Stop the program. <br> 9. Run the program, log in or register then log in into the application. <br> 10. Choose a food item and click the `View Cart` button. | - After step 6, the tester will see that the row they modified retained its modification even after a program restart. <br> - After step 10, the tester will see that the new location they added appears on the map. | 5 - The employee accounts can add or modify food listings to the software and restaurant locations to the map. |

## Flow Diagrams
<img src="https://github.com/user-attachments/assets/c3a995d9-ebb6-4e24-9716-45f2199b7ee2" height="1000">

Flow diagram of the software's login method from the LoginScreen class that can differentiate between employees and customer

<img src="https://github.com/user-attachments/assets/4692d369-d84d-4853-a196-434c2446a2a6" height="1000">

Flow diagram of the software's method to add new items to any table of the database

<img src="https://github.com/user-attachments/assets/a6d1c5db-ae16-4a78-bc61-9c7e36876585" height="1000">

Flow diagram of the software's method that can send and store customer's order in the database

## System Diagram
![image](https://github.com/user-attachments/assets/1f43e789-cd90-4568-a37b-01b587f53489)

## ER Diagram
<img width="1164" alt="image" src="https://github.com/user-attachments/assets/5cc258b3-c666-4241-9d73-30e15d06a232" />


## UML Diagram
![image](https://github.com/user-attachments/assets/c92d6601-33cc-43bc-be9d-b80ee4ecbb55)

## Record of Tasks
| Task Number | Planned Action | Planned Outcome | Time Estimated | Target Completion Date | Criterion |
|-------------|---------------|-----------------|----------------|------------------------|-----------|
| 1  | First meeting with client | Have a clear problem definition | 10 minutes | Jan 30 | A |
| 2  | Draft proposed solution and present to client | Provide the client with an idea of a solution to their problem | 30 minutes | Feb 3 | A |
| 3  | Draft and propose success criteria to client | Provide the client with an idea of a solution to their problem | 30 minutes | Feb 3 | A |
| 4  | Modify the success criteria and proposed solution based on client's feedback | Have a proposed solution and success criteria that the client agrees with | 30 minutes | Feb 5 | A |
| 5  | Create wireframe diagrams for software's screen | Determine a clear user interface for the software | 1 hour 20 minutes | Feb 10 | B |
| 6  | Create ER diagram for database and create it in python | Have a clear idea of how data interact with code and each other | 1 hour 20 minutes | Feb 12 | B |
| 7  | Create a test plan | Have a clear view on what I need to test in order to fulfill the Success Criteria | 40 minutes | Feb 12 | B |
| 8  | Determine possible complex operations in the program | Ensure that the product gets delivered in time | 20 minutes | Feb 12 | B |
| 9  | Create an overview flowchart for complex operations in the program | Have a clear idea of how data tables interact with code and each other | 3 hours | Feb 13 | B |
| 10 | Create a basic functional log in screen | Users can log in, and software can distinguish between employees and customers | 70 minutes | Feb 13 | C |
| 11 | Create a basic functional registration screen | Screen allows for registration of new customer accounts | 70 minutes | Feb 14 | C |
| 12 | Add verification hash to user login information | Ensure that database cannot be altered to make unauthorized users access employee screen | 30 minutes | Feb 14 | C |
| 13 | Improve aesthetic of log in and registration screen | Improve user experience | 30 minutes | Feb 15 | C |
| 14 | Create a map that can show the restaurants stored in the database | Users have a way to visualize their location | 1 hour 40 minutes | Feb 20 | C |
| 15 | Add the feature that allows a marker to spawn on the map where clicked | Users can select their location | 10 minutes | Feb 22 | C |
| 16 | Create a function that automatically adds food cards to the screen | Information in the database is presented to users in a convenient way | 1 hour 30 minutes | Feb 23 | C |
| 17 | Add a function that submits the order to the database | Orders are recorded properly | 20 minutes | Feb 25 | C |
| 18 | Add logic to find the closest restaurant to the map marker | Users can accurately know which location is closest to them | 40 minutes | Feb 25 | C |
| 19 | Add a way to draw lines from the closest restaurant to the marker | Easier for users to visualize where the restaurant and their location are located on the map | 20 minutes | Feb 25 | C |
| 20 | Add code to correct screen touch information to map coordinates | Ensure that map touch is accurately translated into map coordinates regardless of screen resolution | 15 minutes | Feb 28 | C |
| 21 | Create hamburger menu to switch between employee screens | Ensure consistency in UI between the screens | 1 hour | March 1 | C |
| 22 | Create table template for employee screens | Minimize possible error points in employee screens | 2 hours | March 3 | C |
| 23 | Add function to retrieve column name for employee's tables | Software retrieves the right data based on the type of employee screen | 20 minutes | March 3 | C |
| 24 | Add function to retrieve row data from employee's tables | Tables in employee screens show the right type of data | 25 minutes | March 5 | C |
| 25 | Integrate row and column data retrieved from database to table template for employee screens | Tables in employee screens show the right type of data | 1 hour | March 5 | C |
| 26 | Add way to modify rows in table | Employees can modify preexisting data in table | 1 hour 20 minutes | March 8 | C |
| 27 | Add function to add new rows to the table | Employees can add additional data to the table | 20 minutes | March 8 | C |
| 28 | Add function to save new row and modified row to database | Data from table can be correctly saved to the database | 20 minutes | March 9 | C |
| 29 | Verify that text fields only accept the type of data they should accept | Minimize the risk that calculations and functions that use data from these text fields deviate from what they are supposed to perform | 40 minutes | March 9 | C |
| 30 | Add hint and error texts to text fields | Improve the user experience | 30 minutes | March 9 | C |
| 31 | Run tests in accordance to the test plan| Run tests in accordance with the test plan | 20 minutes | March 10 | B/C/D |
| 32 | Add a function that allows users to remove items from their cart | Users can effectively manage their cart, fulfilling feedback from client | 45 minutes | March 10 | C |
| 33 | Create demonstration video for my product | Verify that my product works in its entirety | 45 minutes | March 11 | D |
| 34 | Add additional comments to clarify my code | Increase ease of possible future modifications | 20 minutes | March 11 | D |
| 35 | Meet client for final evaluation | Client confirms that the program fulfills every success criteria | 20 minutes | March 11 | A/D |

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



