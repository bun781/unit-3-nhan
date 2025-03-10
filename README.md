# Criterion A: Planning
## Problem Definition
My client is an old local restaurateur with a chain of restaurants around the city. Lately, he noticed that the number of customers visiting his restaurants are decreasing since online food ordering and delivering services are on the rise. My client wants to be able to update his service so that the restaurant can compete with these platforms. The restaurant currently only has food delivery via orders done through the phone, but my client said that they refrain from doing so because it provides no written record of the orders. He also said that it generally hurts the relationship between the restaurants and customers because there is nothing recording the order. Furthermore, he said that these disagreements usually start because customers do not know what the dishes look like, nor which ingredients were in it. And as users usually underestimate the cost of delivery to their location, they usually disagree at the food delivery fees. The problem also expands to staff’s reliability in pricing through phones, as they might read the wrong price. He said that whether or not it is accidentally or deliberately, a situation like such should never happen. My client said that most importantly, the restaurant can’t keep track of who is making the calls. He said that the restaurant chain prides on having the best customer service program. Lastly, he requested that the solution should accommodate for his ever expanding restaurant network and food listings.

## Proposed Solution
I propose an application that has a graphic user interface (GUI) allowing users to order their food without the compromises of ordering through phone calls, allowing the restaurant to reliably keep track of the orders.

Python is an interpreted language that is compatible with both Intel x86 and ARM across multiple operating systems. This in addition to Python robust community support and wide range of available libraries allows it to be a great choice for efficiently creating applications that work across multiple platforms.

The graphic framework Kivy and the extension KivyMD will be used to create the GUI for the application. One reason was because Kivy allows responsive design, an important feature when customer’s devices can have varying aspect ratios. Another reason was that KivyMD has Kivy elements that follows Google’s Material Design language, allowing it to appear native and professional. Moreover, Kivy and KivyMD were specifically designed to be implemented with Python, making the development more efficient, streamlined, and minimize unexpected behaviour.

The data storage solution will use SQLite. Relational database tools like SQL are preferred over simple storage options such as CSV or JSON files, as data stored is relatively complex and interrelated. SQLite was selected because it is lightweight and embedded, allowing users to quickly access data even when not having stable connections. It also does not require a lot of storage nor a dedicated server, resources that are excessive for the application and require additional operating cost for my client.

## Success Criteria
- The application has a login and register functions for both users and employees.
- The application allows users to order food and securely save the order to a database.
- The application allows users to select their location through a map.
- The application allows employees to view orders made by customers.
- The employee accounts can add or modify food listings to the software and restaurant locations to the map.

# Criterion B: Design

## Flow Diagrams
![image](https://github.com/user-attachments/assets/c3a995d9-ebb6-4e24-9716-45f2199b7ee2)

Fig x. Flow diagram of the software's login method from the LoginScreen class that can differentiate between employees and customer

![image](https://github.com/user-attachments/assets/4692d369-d84d-4853-a196-434c2446a2a6)

Fig x. Flow diagram of the software's method to add new items to any table of the database

![image](https://github.com/user-attachments/assets/a6d1c5db-ae16-4a78-bc61-9c7e36876585)

Fig x. Flow diagram of the software's method that can send and store customer's order in the database

## System Diagram
![image](https://github.com/user-attachments/assets/4d99e418-e7dd-45dd-bf90-9334d3abbdc2)

## ER Diagram
<img width="1165" alt="image" src="https://github.com/user-attachments/assets/39e9cef4-b210-4736-953d-144f9b30f7b7" />

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
| 31 | Run tests | Run tests in accordance with the test plan | 20 minutes | March 10 | B/C/D |
| 32 | Add a function that allows users to remove items from their cart | Users can effectively manage their cart, fulfilling feedback from client | 45 minutes | March 10 | C |
| 33 | Create demonstration video for my product | Verify that my product works in its entirety | 45 minutes | March 11 | D |
| 34 | Add additional comments to clarify my code | Increase ease of possible future modifications | 20 minutes | March 11 | D |
| 35 | Meet client for final evaluation | Client confirms that the program fulfills every success criteria | 20 minutes | March 11 | A/D |
