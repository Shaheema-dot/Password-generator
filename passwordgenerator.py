import random
import tkinter as tk 
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

root = tk.Tk()
root.title("Random Password Generator")
root.geometry('750x500')

label = tk.Label(root, text="Password Generator", anchor=N, fg='white',bg='orange', font=("Helvetica 30"))
label.grid(row=0, column=0, columnspan=4, pady=(0,40),ipadx=195) 

var = IntVar()
var1 = IntVar()

url_target = tk.Label(root, text="URL",font=("Helvetica", 15),fg='black')
url_target.grid(row=2, column=0,pady=(0,10),padx=(100,0))
url = Entry(root,font=("Helvetica", 10),width=31)
url.grid(row=2, column=1,pady=(0,10),padx=(0,90))

Username = tk.Label(root, text= "Username/Email",font=("Helvetica", 15),fg='black')
Username.grid(row=3,pady=(0,10),padx=(100,0))
user = Entry(root,font=("Helvetica", 10),width=31)
user.grid(row=3, column=1,pady=(0,10),padx=(0,90))

length = tk.Label(root, text="Length",font=("Helvetica", 15),fg='black')
length.grid(row=4,pady=(0,10),padx=(100,0))

combo = Combobox(root, width=34,textvariable=var1)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, "Length")              
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(row=4,column=1,pady=(0,10),padx=(0,90),ipady=1)

Strength = tk.Label(root, text="Strength",font=("Helvetica", 15),fg='black')
Strength.grid(row=5,column=0,padx=(90,55),sticky='e')

style = Style(root)
style.configure("TRadiobutton",foreground = "black", font = ("Helvetica", 15))
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=5,column=1,columnspan=3,padx=(0,360))
radio_middle = Radiobutton(root, text="Medium", variable=var, value=3)
radio_middle.grid(row=5, column=1,padx=(0,110))
radio_strong = Radiobutton(root, text="Strong", variable=var, value=0)
radio_strong.grid(row=5, column=1,padx=(90,25))


Random_password = tk.Label(root, text="Password",font=("Helvetica", 15),fg='black')
Random_password.grid(row=7,column=0,pady=(5,10),padx=(100,0))
entry = Entry(root,font=("Helvetica", 10),width=30)
entry.grid(row=7, column=1,pady=(5,10),padx=(5,90))


def low():
    entry.delete(0, END)

    length = var1.get()

    lowSecurity = "abcdefghijklmnopqrstuvwxyz0123456789"
    mediumSecurity = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    highSecurity = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    password = ""

    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lowSecurity)
        return password

    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(mediumSecurity)
        return password

    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(highSecurity)
        return password
    else:
        print("Please choose an option")

def generate():
    password1 = low()
    entry.insert(10, password1)

def save():
    url_target = url.get()
    Username = user.get()
    random_password = entry.get()
    f= open(Username+".txt", "a+")
    f.write("Your targeted URL: "+url_target+"\r\n"+"Your UserName: "+Username+"\r\n"+"Your Password: "+random_password+"\r\n")
    messagebox.showinfo("Credentials Saved", "Your Credentials are saved.")

copy_button = tk.Button(root, text="Save", command=save, font=("Helvetica", 15),bg="orange",width=11, fg='white', bd=5)
copy_button.grid(row=8,column=1,pady=(10,0),padx=(0,90))
generate_button = tk.Button(root, text="Generate", command=generate,font=("Helvetica", 15),bg="orange",width=12, fg='white', bd=5)
generate_button.grid(row=6,column=1,pady=(10,10),padx=(0,90))

root.mainloop()
 
