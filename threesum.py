import unittest
from typing import List, Tuple


def three_sum_answer1(nums: List[int]) -> List[Tuple[int]]:
  """ three_sum_answer1 solves the ThreeSum problem using brute force
  :param nums: a list of integers in no particular order
  :return: a list of elements of nums such that nums[i] + nums[j] + nums[k] == 0
    and i != j != k. No duplicates of (nums[i], nums[j], nums[k]) are allowed.
  """
  solutions = set()
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      for k in range(j + 1, len(nums)):
        if nums[i] + nums[j] + nums[k] == 0:
          t = sorted((nums[i], nums[j], nums[k]))
          solutions.add(tuple(t))
  return list(solutions)


class TestThreeSums(unittest.TestCase):
  def test_two_sum_answer1(self):
    self.assertCountEqual(three_sum_answer1([0, 1, 1]), [])
    self.assertCountEqual(three_sum_answer1([-1, 0, 1, 2, -1, -4]), [(-1, -1, 2), (-1, 0, 1)])


if __name__ == '__main__':
  unittest.main()
