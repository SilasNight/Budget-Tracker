from tkinter import StringVar
import database_interface
import tkinter as tk
from tkinter import ttk
import datetime



class MainWindow:
    def __init__(self):
        self.months = "January, February, March, April, May, June, July, August, September, October, November, December".split(", ")
        food_groups = ("Fats, Oils and Sweets", "Milk, Yogurt and Cheese", "Meats, Eggs, Dry Beans and  Nuts",
                       "Vegetables", "Fruits", "Bread, Pasta, Cereal and Rice", "N/A")

        self.date = datetime.datetime.now().strftime("%d-%m-%Y")
        self.window = tk.Tk()
        date = StringVar()
        date.set(self.date)
        self.database = database_interface.Budget()
        self.window.config(padx=50,pady=50)
        self.main_canvas = tk.Canvas(self.window, bd=0, highlightthickness=0)
        self.back = tk.Button(self.main_canvas, text="Main Page", command= self.main_page,padx=3,pady=3)
        self.element_list = []

        #Main Page
        self.greeting = tk.Label(self.main_canvas, text="Time to add some data!")
        self.button_view = tk.Button(self.main_canvas, text= "View", command=self.view, width=20)
        self.button_add = tk.Button(self.main_canvas, text="Add", command=self.add_page, width=20)
        self.button_edit = tk.Button(self.main_canvas, text="Edit",command=self.index_selection, width=20)

        #Add Page
        self.date_label = tk.Label(self.main_canvas, text="Date (DD-MM-YYYY)",padx=3,pady=3)
        self.date_entry = tk.Entry(self.main_canvas, textvariable=date, width=35)
        self.product_name_label = tk.Label(self.main_canvas, text= "Product name",padx=3,pady=3)
        self.product_name_entry = tk.Entry(self.main_canvas, width=35)
        self.category_label = tk.Label(self.main_canvas, text="Type in the category.",padx=3,pady=3)
        self.category_entry = tk.Entry(self.main_canvas , width=35)
        self.food_group_label = tk.Label(self.main_canvas, text="Please type food group.",padx=3,pady=3)
        self.food_group_combo_text = StringVar()
        self.food_group_combo = ttk.Combobox(self.main_canvas, width=32,textvariable=self.food_group_combo_text)
        self.food_group_combo["values"] = food_groups
        self.price_label = tk.Label(self.main_canvas, text="What is the price? (Per Item)",padx=3,pady=3)
        self.price_entry = tk.Entry(self.main_canvas,  width=35)
        self.quantity_label = tk.Label(self.main_canvas, text="How many did you buy?",padx=3,pady=3)
        self.quantity_entry = tk.Entry(self.main_canvas,  width=35)
        self.insert_button = tk.Button(self.main_canvas, text="Insert", command=self.insert,padx=3,pady=3)


        #Index selection
        self.id_target = ""
        self.id_name_to_edit = tk.Label(self.main_canvas, text="Please choose which ID you would like to edit")
        self.id_entry = tk.Entry(self.main_canvas, )
        self.id_accept_button = tk.Button(self.main_canvas, text="Accept", command=self.accept_button)
        self.id_view_button = tk.Button(self.main_canvas,text="View",command=self.view)
        self.id_back_button = tk.Button(self.main_canvas,text="Main Page", command=self.main_page)



        #Edit Page
        self.date_label_edit = tk.Label(self.main_canvas, text="Date (DD-MM-YYYY)", padx=3, pady=3)
        self.date_entry_edit = tk.Entry(self.main_canvas, textvariable=date, width=35)
        self.product_name_label_edit = tk.Label(self.main_canvas, text="Product name", padx=3, pady=3)
        self.product_name_entry_edit = tk.Entry(self.main_canvas, width=35)
        self.category_label_edit = tk.Label(self.main_canvas, text="Type in the category.", padx=3, pady=3)
        self.category_entry_edit = tk.Entry(self.main_canvas, width=35)
        self.food_group_label_edit = tk.Label(self.main_canvas, text="Please type food group.", padx=3, pady=3)
        self.food_group_entry = tk.Entry(self.main_canvas, width=35)
        self.price_label_edit = tk.Label(self.main_canvas, text="What is the price? (Per Item)", padx=3, pady=3)
        self.price_entry_edit = tk.Entry(self.main_canvas, width=35)
        self.quantity_label_edit = tk.Label(self.main_canvas, text="How many did you buy?", padx=3, pady=3)
        self.quantity_entry_edit = tk.Entry(self.main_canvas, width=35)
        self.insert_button_edit = tk.Button(self.main_canvas, text="Insert", command=self.update, padx=3, pady=3)


        #View Page
        self.view_year_label = tk.Label(self.main_canvas,text= "Year")
        self.view_month_label = tk.Label(self.main_canvas,text= "Month")
        self.view_day_label = tk.Label(self.main_canvas,text= "Day")
        self.view_name_label = tk.Label(self.main_canvas,text= "Name")
        self.view_category_label = tk.Label(self.main_canvas,text= "Category")
        self.view_food_group_label = tk.Label(self.main_canvas,text= "Food Group")
        self.view_price_label = tk.Label(self.main_canvas,text= "Price")
        self.view_quantity_label = tk.Label(self.main_canvas,text= "Quantity")

        self.main_canvas.pack()

        self.main_page()
        self.window.mainloop()

    def view(self):
        self.clear()
        self.window.title("Viewing Data...")
        column = 0
        row = 1
        data = self.database.load()
        self.view_year_label.grid(column=1, row=0)
        self.view_month_label.grid(column=2, row=0)
        self.view_day_label.grid(column=3, row=0)
        self.view_name_label.grid(column=4, row=0)
        self.view_category_label.grid(column=5, row=0)
        self.view_food_group_label.grid(column=6, row=0)
        self.view_price_label.grid(column=7, row=0)
        self.view_quantity_label.grid(column=8, row=0)
        self.element_list = [self.view_year_label, self.view_month_label, self.view_day_label, self.view_name_label,
                             self.view_category_label, self.view_food_group_label, self.view_price_label,
                             self.view_quantity_label, self.back]
        for data_row in data:
            for data_column in data_row:
                if column == 2:
                    data_column = self.months[int(data_column)-1]
                variable_entry = tk.Label(self.main_canvas,text=data_column,borderwidth=1,relief="solid")
                self.element_list.append(variable_entry)
                variable_entry.grid(column=column, row=row, sticky="w"+"e")

                if column ==8:
                    column = 0
                else:
                    column+=1
            row+=1
        self.back.grid(column=column, row=row, sticky="w"+"e")

    def index_selection(self):
        self.clear()
        self.window.title("Select The ID of a entry to edit")
        self.id_name_to_edit.grid(column=0,row=0,columnspan=3)
        self.id_entry.grid(column=0,row=1,columnspan=3, sticky="w" + "e")
        self.id_accept_button.grid(column=1,row=2, sticky="w" + "e")
        self.id_back_button.grid(column=0,row=2, sticky="w" + "e")
        self.id_view_button.grid(column=2, row=2, sticky="w" + "e")
        self.element_list = [self.id_name_to_edit, self.id_entry,self.id_accept_button,self.id_back_button,
                             self.id_view_button]

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
        self.clear()
        self.window.title("Edit Entry")
        self.date_label_edit.grid(column=0,row=0)
        self.date_entry_edit.grid(column=1,row=0)
        self.product_name_label_edit.grid(column=0,row=1)
        self.product_name_entry_edit.grid(column=1,row=1)
        self.category_label_edit.grid(column=0,row=2)
        self.category_entry_edit.grid(column=1,row=2)
        self.food_group_label_edit.grid(column=0,row=3)
        self.food_group_entry.grid(column=1,row=3)
        self.price_label_edit.grid(column=0,row=4)
        self.price_entry_edit.grid(column=1,row=4)
        self.quantity_label_edit.grid(column=0,row=5)
        self.quantity_entry_edit.grid(column=1,row=5)
        self.back.grid(column=0, row=6)
        self.insert_button_edit.grid(column=1,row=6)
        self.get_edit_info(self.id_entry.get())
        self.element_list = [self.date_entry_edit, self.date_label_edit, self.product_name_label_edit,
                             self.product_name_entry_edit, self.category_label_edit, self.category_entry_edit,
                             self.food_group_label_edit, self.food_group_entry, self.price_label_edit,
                             self.price_entry_edit, self.quantity_label_edit, self.quantity_entry_edit,
                             self.insert_button_edit, self.back]

    def update(self):
        date = self.date_entry_edit.get()
        name = self.product_name_entry_edit.get()
        category = self.category_entry_edit.get()
        food_group = self.food_group_entry.get()
        price = self.price_entry_edit.get()
        quantity = self.quantity_entry_edit.get()

        day,month,year = date.split("-")
        output = [year, month, day, name, category, food_group, price, quantity]
        data = [self.id_target, output]
        self.database.edit_entry(data)


    def accept_button(self):
        target_id = self.id_entry.get()
        if self.database.check_id(test=target_id):
            self.edit()
            self.id_target = target_id
        else:
            self.window.title("Invalid ID!")

    def get_edit_info(self, test):
        data = self.database.edit_info(test)
        self.date_entry_edit.delete(0,tk.END)
        self.product_name_entry_edit.delete(0,tk.END)
        self.category_entry_edit.delete(0,tk.END)
        self.food_group_entry.delete(0,tk.END)
        self.price_entry_edit.delete(0,tk.END)
        self.quantity_entry_edit.delete(0,tk.END)

        year = data[1]
        month = data[2]
        day = data[3]
        name = data[4]
        category = data[5]
        food_group = data[6]
        price = data[7]
        quantity = data[8]
        date = f"{day}-{month}-{year}"

        self.date_entry_edit.insert(0, date)
        self.product_name_entry_edit.insert(0, name)
        self.category_entry_edit.insert(0, category)
        self.food_group_entry.insert(0, food_group)
        self.price_entry_edit.insert(0, price)
        self.quantity_entry_edit.insert(0, quantity)






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


    def insert(self):
        date = self.date_entry.get()
        day,month,year = date.split("-")
        name = self.product_name_entry.get().title()
        category = self.category_entry.get().title()
        food_group = self.food_group_combo_text.get()
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

        self.product_name_entry.delete(0,tk.END)
        self.category_entry.delete(0,tk.END)
        self.price_entry.delete(0,tk.END)
        self.quantity_entry.delete(0,tk.END)









def main():
    MainWindow()


main()