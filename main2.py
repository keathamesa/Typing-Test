from english_words import get_english_words_set
from tkinter import *
import tkinter.font as font
import random

# Global variables for the game
score = 0
missed = 0
time = 0
count = 0
words = list(get_english_words_set(sources=["web2"]))
user_credentials = {}  # Dictionary to store user credentials
previous_results = []  # List to store previous results


# Function for Home Page
def homePage():
    home = Tk()
    home.geometry("600x600")
    home.title("Home - Typing Test")
    home.config(bg="LightBlue1")

    Label(
        home,
        text="Welcome to Typing Test",
        font=("Courier", 18, "bold"),
        bg="LightBlue1",
    ).place(relx=0.2, rely=0.2)

    Button(
        home,
        text="Login",
        bg="old lace",
        fg="black",
        width=20,
        height=2,
        command=lambda: [home.destroy(), loginPage()],
    ).place(x=200, y=250)

    Button(
        home,
        text="Signup",
        bg="old lace",
        fg="black",
        width=20,
        height=2,
        command=lambda: [home.destroy(), signupPage()],
    ).place(x=200, y=350)

    home.mainloop()


# Function for Signup Page
def signupPage():
    signup = Tk()
    signup.geometry("600x600")
    signup.title("Signup - Typing Test")
    signup.config(bg="LightBlue1")

    def register():
        username = usernameEntry.get()
        password = passwordEntry.get()
        if username and password:
            user_credentials[username] = password
            Label(
                signup,
                text="Signup Successful! Please Login.",
                font=("Courier", 12),
                fg="green",
                bg="LightBlue1",
            ).place(x=150, y=400)
        else:
            Label(
                signup,
                text="Please fill all fields!",
                font=("Courier", 12),
                fg="red",
                bg="LightBlue1",
            ).place(x=150, y=400)

    Label(
        signup,
        text="Signup",
        font=("Courier", 18, "bold"),
        bg="LightBlue1",
    ).place(relx=0.4, rely=0.1)

    Label(signup, text="Username:", font=("Courier", 12), bg="LightBlue1").place(x=100, y=200)
    usernameEntry = Entry(signup, font=("Courier", 12))
    usernameEntry.place(x=200, y=200)

    Label(signup, text="Password:", font=("Courier", 12), bg="LightBlue1").place(x=100, y=250)
    passwordEntry = Entry(signup, show="*", font=("Courier", 12))
    passwordEntry.place(x=200, y=250)

    Button(signup, text="Signup", bg="old lace", fg="black", command=register).place(x=250, y=300)

    Button(
        signup,
        text="Back",
        bg="old lace",
        fg="black",
        command=lambda: [signup.destroy(), homePage()],
    ).place(x=250, y=350)

    signup.mainloop()


# Function for Login Page
def loginPage():
    login = Tk()
    login.geometry("600x600")
    login.title("Login - Typing Test")
    login.config(bg="LightBlue1")

    def validateLogin():
        username = usernameEntry.get()
        password = passwordEntry.get()
        if username in user_credentials and user_credentials[username] == password:
            login.destroy()
            startGame()
        else:
            Label(
                login,
                text="Invalid Credentials!",
                font=("Courier", 12),
                fg="red",
                bg="LightBlue1",
            ).place(x=200, y=400)

    Label(
        login,
        text="Login",
        font=("Courier", 18, "bold"),
        bg="LightBlue1",
    ).place(relx=0.4, rely=0.1)

    Label(login, text="Username:", font=("Courier", 12), bg="LightBlue1").place(x=100, y=200)
    usernameEntry = Entry(login, font=("Courier", 12))
    usernameEntry.place(x=200, y=200)

    Label(login, text="Password:", font=("Courier", 12), bg="LightBlue1").place(x=100, y=250)
    passwordEntry = Entry(login, show="*", font=("Courier", 12))
    passwordEntry.place(x=200, y=250)

    Button(login, text="Login", bg="old lace", fg="black", command=validateLogin).place(x=250, y=300)

    Button(
        login,
        text="Back",
        bg="old lace",
        fg="black",
        command=lambda: [login.destroy(), homePage()],
    ).place(x=250, y=350)

    login.mainloop()


# Function to start the game
def startGame():
    global score, time, count
    score, time, count = 0, 0, 0  # Reset game variables
    gameWindow = Tk()
    gameWindow.geometry("800x600")
    gameWindow.title("Typing Test By PythonGeeks")
    gameWindow.config(bg="honeydew2")

    def timeFunc():
        global time, score, count
        if count < 10:  # Allow only 10 words
            time += 1
            timer.configure(text=time)
            timer.after(1000, timeFunc)
        else:  # End game and show results
            previous_results.append((score, time))  # Store the current result
            previous_score = previous_results[-2][0] if len(previous_results) > 1 else None

            result_text = f"Time taken = {time} seconds\nScore = {score}\nMissed = {10 - score}"
            if previous_score is not None:
                result_text += f"\nPrevious Score = {previous_score}\nImprovement = {score - previous_score}"

            result = Label(
                gameWindow,
                text=result_text,
                font=("arial", 18, "italic bold"),
                fg="grey",
            )
            result.place(x=150, y=200)

            # Ask if the user wants to play again
            play_again = Button(
                gameWindow,
                text="Play Again",
                bg="light green",
                font=("arial", 15),
                command=lambda: [gameWindow.destroy(), startGame()],
            )
            play_again.place(x=200, y=400)

            exit_game = Button(
                gameWindow,
                text="Exit",
                bg="salmon",
                font=("arial", 15),
                command=gameWindow.destroy,
            )
            exit_game.place(x=400, y=400)

            userInput.destroy()
            nextWord.destroy()

    def mainGame(event):
        global score, count
        if time == 0:  # Start the timer on the first keypress
            random.shuffle(words)
            nextWord.configure(text=words[0])
            userInput.delete(0, END)
            timeFunc()

        if userInput.get() == nextWord["text"]:  # Correct input
            score += 1
            scoreboard.configure(text=score)
        count += 1

        if count < 10:  # Prepare next word
            random.shuffle(words)
            nextWord.configure(text=words[0])
            userInput.delete(0, END)

    # Add widgets to the game window
    Label(gameWindow, text="Typing Test", font=("arial", 25, "italic bold"), fg="gray").place(x=10, y=10)
    nextWord = Label(gameWindow, text="Hit Enter to start!", font=("arial", 20, "italic bold"), fg="black")
    nextWord.place(x=30, y=240)

    Label(gameWindow, text="Your Score:", font=("arial", 25, "italic bold"), fg="red").place(x=10, y=100)
    scoreboard = Label(gameWindow, text=score, font=("arial", 25, "italic bold"), fg="blue")
    scoreboard.place(x=200, y=100)

    Label(gameWindow, text="Time Elapsed:", font=("arial", 25, "italic bold"), fg="red").place(x=500, y=100)
    timer = Label(gameWindow, text=time, font=("arial", 25, "italic bold"), fg="blue")
    timer.place(x=580, y=100)

    userInput = Entry(gameWindow, font=("arial", 25, "italic bold"), bd=10, justify="center")
    userInput.place(x=150, y=330)
    userInput.focus_set()

    gameWindow.bind("<Return>", mainGame)
    gameWindow.mainloop()


# Start the application with Home Page
homePage()
