#!/usr/bin/python3

import tkinter as tk
from PIL import Image, ImageTk

def button1_clicked():
    print("Button 1 clicked")

def button2_clicked():
    print("Button 2 clicked")

def button3_clicked():
    print("Button 3 clicked")

def button4_clicked():
    print("Button 4 clicked")

def button5_clicked():
    print("Button 5 clicked")

def button6_clicked():
    print("Button 6 clicked")

root = tk.Tk()
root.title("6 Buttons Interface")
root.geometry("1366x768")
root.iconbitmap(r"C:\Users\zabel\Desktop\shell.png")


button1 = tk.Button(root, text="Button 1", command=button1_clicked)
button1.pack()
button1.image = mushroom_cup_icon

button2 = tk.Button(root, text="Button 2", command=button2_clicked)
button2.pack()

button3 = tk.Button(root, text="Button 3", command=button3_clicked)
button3.pack()

button4 = tk.Button(root, text="Button 4", command=button4_clicked)
button4.pack()

button5 = tk.Button(root, text="Button 5", command=button5_clicked)
button5.pack()

button6 = tk.Button(root, text="Button 6", command=button6_clicked)
button6.pack()

root.mainloop()
                                                
