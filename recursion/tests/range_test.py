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

