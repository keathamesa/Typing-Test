1. Project Title:
Typing Test Application

2. Project Issue / Problem to be Solved:
The project aims to provide an engaging platform to improve typing speed and accuracy while tracking user progress over time. The inclusion of login and signup features enhances user personalization, enabling users to store and compare their results.

3. Current Progress (PDLC):

Problem Analysis: Completed. The need for a typing practice and test application with user authentication and progress tracking has been identified.
Design: Implemented. The project includes structured Tkinter-based GUIs for Home, Signup, Login, and Game pages.
Implementation: The application includes functionalities like user registration, login validation, gameplay mechanics, and result tracking.
Testing: In progress, focusing on UI functionality, gameplay logic, and data persistence.
Deployment: Not yet deployed.

4. Project Functions/Features:

Authentication:
User signup (store username/password).
User login (validate credentials).
Typing Game:
Random word display for typing.
Timer to measure speed.
Scoring based on correctly typed words.
Tracking missed words.
Result Tracking:
Store and display past results (e.g., score, time taken).
Show improvements over previous attempts.

5. Expected No. of Pages:

Home Page: Welcome screen with navigation to login or signup.
Signup Page: Form for new user registration.
Login Page: Form for user login.
Game Page: Main gameplay screen with words, timer, and score display.
Result Page (integrated into the Game Page): Displays performance metrics after game completion.

6. Database Applied:

Data Structures:
user_credentials: Dictionary to store usernames and passwords.
previous_results: List to store scores and times for individual users.
Records: No external database is used. All data is stored in memory, making it volatile. Future improvements could involve integrating a database like SQLite.

7. Project References / Sources:

Refernece:  (https://pythongeeks.org/python-typing-test-project/)
Libraries used:
Tkinter for GUI development.
english_words for retrieving a set of English words.


Instruction on how t run the code application:

Required Software and Libraries
Python 3.x Required Python libraries:
tkinter
english-words
Installation Instructions Install Python:
Download and install Python from the official Python website.
Ensure Python is added to your system's PATH during installation. Install Required Libraries:
Open a terminal or command prompt and run: pip install english-words
Running the Application Save the Code:
Copy the provided Python code (https://pythongeeks.org/python-typing-test-project/) into a file and save it with a .py extension, e.g., typing_test.py. Run the Application:
Open a terminal or command prompt.
Navigate to the directory where the file is saved. Run the application with:
python typing_test.py Navigate Through the GUI:
The home screen will display "Login" and "Signup" buttons.
Use the "Signup" option to create a user account.
Use the "Login" option to access the typing test.
Follow the instructions within the application to play.
Configuration Settings User Credentials:
Usernames and passwords are stored in the user_credentials dictionary during runtime. This is a simple implementation and does not persist data between sessions. Game Settings:
The number of words in a game is limited to 10 (if count < 10).
Dependencies External Services/Data Sources:
The application uses the english-words library to fetch English words from the "web2" word set.
