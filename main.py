import customtkinter as ctk
from tkinter import *

# Initializing the app
ctk.set_default_color_theme ("green")
ctk.set_appearance_mode ("light")

# Global variable
app_geometry = "600x520"
c_radius, padding       = 10, 10
rect_width, rect_height = 590, 510
radius_values           = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# Initializing the app
root = ctk.CTk ()
root.geometry(app_geometry)
root.title ("Helium Notes")

if __name__ == '__main__':
    root.mainloop()