import unittest


def two_sum_optimal(nums, target):
  addends = {}
  for i, num in enumerate(nums):
    complement = target - num
    if complement in addends:
      return [addends[complement], i]
    addends[num] = i
  return None


def two_sum_silly_brute_force(nums, target):
  for pizza in range(len(nums)):
    for bob in range(len(nums)):
      if pizza == bob:
        continue
      if nums[pizza] + nums[bob] == target:
        return [pizza, bob]
  return None


def two_sum_brute_force(nums, target):
  for i, num_i in enumerate(nums):
    for j, num_j in enumerate(nums):
      if i == j:
        continue
      if num_i + num_j == target:
        return [i, j]
  return None


class TestOpt(unittest.TestCase):

  def test_example1(self):
    nums = [2, 7, 11, 15]
    target = 9
    ans = [0, 1]
    self.assertCountEqual(two_sum_optimal(nums, target), ans)
    self.assertCountEqual(two_sum_brute_force(nums, target), ans)
    self.assertCountEqual(two_sum_silly_brute_force(nums, target), ans)

  def test_example2(self):
    nums = [3, 2, 4]
    target = 6
    ans = [1, 2]
    self.assertCountEqual(two_sum_optimal(nums, target), ans)
    self.assertCountEqual(two_sum_brute_force(nums, target), ans)
    self.assertCountEqual(two_sum_silly_brute_force(nums, target), ans)

  def test_example3(self):
    nums = [3, 3]
    target = 6
    ans = [0, 1]
    self.assertCountEqual(two_sum_optimal(nums, target), ans)
    self.assertCountEqual(two_sum_brute_force(nums, target), ans)
    self.assertCountEqual(two_sum_silly_brute_force(nums, target), ans)


if __name__ == '__main__':
  unittest.main()
