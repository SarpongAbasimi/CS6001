import os, sys, pytest
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path + '/../')

from src.range import Range

@pytest.fixture()
def new_range():
  new_range = Range()
  return new_range

class TestRange(object):

  def test_range_one(self, new_range):
    assert new_range.range_(0) == 0
  
  def test_range_two(self, new_range, capsys):
    new_range.range_(2)
    out = capsys.readouterr()
    assert out.out == '2\n1\n'
  
  def test_range_three(self, new_range, capsys):
    new_range.range_(5)
    out = capsys.readouterr()
    assert out.out == '5\n4\n3\n2\n1\n'
  
  def test_fib_one(self, new_range):
    assert new_range.fib(1)  == 1
  
  def test_fib_three(self, new_range):
    assert new_range.fib(3) == 2
  
  def test_fib_ten(self, new_range):
    assert new_range.fib(8) == 21
  
  def test_fib_15(self, new_range):
    assert new_range.fib(15) == 610

  def test_factorail(self, new_range):
    assert new_range.factorial(1) == 1
  
  def test_factorail_of_two(self, new_range):
    assert new_range.factorial(2) == 2
  