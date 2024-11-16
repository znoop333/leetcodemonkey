import unittest
import scrabble_score
import numpy as np


class TestAbsFunction(unittest.TestCase):
  def test_score(self):
    self.assertEqual(scrabble_score.score("word"), 8)

  def test_sort_by_score(self):
    self.assertEqual(scrabble_score.sort_by_score(["word", "zq", "xyzzy"]), [('word', 8), ('zq', 20), ('xyzzy', 36)])

  def test_greens(self):
    np.testing.assert_array_equal(scrabble_score.greens("smile", "stile"), np.array([True, False, True, True, True]),
                                  strict=True)

  def test_yellows(self):
    np.testing.assert_array_equal(scrabble_score.yellows("smile", "stile"), np.array([True, False, True, True, True]),
                                  strict=True)
    np.testing.assert_array_equal(scrabble_score.yellows("smile", "miles"), np.array([True, True, True, True, True]),
                                  strict=True)


if __name__ == '__main__':
  unittest.main()
