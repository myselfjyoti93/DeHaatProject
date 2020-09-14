class Account:
  def __init__(self, user_name, password, role):
    self.__user_name = user_name
    self.__password = password
    self.__role = role

  def reset_password(self):
    None