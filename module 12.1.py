import unittest
import runner

class RunnerTest(unittest.TestCase):
    def test_walk(self, mark):
        x = runner.Runner.walk(10)
        self.assertEqual(runner.Runner.walk(10, 50))

    def test_run(self):
        pass

    def test_challenge(self):
        pass
