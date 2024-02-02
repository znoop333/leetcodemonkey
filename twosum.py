import unittest


def two_sum_optimal(nums, target):
  addends = {}
  for i, num in enumerate(nums):
    complement = target - num
    if complement in addends:
      return [addends[complement], i]
    addends[num] = i
  return None


class TestOpt(unittest.TestCase):

  def test_example1(self):
    nums = [2, 7, 11, 15]
    target = 9
    self.assertEqual(two_sum_optimal(nums, target), [0, 1])

  def test_example2(self):
    nums = [3, 2, 4]
    target = 6
    self.assertEqual(two_sum_optimal(nums, target), [1, 2])

  def test_example3(self):
    nums = [3, 3]
    target = 6
    self.assertEqual(two_sum_optimal(nums, target), [0, 1])


if __name__ == '__main__':
  unittest.main()
