class Bisection():
  def __init__(self):
    self.low = 0 
    self.high = 10
    self.num_of_guess = 0
    self.answer = (self.low + self.high)/ 2

  def guess(self, number):
    if type(number) is str:
      return []
    while True:
      if self.answer == number:
        print(f'your number was {self.answer}')
        self.num_of_guess += 1
        return number
        break
      if self.answer < number:
        self.low = self.answer
      else: 
        self.high = self. answer
      self.answer = (self.low + self.high)/ 2

      self.num_of_guess += 1
      print(f'low = {self.low}, high= {self.high}, answer= {self.answer}, num_guess= {self.num_of_guess} ')

  
  
bisection = Bisection()
bisection.guess(4)