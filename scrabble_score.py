import sys
import re
import random
import math
import numpy as np
from collections import Counter

_scrabble = {
  'd': 2,
  'g': 2,

  'b': 3,
  'c': 3,
  'm': 3,
  'p': 3,

  'f': 4,
  'h': 4,
  'v': 4,
  'w': 4,
  'y': 4,

  'k': 5,

  'j': 8,
  'x': 8,

  'q': 10,
  'z': 10,
}


def score(word: str) -> int:
  i = 0
  for c in word:
    c = c.lower().strip()
    i += _scrabble.get(c, 1)
  return i


def sort_by_score(words: list[str]) -> list:
  scored = [(w, score(w)) for w in words]
  scored.sort(key=lambda x: x[1])
  return scored


def letter_filters(s: str, must_exclude: str, must_include: str) -> bool:
  for c in must_exclude:
    if c in s:
      return False

  for c in must_include:
    if c not in s:
      return False

  return True


def filter_words(words: list[str]) -> list:
  filtered = []
  for w in words:
    w = w.strip()
    if not len(w) == 5:
      continue
    if not letter_filters(w, 'cntlms', 'are'):
      continue
    if not re.match(r'rea[^r][^e]', w):
      continue

    filtered.append(w)
  return filtered


def str2v(s: str) -> np.array:
  return np.array([ord(a) for a in s])


def v2str(a_vec: np.array) -> str:
  return ''.join([chr(n) for n in a_vec])


def greens(guess: str, answer: str) -> np.array:
  return np.array([g == a for (g, a) in zip(guess, answer)])


def yellows(guess: str, answer: str) -> np.array:
  c1 = Counter(answer)
  o = np.zeros((5,), dtype=int)
  for i, ch in enumerate(guess):
    x = c1.get(ch, 0)
    if x:
      c1[ch] -= 1
      o[i] = 1

  return o


def get_pattern(guess: str, answer: str) -> np.array:
  gr = greens(guess, answer)
  if np.any(gr):
    modified_answer = ''.join([answer[i] if not gr[i] else '_' for i, c in enumerate(gr)])
    modified_guess = ''.join([guess[i] if not gr[i] else '*' for i, c in enumerate(gr)])
  else:
    modified_answer = answer
    modified_guess = guess

  yw = yellows(modified_guess, modified_answer)
  pattern = yw
  pattern[gr] = 2

  return pattern


def compute_distribution(words_in_play: list[str], guess: str) -> np.array:
  distr = {}
  for w in words_in_play:
    p = get_pattern(guess, w)
    tp = tuple(p)
    if tp in distr:
      distr[tp].append(w)
    else:
      distr[tp] = [w]
  return distr


def calculate_entropy(distr: dict, n_words: int) -> float:
  h = 0
  for pattern, words in distr.items():
    prob = len(words) / n_words
    h += prob * (-math.log2(prob))

  return h


def play_game():
  # for reproducibility and debugging
  random.seed(1337)
  # https://github.com/dwyl/english-words  words_alpha.txt filtered to 5 letters
  input_filename = r'words_5letters.txt'
  with open(input_filename) as f:
    all_words = f.readlines()
  all_words = [w.strip() for w in all_words]
  max_words = min(2000, len(all_words))
  words_in_play = random.sample(all_words, max_words)
  random.shuffle(words_in_play)
  solution = random.sample(words_in_play, 1)

  print(f'Starting to play with solution {solution} among {max_words} (e.g., {words_in_play[:10]})')
  scrabble_scores = sort_by_score(words_in_play)

  for i_guess in range(5):
    guess = random.sample(words_in_play, 1)[0]
    while guess == solution:
      guess = random.sample(words_in_play, 1)[0]

    distribution = compute_distribution(words_in_play, guess)
    h = calculate_entropy(distribution, max_words)
    print(f'The entropy for guess {guess} was {h}')

  1


if __name__ == "__main__":
  play_game()

  """
  if len(sys.argv) > 1:
    with open(sys.argv[1]) as f:
      lines = f.readlines()
  else:
    lines = [l for l in sys.stdin]

  lines = filter_words(lines)

  print(sort_by_score(lines))
  """
