import tkinter as tk
from tkinter import messagebox
import calendar
import datetime
import holidays

class CalendarApp:
    def __init__(self,root):
        self.root=root
        self.root.title("MAVYM Calendier")
        self.ro_holidays=holidays.RO()

        #create control frame for year and month
        control_frame=tk.Frame(root)
        control_frame.pack(pady=10)

        tk.Label(control_frame,text="Year :").grid(row=0,column=0,padx=5)
        self.year_entry=tk.Entry(control_frame,width=6)
        self.year_entry.insert(0,str(datetime.datetime.now().year))
        self.year_entry.grid(row=0,column=3,padx=5)

        tk.Label(control_frame,text="month :").grid(row=0,column=2,padx=5)
        self.month_entry=tk.Entry(control_frame,width=4)
        self.month_entry.insert(0,str(datetime.datetime.now().month))
        self.month_entry.grid(row=0,column=3,padx=5)

        tk.Button(control_frame,text="Show",command=self.update_calendar).grid(row=0,column=4,padx=10)

        #create frame for the calendar
        self.calendar_frame=tk.Frame(root)
        self.calendar_frame.pack(padx=10)

        #Create header for the days of the week
        days_of_week=['Lun','Mar','Mer','Jeu','Ven','Sam','Dim']
        for idx, day in enumerate(days_of_week):
            Ibl=tk.Label(self.calendar_frame,text=day,font=('Arial',10,"bold"),borderwidth=1,relief="solid",width=4,height=2,bg="#f0f0f0")
            Ibl.grid(row=0,column=idx,padx=1,pady=1)#Dispaly the curren calendar on launch
        self.update_calendar()

        def update_calendar(self):
            #Clear previous calendar
            for widget in self.calendar_frame.winfo_children():
                if widget.grid_info()['row'] !='0': #prendre la tete
                    widget.destroy()

        try :
            year=int(self.year_entry.get())
            month=yaer=int(self.month_entry.get())
            if not (i<=month <= 12):
                raise ValueError
        except ValueError :
            messagebox.showerror("Error","Year and month must be valid integer")

