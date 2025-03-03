from tkinter import StringVar

import database_interface
import tkinter as tk
from tkinter import ttk
import datetime



class MainWindow:
    def __init__(self):
        food_groups = ("Fats, Oils and Sweets", "Milk, Yogurt and Cheese", "Meats, Eggs, Dry Beans and  Nuts",
                       "Vegetables", "Fruits", "Bread, Pasta, Cereal and Rice", "N/A")
        self.date = datetime.datetime.now().strftime("%d-%m-%Y")
        self.window = tk.Tk()
        date = StringVar()
        date.set(self.date)
        self.database = database_interface.Budget()
        self.window.config(padx=50,pady=50)
        self.main_canvas = tk.Canvas(self.window)
        self.back = tk.Button(self.main_canvas, text="Back", command= self.main_page,padx=3,pady=3)
        self.element_list = []
        #Main Page
        self.greeting = tk.Label(self.main_canvas, text="Time to add some data!")
        self.button_view = tk.Button(self.main_canvas, text= "View", command=self.view, width=20)
        self.button_add = tk.Button(self.main_canvas, text="Add", command=self.add_page, width=20)
        self.button_edit = tk.Button(self.main_canvas, text="Edit",command=self.edit, width=20)
        #Add Page
        self.date_label = tk.Label(self.main_canvas, text="Date (DD-MM-YYYY)",padx=3,pady=3)
        self.date_entry = tk.Entry(self.main_canvas, textvariable=date, width=35)
        self.product_name_label = tk.Label(self.main_canvas, text= "Product name",padx=3,pady=3)
        self.product_name_entry = tk.Entry(self.main_canvas, width=35)
        self.category_label = tk.Label(self.main_canvas, text="Type in the category.",padx=3,pady=3)
        self.category_entry = tk.Entry(self.main_canvas , width=35)
        self.food_group_label = tk.Label(self.main_canvas, text="Please type food group.",padx=3,pady=3)
        self.food_group_combo = ttk.Combobox(self.main_canvas, width=32)
        self.food_group_combo["values"] = food_groups
        self.price_label = tk.Label(self.main_canvas, text="What is the price? (Per Item)",padx=3,pady=3)
        self.price_entry = tk.Entry(self.main_canvas,  width=35)
        self.quantity_label = tk.Label(self.main_canvas, text="How many did you buy?",padx=3,pady=3)
        self.quantity_entry = tk.Entry(self.main_canvas,  width=35)
        self.insert_button = tk.Button(self.main_canvas, text="Insert", command=self.insert,padx=3,pady=3)






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
        self.product_name_label.grid(column=0, row=1, sticky="w")
        self.product_name_entry.grid(column=1, row=1)
        self.category_label.grid(column=0, row=2, sticky="w")
        self.category_entry.grid(column=1, row=2)
        self.food_group_label.grid(column=0, row=3, sticky="w")
        self.food_group_combo.grid(column=1, row=3)
        self.price_label.grid(column=0, row=4, sticky="w")
        self.price_entry.grid(column=1, row=4)
        self.quantity_label.grid(column=0, row=5, sticky="w")
        self.quantity_entry.grid(column=1, row=5)
        self.back.grid(column=0, row=6, sticky="w"+"e")
        self.insert_button.grid(column=1, row=6, sticky="w"+"e")



        self.element_list = [self.date_label, self.date_entry, self.category_label, self.category_entry,
                             self.food_group_label, self.food_group_combo, self.price_label, self.price_entry,
                             self.quantity_label, self.quantity_entry, self.back, self.insert_button,
                             self.product_name_entry,self.product_name_label]

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

    def check(self):
        pass

    def insert(self):
        date = self.date_entry.get()
        day,month,year = date.split("-")
        name = self.product_name_entry.get()
        category = self.category_entry.get()
        food_group = self.food_group_combo.current()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        data = {
            "Year" : year,
            "Month" : month,
            "Day" : day,
            "Name" : name,
            "Category" : category,
            "FoodGroup" : food_group,
            "Price" : price,
            "Quantity" : quantity
        }

        self.database.insert(data=data)









def main():
    MainWindow()


main()