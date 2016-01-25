import tkinter as tk
import time
from tkinter import*

class App():

    def __init__(self):


        self.root = tk.Tk()

        

        self.label = tk.Label(text="", font = ("Helvetica", 32))
        self.label.grid(row = 2, column = 2, columnspan = 2, pady = 5)
        self.update_clock()
    
        self.root.title("Alarm clock")

        
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

app=App()
