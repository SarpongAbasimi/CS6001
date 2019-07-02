class Bisection():
  def __init__(self, high=10):
    self.low = 0 
    self.high = high
    self.num_of_guess = 0
    self.answer = (self.low + self.high)/ 2

  def guess(self, number):
    if type(number) is str:
      return []
    while True:
      if self.answer == number:
        return self.perfect_guess(number)
        break
      self.less(number) if self.answer < number else self.more(number)
      self.answer = (self.low + self.high)/ 2
      self.num_of_guess += 1
      
      print(f'low = {self.low}, high= {self.high}, answer= {self.answer}, num_guess= {self.num_of_guess} ')
  
  def perfect_guess(self, number):
    print(f'your number was {self.answer}')
    self.num_of_guess += 1
    return number
  
  def less(self, number):
    self.low = self.answer
  
  def more(self, number):
    self.high = self. answer
