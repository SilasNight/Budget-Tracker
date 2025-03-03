import mysql.connector
import private
import pandas

class Budget:
    def __init__(self):
        self.price = ""
        self.mydb = mysql.connector.connect(
            host="localhost",
            user=private.USERNAME,
            password=private.PASSWORD,
            database = "budget"

        )
        print(self.mydb)
    def insert(self,data):
        for item in data:
            if data[item] == "":
                raise ValueError #Please fill in all inputs

        cursor = self.mydb.cursor()

        year = data["Year"]
        month = data["Month"]
        day = data["Day"]
        name = data["Name"]
        category = data["Category"]
        food_group = data["FoodGroup"]
        price = self.format_price(data["Price"])
        quantity = data["Quantity"]


        cursor.execute(f'insert into receipts (Year, Month, Day, Name, Category, FoodGroup, Price, Quantity)'
                       f' values(%s,%s,%s,%s,%s,%s,%s,%s)',
                       (year,month,day,name,category,food_group,price,quantity))
        self.mydb.commit()

    def format_price(self, item):
        price = item
        if price[0] == "R":
            price = "R"+item
        if "." not in list(price):
            price = price+".00"
        return price




if __name__ == "__main__":

    Budget()
