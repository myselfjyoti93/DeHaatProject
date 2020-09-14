from DehatFlipkart.Account import Account
import DehatFlipkart.Enums as Enums
import logging


class SalesAgent(Account):
  def __init__(self, user_name, password, role):
    self.logger = logging
    if role is not Enums.UserRoles.SALES_AGENT:
      self.logger.ERROR("Not an Sales Agent")
      return
    super().__init__(user_name, password, role)