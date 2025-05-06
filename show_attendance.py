import pandas as pd
from glob import glob
import os
import tkinter
import csv
import tkinter as tk
from tkinter import *

def Mealchoose(text_to_speech):
    def calculate_attendance():
        Meal = tx.get()
        if Meal=="":
            t='Please enter the Meal name.'
            text_to_speech(t)
    
        filenames = glob(
            f"Attendance\\{Meal}\\{Meal}*.csv"
        )
        df = [pd.read_csv(f) for f in filenames]
        newdf = df[0]
        for i in range(1, len(df)):
            newdf = newdf.merge(df[i], how="outer")
        newdf.fillna(0, inplace=True)
        newdf["Attendance"] = 0
        for i in range(len(newdf)):
            newdf["Attendance"].iloc[i] = str(int(round(newdf.iloc[i, 2:-1].mean() * 100)))+'%'
            #newdf.sort_values(by=['Enrollment'],inplace=True)
        newdf.to_csv(f"Attendance\\{Meal}\\attendance.csv", index=False)

        root = tkinter.Tk()
        root.title("Attendance of "+Meal)
        root.configure(background="#EFDFBB")
        cs = f"Attendance\\{Meal}\\attendance.csv"
        with open(cs) as file:
            reader = csv.reader(file)
            r = 0

            for col in reader:
                c = 0
                for row in col:

                    label = tkinter.Label(
                        root,
                        width=10,
                        height=1,
                        fg="#722F37",
                        font=("times", 15, " bold "),
                        bg="#EFDFBB",
                        text=row,
                        relief=tkinter.RIDGE,
                    )
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
        root.mainloop()
        print(newdf)

    Meal = Tk()
    # windo.iconbitmap("AMS.ico")
    Meal.title("Meal...")
    Meal.geometry("580x320")
    Meal.resizable(0, 0)
    Meal.configure(background="#DABF80")
    # Meal_logo = Image.open("UI_Image/0004.png")
    # Meal_logo = Meal_logo.resize((50, 47), Image.ANTIALIAS)
    # Meal_logo1 = ImageTk.PhotoImage(Meal_logo)
    titl = tk.Label(Meal, bg="#DABF80", relief=RIDGE, bd=10, font=("arial", 30))
    titl.pack(fill=X)
    # l1 = tk.Label(Meal, image=Meal_logo1, bg="black",)
    # l1.place(x=100, y=10)
    titl = tk.Label(
        Meal,
        text="Which Meal of Attendance?",
        bg="#DABF80",
        fg="green",
        font=("arial", 25),
    )
    titl.place(x=100, y=12)

    def Attf():
        sub = tx.get()
        if sub == "":
            t="Please enter the Meal name!!!"
            text_to_speech(t)
        else:
            os.startfile(
            f"Attendance\\{sub}"
            )


    attf = tk.Button(
        Meal,
        text="Check Sheets",
        command=Attf,
        bd=7,
        font=("times new roman", 15),
        bg="#DABF80",
        fg="#722F37",
        height=2,
        width=10,
        relief=RIDGE,
    )
    attf.place(x=360, y=170)

    sub = tk.Label(
        Meal,
        text="Enter Meal",
        width=10,
        height=2,
        bg="#DABF80",
        fg="#722F37",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 15),
    )
    sub.place(x=50, y=100)

    tx = tk.Entry(
        Meal,
        width=15,
        bd=5,
        bg="#DABF80",
        fg="#722F37",
        relief=RIDGE,
        font=("times", 30, "bold"),
    )
    tx.place(x=190, y=100)

    fill_a = tk.Button(
        Meal,
        text="View Attendance",
        command=calculate_attendance,
        bd=7,
        font=("times new roman", 15),
        bg="#DABF80",
        fg="#722F37",
        height=2,
        width=12,
        relief=RIDGE,
    )
    fill_a.place(x=195, y=170)
    Meal.mainloop()
