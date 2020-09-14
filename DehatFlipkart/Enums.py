from enum import Enum


class ProductStockLevel(Enum):
    AVAILABLE, UNAVAILABLE = 0, 1


class ProductStatusForSelling(Enum):
    ELIGIBLE, INELIGIBLE = 0, 1


class ProductColor(Enum):
    RED, BLUE = 1, 2


class ProductSize(Enum):
    INCH13, INCH14 = 1, 2


class ProductVariant(Enum):
    V140 = 1


class OrderStatus(Enum):
    ACCEPTED, DELIVERED, CANCELLED = 1, 2, 3


class UserRoles(Enum):
    ADMIN, CUSTOMER, SALES_AGENT = 1, 2, 3




"""
class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country


class Person():
    def __init__(self, name, address, email, phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone

"""