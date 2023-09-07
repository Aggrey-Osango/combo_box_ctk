import customtkinter as ctk
from tkinter import *

# Initializing the app
ctk.set_default_color_theme ("green")
ctk.set_appearance_mode ("light")




# Global variable
app_geometry = "600x520"
c_radius, padding       = 10, 10
framex, framey = 590, 510
widthx,heighty = 170, 35

x1, y1 = 0.5, 0.4
x2, y2 = 0.5, 0.5
x3, y3 = 0.5, 0.6
x4, y4 = 0.5, 0.7

radius_values           = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Initializing the app
root = ctk.CTk ()
root.geometry(app_geometry)
root.title ("Helium Notes")

text_var = StringVar ()

frame = ctk.CTkFrame (master = root, width = framex, height = framey)

user_name = ctk.CTkEntry (master = frame, width = widthx, height = heighty, corner_radius = c_radius, placeholder_text = "User Name" )

user_pwd = ctk.CTkEntry (master = frame, width = widthx, height = heighty, corner_radius = c_radius, show = "*")

msg_label = ctk.CTkLabel(master = frame, width = widthx, height = heighty, corner_radius = c_radius, textvariable = text_var, bg_color = "yellow")


def log():
    if (user_name.get() == "aggrey") and (user_pwd.get() == "1234"):
        text_var.set(user_name.get())
        # text_var.set(user_pwd.get())
        print("Success!!")
    else:
        print("Wrong Name or Password")


btn_submit = ctk.CTkButton(master = frame, text = "Submit", corner_radius = c_radius, command = log)


frame.pack(padx=padding, pady=padding)
user_name.place(relx = x1, rely= y1, anchor = CENTER)

user_pwd.place(relx=x2, rely=y2, anchor = CENTER)

btn_submit.place(relx=x4, rely=y4, anchor = CENTER)

msg_label.place(relx=x3, rely=y3, anchor = CENTER)




if __name__ == '__main__':
    root.mainloop()