import mysql.connector
import private
import pandas

class Budget:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user=private.USERNAME,
            password=private.PASSWORD,
            database = "budget"

        )
        print(self.mydb)
    def insert(self,data):
        cursor = self.mydb.cursor()
        # data = {
        #     "Year": year,
        #     "Month": month,
        #     "Day": day,
        #     "Category": category,
        #     "FoodGroup": food_group,
        #     "Price": price,
        #     "Quantity": quantity
        # }
        year = data["Year"]
        month = data["Month"]
        day = data["Day"]
        name = data["Name"]
        category = data["Category"]
        food_group = data["FoodGroup"]
        price = data["Price"]
        quantity = data["Quantity"]
        print(data)

        cursor.execute(f'insert into receipts (Year, Month, Day, Name, Category, FoodGroup, Price, Quantity)'
                       f' values(%s,%s,%s,%s,%s,%s,%s,%s)',
                       (year,month,day,name,category,food_group,price,quantity))
        self.mydb.commit()




if __name__ == "__main__":

    Budget()
