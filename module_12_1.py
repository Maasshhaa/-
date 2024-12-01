"""
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name
"""

import runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner_tested = runner.Runner('Name')
        for i in range(0, 10):
            runner_tested.walk()
        self.assertEqual(runner_tested.distance, 50)

    def test_run(self):
        runner_tested = runner.Runner('Name')
        for i in range(0, 10):
            runner_tested.run()
        self.assertEqual(runner_tested.distance, 100)

    def test_challenge(self):
        runner_tested1 = runner.Runner('1')
        runner_tested2 = runner.Runner('2')
        for i in range(0, 10):
            runner_tested1.run()
            runner_tested2.walk()
        self.assertNotEqual(runner_tested1.distance, runner_tested2.distance)


if __name__ == '__main__':
    unittest.main()




