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
    np.testing.assert_array_equal(scrabble_score.yellows("smile", "stile"), np.array([1, 0, 1, 1, 1]),
                                  strict=True)
    np.testing.assert_array_equal(scrabble_score.yellows("smile", "miles"), np.array([1, 1, 1, 1, 1]),
                                  strict=True)

  def test_get_pattern(self):
    np.testing.assert_array_equal(scrabble_score.get_pattern("xxxxx", "xxxxx"), [2, 2, 2, 2, 2],
                                  strict=True)
    np.testing.assert_array_equal(scrabble_score.get_pattern("xxxxx", "yyyyy"), [0, 0, 0, 0, 0],
                                  strict=True)
    np.testing.assert_array_equal(scrabble_score.get_pattern("smile", "miles"), [1, 1, 1, 1, 1],
                                  strict=True)
    np.testing.assert_array_equal(scrabble_score.get_pattern("smile", "stile"), [2, 0, 2, 2, 2],
                                  strict=True)
    np.testing.assert_array_equal(scrabble_score.get_pattern("crane", "chain"), [2, 0, 2, 1, 0],
                                  strict=True)

  def test_get_pattern_repeated_letters(self):
    np.testing.assert_array_equal(scrabble_score.get_pattern("eeeee", "cheek"), [0, 0, 2, 2, 0],
                                  strict=True)
    np.testing.assert_array_equal(scrabble_score.get_pattern("speed", "abide"), [0, 0, 1, 0, 1],
                                  strict=True)
    np.testing.assert_array_equal(scrabble_score.get_pattern("speed", "steal"), [2, 0, 2, 0, 0],
                                  strict=True)
    np.testing.assert_array_equal(scrabble_score.get_pattern("speed", "crepe"), [0, 1, 2, 1, 0],
                                  strict=True)

  if __name__ == '__main__':
    unittest.main()
