from DehatFlipkart.Account import Account
import DehatFlipkart.Enums as Enums
import logging
import DehatFlipkart.Data as db


class Customer(Account):
  def __init__(self, user_name, role):
    self.logger = logging
    if role is not Enums.UserRoles.CUSTOMER:
      self.logger.ERROR("Not a Customer")
      return
    super().__init__(user_name, role)

  def view_products_for_sale(self):
    productList = db.get_all_products()
    for product in productList:
      print(product)