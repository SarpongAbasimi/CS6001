class Range():
  
  def range_(self, user_input):
    if user_input is 0:
      return user_input
    else:
      print(user_input)
      self.range_(user_input -1)
  
  def fib(self, user_input):
    if user_input == 1:
      return 1
    elif user_input == 2:
      return 1
    else:
      return(self.fib(user_input - 1) + self.fib(user_input - 2))