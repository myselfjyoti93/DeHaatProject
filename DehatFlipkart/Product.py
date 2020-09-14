class Product:
  def __init__(self, product_name, product_color, product_size, product_variant):
    self.__product_name = product_name
    self.__product_name = product_color
    self.__product_name = product_size
    self.__product_variant = product_variant
    self.__product_price = 0
    self.__product_count = 0

  def update_product_price(self, price):
      self.__product_price = price

  def get_product_price(self, name):
      return self.__product_price

  def update_product_count(self, count):
      self.__product_count = count

  def get_product_count(self, name):
      return self.__product_count