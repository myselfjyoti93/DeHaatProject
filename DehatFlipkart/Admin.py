from DehatFlipkart.Account import Account
import DehatFlipkart.Enums as Enums
import logging
from DehatFlipkart.Customer import Customer
from DehatFlipkart.SalesAgent import SalesAgent
from DehatFlipkart.Product import Product
import DehatFlipkart.Data as db


class Admin(Account):
  def __init__(self, user_name, password, role):
    self.logger = logging
    if role is not Enums.UserRoles.ADMIN:
      self.logger.ERROR("Not an Admin")
      return
    self.db = db
    self.db.UserList
    self.db.ProductList
    super().__init__(user_name, password, role)

  def create_users_for_roles(self, name, role, password = 0):
    if role is Enums.UserRoles.CUSTOMER:
      self.db.UserList.add_user(name, role, password)
      return Customer(name, Enums.UserRoles.CUSTOMER)
    elif role is Enums.UserRoles.SALES_AGENT:
      self.db.UserList.add_user(name, role, password)
      return SalesAgent(name, '', Enums.UserRoles.SALES_AGENT)

  def create_new_product(self, product_name, product_color, product_size, product_variant):
    self.db.ProductList.add_product(product_name, product_color, product_size, product_variant)
    return Product(product_name, product_color, product_size, product_variant)

  def update_product_count(self, product_name, product_count):
    self.db.ProductList.update_product(product_name, product_count, 0)

  def update_product_price(self, product_name, product_price):
    self.db.ProductList.update_product(product_name, 0, product_price)


