import tkinter as tk
import time
from tkinter import*

class App():

    def __init__(self):
        
        
        # Function to inform user that alarm has been set
        def alarmSet():
            global alarmTime
            global message
            message = messageEntry.get()
            tk.messagebox.showinfo("Set", "Alarm set for " + alarmTime)


        # Function to get the time for the alarm to go off
        def getAlarmString():
            hour = hourSpin.get()
            minute = minuteSpin.get()
            if (len(str(hour)) < 2):
                hour = "0" + hour
            if (len(str(minute)) < 2):
                minute = "0" + minute
            global alarmTime
            alarmTime = (hour + ":" + minute + ":00")
            alarmSet()

        # Elements of the GUI
        self.root = tk.Tk()
        currentTime = tk.Label(text = "Current time:", font = ("Helvetica", 24))
        currentTime.grid(row = 1, column = 2, columnspan = 2)
        self.label = tk.Label(text="", font = ("Helvetica", 32))
        self.label.grid(row = 2, column = 2, columnspan = 2, pady = 5)
        self.update_clock()
        setAlarmTime = tk.Label(text = "Set alarm time:", font = ("Helvetica", 20))
        setAlarmTime.grid(row = 4, column = 2, columnspan = 2, pady = 5)

        hourSelect = tk.Label(text = "Hour:", font = ("Helvetica", 18))
        hourSelect.grid(row = 5, column = 2, sticky = E, padx = 5)

        hourSpin = Spinbox(self.root, from_=0, to=24, font = ("Helvetica", 18), width = 2)
        hourSpin.grid(row = 6, column = 2, sticky = E, padx = 5)

        minuteSelect = tk.Label(text = "Minute:", font = ("Helvetica", 18))
        minuteSelect.grid(row = 5, column = 3, sticky = W, padx = 5)

        minuteSpin = Spinbox(self.root, from_=0, to=60, font = ("Helvetica", 18), width = 2)
        minuteSpin.grid(row = 6, column = 3, sticky = W, padx = 5)

        alarmMessage = tk.Label(text = "What message should appear when the alarm goes off?", font = ("Helvetica", 16))
        alarmMessage.grid(row = 7, column = 2, columnspan = 2, padx = 5, pady = 5)

        messageEntry = Entry(self.root, font = ("Helvetica", 16))
        messageEntry.grid(row = 8, column = 2, columnspan = 2, padx = 5, pady = 5)

        alarmButton = Button(self.root, text = "Set Alarm", font = ("Helvetica", 20), padx = 5, pady = 5, command = getAlarmString)
        alarmButton.grid(row = 9, column = 2, columnspan = 2, padx = 5, pady = 5)

        

        self.label = tk.Label(text="", font = ("Helvetica", 32))
        self.label.grid(row = 2, column = 2, columnspan = 2, pady = 5)
        self.update_clock()
    
        self.root.title("Alarm clock")

        
        self.root.mainloop()

    # Function to update the time of the clock once per second.
    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)
        
        # Branch to make the alarm message appear when it's the right time.
        if alarmTime:
            if (alarmTime == now):
                tk.messagebox.showinfo("Alarm!", message)
            else:
                pass
        else:
            pass

app=App()
