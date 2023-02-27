import os
import socket
import sqlite3
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk, ImageOps
from rich import print
from rich.console import Console
from rich.traceback import install

import art
import loadingscr
from dbgrabber import dbgrab

install()

console = Console(record=True)

download = 0

print("[bold red]Waiting for Login!..[/bold red]")
while True:
    def is_connected():
        os.system("cls||clear")
        art.art2()
        try:
            # Connect to a website and port to check if the connection is successful
            host = socket.gethostbyname("www.google.com")
            s = socket.create_connection((host, 80), 2)
            windowcreate = 1
            return True
        except:
            pass
        return False


    if is_connected():
        if download == 0:
            dbgrab()
            download = download+1
        AccountSystem = Tk()
        AccountSystem.rowconfigure(0, weight=1)
        AccountSystem.columnconfigure(0, weight=1)
        height = 550
        width = 580
        x = (AccountSystem.winfo_screenwidth() // 2) - (width // 2)
        y = (AccountSystem.winfo_screenheight() // 4) - (height // 4)
        AccountSystem.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        AccountSystem.title("ProjectEve")

        sign_in = Frame(AccountSystem)
        sign_up = Frame(AccountSystem)

        for frame in (sign_in, sign_up):
            frame.grid(row=0, column=0, sticky='nsew')


        def show_frame(frame):
            frame.tkraise()


        show_frame(sign_in)

        # Variables
        Email = StringVar()
        Password = StringVar()

        sign_in.configure(bg="#525561")

        # ================Background Image ====================
        Login_backgroundImage = Image.open("assets\\image_1.png")
        img = ImageOps.fit(Login_backgroundImage, (620, 744), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        bg_imageLogin = Label(
            sign_in,
            image=img,
            bg="#525561"
        )
        bg_imageLogin.pack(fill=BOTH, expand=True)
        # ================ Header Text Left ====================
        Login_headerText_image_left = PhotoImage(file="assets\\headerText_image.png")
        Login_headerText_image_label1 = Label(
            bg_imageLogin,
            image=Login_headerText_image_left,
            bg="#272A37"
        )
        Login_headerText_image_label1.place(x=60, y=45)

        Login_headerText1 = Label(
            bg_imageLogin,
            text="Project_Eve(Ver.1.2)",
            fg="#FFFFFF",
            font=("yu gothic ui bold", 20 * -1),
            bg="#272A37"
        )
        Login_headerText1.place(x=110, y=45)

        # ================ Header Text Right ====================
        Login_headerText_image_right = PhotoImage(file="assets\\headerText_image.png")
        Login_headerText_image_label2 = Label(
            bg_imageLogin,
            image=Login_headerText_image_right,
            bg="#272A37"
        )

        # ================ LOGIN TO ACCOUNT HEADER ====================
        loginAccount_header = Label(
            bg_imageLogin,
            text="Login to continue",
            fg="#FFFFFF",
            font=("yu gothic ui Bold", 28 * -1),
            bg="#272A37"
        )
        loginAccount_header.place(x=165, y=121)

        # ================ Email Name Section ====================
        Login_emailName_image = PhotoImage(file="assets\\email.png")
        Login_emailName_image_Label = Label(
            bg_imageLogin,
            image=Login_emailName_image,
            bg="#272A37"
        )
        Login_emailName_image_Label.place(x=76, y=242)

        Login_emailName_text = Label(
            Login_emailName_image_Label,
            text="Email account",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        Login_emailName_text.place(x=25, y=0)

        Login_emailName_icon = PhotoImage(file="assets\\email-icon.png")
        Login_emailName_icon_Label = Label(
            Login_emailName_image_Label,
            image=Login_emailName_icon,
            bg="#3D404B"
        )
        Login_emailName_icon_Label.place(x=370, y=15)

        Login_emailName_entry = Entry(
            Login_emailName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
            textvariable=Email
        )
        Login_emailName_entry.place(x=30, y=20, width=330, height=27)

        # ================ Password Name Section ====================
        Login_passwordName_image = PhotoImage(file="assets\\email.png")
        Login_passwordName_image_Label = Label(
            bg_imageLogin,
            image=Login_passwordName_image,
            bg="#272A37"
        )
        Login_passwordName_image_Label.place(x=80, y=330)

        Login_passwordName_text = Label(
            Login_passwordName_image_Label,
            text="Password",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        Login_passwordName_text.place(x=25, y=0)

        Login_passwordName_icon = PhotoImage(file="assets\\pass-icon.png")
        Login_passwordName_icon_Label = Label(
            Login_passwordName_image_Label,
            image=Login_passwordName_icon,
            bg="#3D404B"
        )
        Login_passwordName_icon_Label.place(x=370, y=15)

        Login_passwordName_entry = Entry(
            Login_passwordName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
            textvariable=Password
        )
        Login_passwordName_entry.place(x=30, y=20, width=330, height=27)

        # =============== Submit Button ====================
        Login_button_image_1 = PhotoImage(
            file="assets\\button_1.png")
        Login_button_1 = Button(
            bg_imageLogin,
            image=Login_button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: login(),
            relief="flat",
            activebackground="#272A37",
            cursor="hand2",
        )
        Login_button_1.place(x=120, y=420, width=333, height=65)


        # Clear Login Fields.
        def clear_login():
            Email.set("")
            Password.set("")


        # DB Connection

        def login():
            # conn = sqlite3.connect('databases.000webhost.com', user='projectevedb', password='[[4/MaEX~Q5mI48h', db='projecteve')
            conn = sqlite3.connect("./Database/Userdata.db")
            cursor = conn.cursor()
            find_user = 'SELECT * FROM AccountDB WHERE Email = ? and Password = ?'
            cursor.execute(find_user, [(Login_emailName_entry.get()), (Login_passwordName_entry.get())])
            result = cursor.fetchall()
            if result:
                clear_login()
                messagebox.showinfo("Success", "Logged in Successfully!")
                os.system("clear||cls")
                AccountSystem.destroy()  # destroy the window immediately after successful login
                loadingscr.loadscr()
                AccountSystem.quit()
            else:
                messagebox.showerror("Failed", "Try Again!")

        AccountSystem.protocol('WM_DELETE_WINDOW', lambda: None)
        AccountSystem.mainloop()
        # AccountSystem.resizable(False, False)
    else:
        messagebox.showerror("Error","Connection Error! Try Again!")
        break
        breakpoint()

# console.save_html("log\\log_main.html")

if __name__ == "__main__":
    is_connected()




