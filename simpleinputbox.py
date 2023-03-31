# I searched a lot for a simple input text box, just to get a string and pass it to a variable
# This code is not mine and I am saving as it is. I will change it to get an OTP value and add to a password
# in another project where I am trying to scrap a website that has two factor authentication
# The following code was copied from "https://stackoverflow.com/users/13845805/pruthvi".
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
USER_INP = simpledialog.askstring(title="Test",
                                  prompt="What's your Name?:")

# check it out
print("Hello", USER_INP)
