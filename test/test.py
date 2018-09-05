import unittest


class TestAccuracy(unittest.TestCase):
    METRICS_FILE = "results/score.txt"

    def test_95percent_accuracy(self):    
        with open(self.METRICS_FILE, 'r') as file:
            error_score = float(file.read())

        self.assertLessEqual(error_score, 0.85)


if __name__ == "__main__":
    unittest.main()