import unittest
from typing import List, Tuple


def two_sum_optimal(nums, target):
  addends = {}
  for i, num in enumerate(nums):
    complement = target - num
    if complement in addends:
      return [addends[complement], i]
    addends[num] = i
  return None


def two_sum_answer1(nums, target):
  for pizza in range(len(nums)):
    for bob in range(len(nums)):
      if nums[pizza] + nums[bob] == target:
        return [pizza, bob]


def two_sum_answer2(nums: List[int], target: int) -> Tuple:
  """ two_sum_answer2 solves the TwoSum problem using brute force
  :param nums: a list of integers in no particular order
  :param target: an arbitrary integer
  :return: (i, j) such that nums[i] + nums[j] == target
  """
  for i in range(len(nums)):
    for j in range(len(nums)):
      if nums[i] + nums[j] == target:
        return i, j
  return None


def two_sum_answer3(nums: List[int], target: int) -> Tuple:
  for i in range(len(nums)):
    for j in range(len(nums)):
      if i == j:
        # the problem statement said you may not use the same element twice
        continue
      if nums[i] + nums[j] == target:
        return i, j
  return None


class TestTwoSums(unittest.TestCase):
  def test_two_sum_answer2(self):
    self.assertCountEqual(two_sum_answer2([2, 7, 11, 15], 9), (0, 1))
    self.assertCountEqual(two_sum_answer2([3, 2, 4], 6), (1, 2))

  def test_example1(self):
    nums = [2, 7, 11, 15]
    target = 9
    ans = [0, 1]
    self.assertCountEqual(two_sum_optimal(nums, target), ans)
    self.assertCountEqual(two_sum_answer1(nums, target), ans)
    self.assertCountEqual(two_sum_answer2(nums, target), ans)

  def test_example2(self):
    nums = [3, 2, 4]
    target = 6
    ans = [1, 2]
    self.assertCountEqual(two_sum_optimal(nums, target), ans)
    self.assertCountEqual(two_sum_answer1(nums, target), ans)
    self.assertCountEqual(two_sum_answer2(nums, target), ans)

  def test_example3(self):
    nums = [3, 3]
    target = 6
    ans = [0, 1]
    self.assertCountEqual(two_sum_optimal(nums, target), ans)
    self.assertCountEqual(two_sum_answer1(nums, target), ans)
    self.assertCountEqual(two_sum_answer2(nums, target), ans)


if __name__ == '__main__':
  unittest.main()
