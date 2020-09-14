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

  def create_users_for_roles(self, name, role):
    None

  def add_parking_spot(self, floor_name, spot):
    None

  def add_parking_display_board(self, floor_name, display_board):
    None

  def add_customer_info_panel(self, floor_name, info_panel):
    None

  def add_entrance_panel(self, entrance_panel):
    None

  def add_exit_panel(self, exit_panel):
    None