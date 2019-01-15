## importing required libraries
import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import sqlite3
import sqlite_module as sm
from threading import Thread
import sqlalchemy

## creating tkinter
root = tk.Tk()

appLabel = tk.Label(root, text="Welcome to Webscrapping.")
appLabel.pack()

## function called whenever you click on load button.
def load_data():
    messagebox.showinfo("Info", "Writing file's content to the sql.")
    try:
        ## start thread process to load data from csv file to sql table
        ThreadedTask("load").start()
    except (sqlite3.ProgrammingError, sqlite3.OperationalError, sqlalchemy.exc.ArgumentError, pd.io.sql.DatabaseError) as error:
        messagebox.showerror("Error", "Error while writing file contents")
        print(error)

## function called whenever you click on save button
def show_data():
    messagebox.showinfo("Info", "Fetching records from sql table.")
    try:
        ## start thread process to load data from sqlite table
        ThreadedTask("show").start()
    except (sqlite3.OperationalError, sqlite3.ProgrammingError) as error:
        messagebox.showerror("Error", "Error while fetching records from the database.")


## use this threading to work load and show data
class ThreadedTask(Thread):
    def __init__(self, value):
        Thread.__init__(self)
        self.value = value

  ## defining work to perform during thread
    def run(self):
        connection = sm.database_connection()
        if (self.value == "load"):
            data = pd.read_csv('Quotation.csv')
            data.info()
            data = data.set_index('QUOTE_ID')
            data.head()
            data.to_sql("QUOTATION", connection, if_exists="append")
            messagebox.showinfo("Success", "Done writing files to the database")
        else:
            cursor = sm.read_data()
            createNewFrame(cursor)

## creating a new window just to show data.
def createNewFrame(data):
    displayWindow = tk.Tk()

    displayHeading = tk.Label(displayWindow, text="Displaying web scrapped data.")
    displayHeading.pack()

    ## using tree view
    treeview = ttk.Treeview(displayWindow)

    treeview["columns"] = (1, 2)
    treeview.heading(1, text="Quotation")
    treeview.heading(2, text="Author Name")
    i = 0
    for row in data:
        treeview.insert('', i, text=str(i+1), values=(row[1], row[2]))
        i = i + 1

    treeview.pack()
    displayWindow.mainloop()

load_button = tk.Button(root, text="Load Data", command=lambda : load_data())
load_button.pack()

show_button = tk.Button(root, text="Show Data", command=lambda : show_data())
show_button.pack()

root.mainloop()


