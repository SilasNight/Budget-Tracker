import mysql.connector
import private
import pandas

class Budget:
    def __init__(self):
        self.price = ""


    def insert(self,data):
        for item in data:
            if data[item] == "":
                raise ValueError #Please fill in all inputs
        test = int(data["Price"])
        test = int(data["Quantity"])
        database = self.connect_to()
        cursor = database.cursor()

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
        database.commit()
        cursor.close()
        database.close()

    def format_price(self, item):
        price = item
        if price[0] != "R":
            price = "R"+item
        if "." not in list(price):
            price = price+".00"
        return price
    def connect_to(self):
        db = mysql.connector.connect(
            host="localhost",
            user=private.USERNAME,
            password=private.PASSWORD,
            database="budget"
        )
        return db

    def load(self):
        db = self.connect_to()
        cursor = db.cursor()
        cursor.execute("select * from receipts")
        df = cursor.fetchall()
        cursor.close()
        db.close()

        return df

    def check_id(self,test):
        db = self.connect_to()
        cursor = db.cursor()
        cursor.execute("select * from receipts where id = %s", (test, ))
        output = cursor.fetchall()
        cursor.close()
        db.close()

        if len(output) != 0:
            return True
        else:
            return False

    def edit_info(self,target):
        db = self.connect_to()
        cursor = db.cursor()
        cursor.execute("select * from receipts where id = %s", (target, ))
        output = cursor.fetchall()[0]
        cursor.close()
        db.close()

        return output







if __name__ == "__main__":

    Budget().test()
