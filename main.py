from tkinter import messagebox
from tkinter import *
from tkinter import ttk

wind = Tk()
wind.geometry("540x440")
wind.title("WappN")
wind.configure(bg="#333333")
frame = Frame(bg="#333333")

def login():
    userName="informatique"
    password="123456"
    if UsernameInput.get()==userName and PwdInput.get()==password:
        UsernameInput.delete(0,END)
        PwdInput.delete(0,END)
        messagebox.showinfo("connection","vous etes  connecté bravo...")
        messageApp= Label(frame,text="vous etes  connecté bravo...",bg="#333333",fg="green",font=("Arial",10))  
    else:
        UsernameInput.delete(0,END)
        PwdInput.delete(0,END)
        messagebox.showerror("no connection","Nom d'utilisateur ou mot de passe incorrect")
        messageApp= Label(frame,text="Nom d'utilisateur ou mot de passe incorrect",bg="#333333",fg="red",font=("Arial",10)) 
    messageApp.grid(row=4,column=0,columnspan=3)    
    
   
#my element

LoginLabel= Label(frame,text="Login",bg="#333333",fg="#ffffff",font=("Arial",30))
UsernameLabel = Label(frame,text="User Name",bg="#333333",fg="#ffffff",font=("Arial",16),highlightcolor='red')
UsernameInput = Entry(frame,font=("Arial",16))
PwdLabel = Label(frame,text="Password",bg="#333333",fg="#ffffff",font=("Arial",16))
PwdInput = Entry(frame,show="*",font=("Arial",16))
LoginButton = Button(frame,text="Login",font=("Arial",16),command=login)

#placing of elements
LoginLabel.grid(row=0,column=0,columnspan=3, sticky="news",pady=40)
UsernameLabel.grid(row=1,column=0,pady=10)
UsernameInput.grid(row=1,column=1)
PwdInput.grid(row=2,column=1)
PwdLabel.grid(row=2,column=0,pady=10)
LoginButton.grid(row=3,column=0,columnspan=3,pady=30)
frame.pack()



wind.mainloop()
