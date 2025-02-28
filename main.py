from tkinter import StringVar

import mysql.connector
import tkinter as tk
import datetime

class MainWindow:
    def __init__(self):
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.window = tk.Tk()
        date = StringVar()
        date.set(self.date)
        self.window.config(padx=50,pady=50)
        self.main_canvas = tk.Canvas(self.window)
        self.back = tk.Button(self.main_canvas, text="Back", command= self.main_page)
        self.element_list = []
        #Main Page
        self.greeting = tk.Label(self.main_canvas, text="Time to add some data!")
        self.button_view = tk.Button(self.main_canvas, text= "View", command=self.view, width=20)
        self.button_add = tk.Button(self.main_canvas, text="Add", command=self.add_page, width=20)
        self.button_edit = tk.Button(self.main_canvas, text="Edit",command=self.edit, width=20)
        #Add Page
        self.date_label = tk.Label(self.main_canvas, text="Date (DD-MM-YYYY)")
        self.date_entry = tk.Entry(self.main_canvas, textvariable=date)
        self.category_label = tk.Label(self.main_canvas, text="Type in the category.")
        self.category_entry = tk.Entry(self.main_canvas, )
        self.food_group_label = tk.Label(self.main_canvas, text="Please type food group.")
        self.food_group_entry = tk.Entry(self.main_canvas, )
        self.price_label = tk.Label(self.main_canvas, text="What is the price? (Per Item)")
        self.price_entry = tk.Entry(self.main_canvas, )
        self.quantity_label = tk.Label(self.main_canvas, text="How many did you buy?")
        self.quantity_entry = tk.Entry(self.main_canvas, )



        #Edit Page
        #View Page






        self.main_canvas.pack()



        print("me")
        self.main_page()
        self.window.mainloop()

    def view(self):
        pass

    def add_page(self):
        self.clear()
        self.window.title("Adding Data...")
        self.date_label.grid(column=0, row=0, sticky="w")
        self.date_entry.grid(column=1, row=0)
        self.category_label.grid(column=0, row=1, sticky="w")
        self.category_entry.grid(column=1, row=1)
        self.food_group_label.grid(column=0, row=2, sticky="w")
        self.food_group_entry.grid(column=1, row=2)
        self.price_label.grid(column=0, row=3, sticky="w")
        self.price_entry.grid(column=1, row=3)
        self.quantity_label.grid(column=0, row=4, sticky="w")
        self.quantity_entry.grid(column=1, row=4)
        self.back.grid(column=0, row=5, sticky="w")



        self.element_list = [self.date_label, self.date_entry, self.category_label, self.category_entry,
                             self.food_group_label, self.food_group_entry, self.price_label, self.price_entry,
                             self.quantity_label, self.quantity_entry, self.back]

    def edit(self):
        pass

    def main_page(self):
        self.clear()
        self.window.title("Budget Tracker")
        self.greeting.grid(column=0, row=0, columnspan=3, sticky="w" + "e")
        self.button_add.grid(column=0, row=1, sticky="w" + "e")
        self.button_edit.grid(column=1, row=1, sticky="w" + "e")
        self.button_view.grid(column=2, row=1, sticky="w" + "e")
        self.element_list = [self.greeting,self.button_add,self.button_edit,self.button_view]

    def clear(self):
        for item in self.element_list:
            item.grid_remove()
        self.element_list = []





def main():
    MainWindow()


main()