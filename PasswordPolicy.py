# Author :           James Pellerin
# Date:              11/14/2021

import tkinter as tk
import re
root = tk.Tk()

# displays main menu with option buttons
def main_menu():

    # main screen
    canvas = tk.Canvas(root, width = 600, height = 350)
    canvas.grid(columnspan=3)
    root.title('Password Policy')

    # title
    tk.Label(root, text="Password Policy", font=('Helvetica bold',40)).place(x=300, y=60, anchor='center')
    tk.Label(root, text="Edition 1.1.12", font=('Helvetica', 25)).place(x=300, y=115, anchor='center')

    # sign in button
    tk.Button(root, text = "Sign In", command =lambda:sign_in(),
                           bg="white", font=('Helvetica bold',20), width = 15).place(x=300, y=220, anchor='center')

    # create account button
    tk.Button(root, text = "Create Account", command =lambda:create_account(),
                           bg="white", font=('Helvetica bold',20), width = 15).place(x=300, y=290, anchor='center')

# UNENCRYPTED PASSWORD MANAGEMENT FOR CLASS DEMO
# universal dictionary stores username and password
usersList = {"root" : "debug"}
# stores passwords for username in linked list (prevents new password from repeating up)
SavedPasswords = { }

# sign in menu
def sign_in():
    window = tk.Toplevel(root)

    # main screen
    canvas = tk.Canvas(window, width = 500, height = 300, bg='gray90')
    canvas.grid(columnspan=3)

    tk.Label(window, text="Username:", bg='gray90', font=('Helvetica', 12)).place(x=25, y=65)
    username =tk.Entry(window, font=('Helvetica', 12), width=30)
    username.place(x=150, y=65)

    tk.Label(window, text="Password:", bg='gray90', font=('Helvetica', 12)).place(x=25, y=95)
    userPassword =tk.Entry(window, show= '*')
    userPassword.config(font=('Helvetica', 12), width=30)
    userPassword.place(x=150, y=95)

    # view / hide password button widget
    def view_password():
        if userPassword.cget('show') == '':
            userPassword.config(show='*')
            view.config(text='show password')
        else:
            userPassword.config(show='')
            view.config(text='hide password')

    # place view button
    view = tk.Button(window, text='show password', command= lambda:view_password())
    view.config(font=('Helvetica', 10))
    view.place(x=374,y=135, anchor='center')

    # redirect to create account page
    tk.Button(window, text='Reset Password', font=('Helvetica', 12), width = 15,
              command= lambda:create_account()).place(x=330,y=250, anchor='center')

    # calls sign in function
    tk.Button(window, text='Sign in', font=('Helvetica', 12), width = 15,
              command= lambda:login(window, username, userPassword)).place(x=180,y=250, anchor='center')

# login function
def login(window, username, userPassword):
    # clears prompt
    tk.Label(window, text="                                                                                                                       "
            , bg='gray90', font=('Helvetica', 12)).place(x = 250, y = 190, anchor='center')

    username = username.get()
    if username in usersList:
        password = userPassword.get()

        # check for user's password
        if password in usersList[username]:
            tk.Label(window, text=("Welcome back " + username), bg='gray90', font=('Helvetica', 14, 'bold')).place(x=250, y=190, anchor='center')

        else:
            tk.Label(window, text="Invalid password", bg='gray90', font=('Helvetica', 14, 'bold')).place(x=250, y=190, anchor='center')
    else:
        tk.Label(window, text="Invalid username", bg='gray90', font=('Helvetica', 14, 'bold')).place(x=250, y=190, anchor='center')

# Create account window
def create_account():
    window = tk.Toplevel(root)

    # main screen
    entry_menu = tk.Canvas(window, width = 600, height = 500, bg='gray90')
    entry_menu.grid(columnspan=3)

    # user account name
    tk.Label(window, text="*First name / Last name:", bg='gray90', font=('Helvetica', 12)).place(x=25, y=20)
    firstName =tk.Entry(window, font=('Helvetica', 12), width=12)
    firstName.place(x=200, y=20)
    lastName =tk.Entry(window, font=('Helvetica', 12), width=17)
    lastName.place(x=320, y=20)

    # user display name
    tk.Label(window, text="* User display name:", bg='gray90', font=('Helvetica', 12)).place(x=25, y=50)
    displayName =tk.Entry(window, font=('Helvetica', 12), width=30)
    displayName.place(x=200, y=50)

    # username
    tk.Label(window, text="* Username:", bg='gray90', font=('Helvetica', 12)).place(x=25, y=80)
    username =tk.Entry(window, font=('Helvetica', 12), width=30)
    username.place(x=200, y=80)

    # enter password
    tk.Label(window, text="* Enter password:", bg='gray90', font=('Helvetica', 12)).place(x=25, y=130)
    userPassword =tk.Entry(window, show= '*')
    userPassword.config(font=('Helvetica', 12), width=30)
    userPassword.place(x=200, y=130)

    # confirm password
    tk.Label(window, text="* Confirm password:", bg='gray90', font=('Helvetica', 12)).place(x=25, y=160)
    userConfirm =tk.Entry(window, show= '*')
    userConfirm.config(font=('Helvetica', 12), width=30)
    userConfirm.place(x=200, y=160)

    tk.Label(window, text="* Required field", bg='gray90', font=('Helvetica', 9)).place(x=25, y=220)

    # view / hide password button widget
    def view_password():
        if userPassword.cget('show') == '':
            userPassword.config(show='*')
            userConfirm.config(show='*')
            view.config(text='show password')
        else:
            userPassword.config(show='')
            userConfirm.config(show='')
            view.config(text='hide password')

    # place view button
    view = tk.Button(window, text='show password', command= lambda:view_password())
    view.config(font=('Helvetica', 10))
    view.place(x=537,y=142, anchor='center')

    # password criteria display
    entry_menu.create_rectangle(15, 275, 585, 490,
             outline="black", fill="white")

    # GUI display text
    tk.Label(window, text="Password must meet the following criteria:", bg='white', font=('Helvetica', 12, 'bold')).place(x=25, y=290)
    lengthDisplay = tk.Label(window, text="[          ]       Minimum password length 14 characters", bg='white', font=('Helvetica', 12))
    lengthDisplay.place(x=50, y=320)
    upperDisplay = tk.Label(window, text="[          ]       Must contain two uppercase letters (A-Z)", bg='white', font=('Helvetica', 12))
    upperDisplay.place(x=50, y=345)
    lowerDisplay = tk.Label(window, text="[          ]       Must contain two lowercase letters (a-z)", bg='white', font=('Helvetica', 12))
    lowerDisplay.place(x=50, y=370)
    numberDisplay = tk.Label(window, text="[          ]       Must contain two numbers letters (0-9)", bg='white', font=('Helvetica', 12))
    numberDisplay.place(x=50, y=395)
    characterDisplay = tk.Label(window, text="[          ]       Must contain two special characters (@#$&*) ", bg='white', font=('Helvetica', 12))
    characterDisplay.place(x=50, y=420)
    nameDisplay = tk.Label(window, text="[          ]       Cannot contain account name, display name, username", bg='white', font=('Helvetica', 12))
    nameDisplay.place(x=50, y=445)

    # validate password button
    validate = tk.Button(window, text='validate password', command=lambda:testPassword(userPassword, userConfirm, firstName, lastName
                                                                                       , displayName, username, window, lengthDisplay,
                                                                                       upperDisplay, lowerDisplay, numberDisplay,
                                                                                       characterDisplay, nameDisplay))
    validate.config(font=('Helvetica', 10))
    validate.place(x = 300, y = 210, anchor='center')


# Test password function widget using regex
def testPassword(userPassword, userConfirm, firstName, lastName, displayName, username, window,
                 lengthDisplay, upperDisplay, lowerDisplay, numberDisplay, characterDisplay, nameDisplay):

    # defines variables (from input field)
    password = userPassword.get()
    confirmPassword = userConfirm.get()

    fName = firstName.get()
    lName = lastName.get()
    displayName = displayName.get()
    username = username.get()

    # clears errors
    tk.Label(window, text="                                                                                                                       "
            , bg='gray90', font=('Helvetica', 12)).place(x = 300, y = 255, anchor='center')

    # password and confirmation password match
    if password == confirmPassword:
        # Initially sets valid password to true. If any case fails, valid password is automatically false.
        validPassword = True

        # redirection from "reset password"
        if username in SavedPasswords:
            # deletes oldest password of 4 iterations ago
            if len(SavedPasswords[username]) == 4:
                del SavedPasswords[username] [0]


        # tests password length
        if len(password) >= 14:
            lengthDisplay.config(fg='green')
            tk.Label(window, text="[   ✓   ]", bg='white', fg='green', font=('Helvetica', 12)).place(x=50, y=320)
        else:
            lengthDisplay.config(fg='red')
            tk.Label(window, text="[          ]", bg='white', fg='red', font=('Helvetica', 12)).place(x=50, y=320)
            validPassword = False

        # tests for 2 uppercase
        if re.search("[A-Z].*[A-Z]", password):
            upperDisplay.config(fg='green')
            tk.Label(window, text="[   ✓   ]", bg='white', fg='green', font=('Helvetica', 12)).place(x=50, y=345)
        else:
            upperDisplay.config(fg='red')
            tk.Label(window, text="[          ]", bg='white', fg='red', font=('Helvetica', 12)).place(x=50, y=345)
            validPassword = False

        # tests for 2 lowercase
        if re.search("[a-z].*[a-z]", password):
            lowerDisplay.config(fg='green')
            tk.Label(window, text="[   ✓   ]", bg='white', fg='green', font=('Helvetica', 12)).place(x=50, y=370)
        else:
            lowerDisplay.config(fg='red')
            tk.Label(window, text="[          ]", bg='white', fg='red', font=('Helvetica', 12)).place(x=50, y=370)
            validPassword = False

        # tests for 2 numbers
        if re.search("[0-9].*[0-9]", password):
            numberDisplay.config(fg='green')
            tk.Label(window, text="[   ✓   ]", bg='white', fg ='green', font=('Helvetica', 12)).place(x=50, y=395)
        else:
            numberDisplay.config(fg='red')
            tk.Label(window, text="[          ]", bg='white', fg ='red', font=('Helvetica', 12)).place(x=50, y=395)
            validPassword = False

        # tests for special character
        if re.search("[@#$&*].*[@#$&*]", password):
            characterDisplay.config(fg='green')
            tk.Label(window, text="[   ✓   ]", bg='white', fg = 'green', font=('Helvetica', 12)).place(x=50, y=420)
        else:
            characterDisplay.config(fg='red')
            tk.Label(window, text="[          ]", bg='white', fg='red', font=('Helvetica', 12)).place(x=50, y=420)
            validPassword = False

        # tests for account name, username, or display name
        if re.search(fName.lower(), password.lower()) or re.search(lName.lower(), password.lower()) or \
           re.search(displayName.lower(), password.lower()) or re.search(username.lower(), password.lower()):

            nameDisplay.config(fg='red')
            tk.Label(window, text="[          ]", bg='white', fg = 'red', font=('Helvetica', 12)).place(x=50, y=445)
            validPassword = False
        else:
            nameDisplay.config(fg='green')
            tk.Label(window, text="[   ✓   ]", bg='white', fg='green', font=('Helvetica', 12)).place(x=50, y=445)

        # redirection from reset password
        if username in usersList:

            # tests for new password for changed characters
            oldPassword = usersList[username]
            char_count = 0
            for i in range(0, len(password)):
                if oldPassword[i] == password[i]:
                    char_count = char_count + 1
                    i = i + 1
            if char_count > 4:
                tk.Label(window, text="New passwords must differ by at least 4 characters", bg='gray90', font=('Helvetica', 14, 'bold')).place(x = 300, y = 250, anchor='center')
                validPassword = False

            # tests for repeating password
            if password in SavedPasswords[username]:
                tk.Label(window, text="New passwords cannot repeat for 4 iterations", bg='gray90', font=('Helvetica', 14, 'bold')).place(x = 300, y = 250, anchor='center')
                validPassword = False

        # valid password entered, password is saved to username
        if validPassword:
            usersList[username] = password
            SavedPasswords.setdefault(username, []).append(password)
            tk.Label(window, text="Valid Password: Password saved", bg='gray90', font=('Helvetica', 14, 'bold')).place(x = 300, y = 250, anchor='center')

            # Displays current and saved passwords for demo
            print("Current username : password creditals:     " + str(usersList))
            print("Every saved username : every password:     " + str(SavedPasswords))

    # passwordS do not match, display error message
    else:
        tk.Label(window, text="Passwords do not match", bg='gray90', font=('Helvetica', 14, 'bold')).place(x = 300, y = 250, anchor='center')

main_menu()
root.mainloop()
