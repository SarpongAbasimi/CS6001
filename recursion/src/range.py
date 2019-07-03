class Range():
  
  def range_(self, user_input):
    if user_input is 0:
      return user_input
    else:
      print(user_input)
      self.range_(user_input -1)