class Bisection():
  def __init__(self):
    self.low = 0 
    self.high = 10 
    self.answer = (self.low + self.high)/ 2

  def guess(self, number):
    if type(number) is str:
      return []
    while True:
      if self.answer == number:
        print(f'your number was {self.answer}')
        return number
        break
    