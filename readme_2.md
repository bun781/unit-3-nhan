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
