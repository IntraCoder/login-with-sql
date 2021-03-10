from tkinter import *
from tkinter import messagebox as msg
import mysql.connector as ms

login_win = Tk()
login_win.geometry("650x350")
login_win.config(bg="navy")
login_win.resizable(0, 0)

#Connecting with Database
mydb = ms.connect(user="root", password="your_sql_password",
                  database="your_database_name", host="localhost")
cur = mydb.cursor()


def login():
    # Put table name you used in place of 'TEST_TABLE'
    cur.execute(f"SELECT * FROM TEST_TABLE")
    login_pairs = cur.fetchall()
    input_pair = (user_ent.get(), pass_ent.get())
    
    if not all(input_pair):# Check if the tuple contains empty string/sequence
        msg.showerror("Empty Fields", "Please fill all fields")
    elif input_pair in login_pairs:
        msg.showinfo("Logged in!", "Login Successuful")
        login_win.destroy()
    else:
        msg.showerror("Invalid data", "Please enter valid details")


pane = PanedWindow(login_win, width=500, height=260, bg="#ffee58",
                   relief=SUNKEN, bd=7).place(x=70, y=45)
Label(login_win, text="Username",
      font=("Bahnshrift semiLifght SemiCondensed", 25), bg="#ffee58", fg="navy").place(x=100, y=100)
Label(login_win, text="Password",
      font=("Bahnshrift semiLifght SemiCondensed", 25), bg="#ffee58", fg="navy").place(x=100, y=150)
user_ent = Entry(login_win,
                 font=("Bahnshrift semiLifght SemiCondensed", 16), bd=5)
pass_ent = Entry(login_win,
                 font=("Bahnshrift semiLifght SemiCondensed", 16), bd=5)
user_ent.place(x=300, y=110)
pass_ent.place(x=300, y=160)

Button(login_win, text="Login",
       font=("Bahnshrift semiLifght SemiCondensed", 17), bg="navy", fg="#ffee58",
       width=10, command=login, bd=4).place(x=250, y=240)
login_win.mainloop()
