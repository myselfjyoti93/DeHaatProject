import csv
from DehatFlipkart.Product import Product


class ProductList:
    def __init__(self):
        data_list = [["Name", "Colour", "Size", "Variant", "Price", "Count"]]
        with open('products.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerows(data_list)

    def add_product(self, name, color, size, variant, price=0, count=0):
        data_list = [[name, color, size, variant, price, count]]
        with open('products.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerows(data_list)

    def update_product(self, name, count=0, price=0):
        r = csv.reader(open('products.csv'))  # Here your csv file
        lines = list(r)
        for row in lines:
            if row[0] == name:
                if count is not 0:
                    row[5] = count
                if price is not 0:
                    row[4] = price


    def get_product(self, name):
        product = []
        r = csv.reader(open('products.csv'))  # Here your csv file
        lines = list(r)
        for row in lines:
            if row[0] == name:
                product = [row[0], row[1], row[2], row[3], row[4], row[5]]



class UserList:
    def __init__(self):
        data_list = [["SN", "Name", "Role", "Password"]]
        with open('user.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerows(data_list)


    def add_user(self, name, role, password=0):
        data_list = [[name, role, password]]
        with open('user.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerows(data_list)
