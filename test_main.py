import unittest
from main import GuessNumberGame

class TestGuessNumberGame(unittest.TestCase):
    def setUp(self):
        self.game = GuessNumberGame(5, 5)

    def test_correct_guess(self):
        self.assertEqual(self.game.guess(5), "Correct guess")

    def test_incorrect_guess(self):
        self.assertEqual(self.game.guess(4), "Incorrect guess")

    def test_no_attempts_left(self):
        for _ in range(5):
            self.game.guess(4)
        self.assertEqual(self.game.guess(5), "No attempts left")

if __name__ == "__main__":
    unittest.main()
