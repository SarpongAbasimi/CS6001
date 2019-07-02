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
    assert bisection.answer == (bisection.low + bisection.high)/ 2
