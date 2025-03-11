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
