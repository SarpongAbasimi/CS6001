import os, sys, pytest
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path + '/../')

from src.bisection import Bisection

@pytest.fixture
def bisection():
  bisection = Bisection()
  return bisection

class TestBisection(object):

  def test_Bisection_properties(self, bisection):
    assert bisection.low == 0
    assert bisection.high == 10
    assert bisection.num_of_guess == 0
    assert bisection.answer == (bisection.low + bisection.high)/ 2
  
  def test_guess(self, bisection):
    number = 5
    assert bisection.guess(number) == bisection.answer
  
  def test_guess_returns_list_if_passed_string(self, bisection):
    number = 's'
    assert bisection.guess('s') == []
  
  def test_guess_prints_what_user_input(self, bisection, capsys):
    bisection.guess(5)
    output = capsys.readouterr()
    assert output.out == f'your number was {bisection.answer}\n'
    assert bisection.num_of_guess == 1
  
  
