import runner
from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        Runner(name='jump')
        for i in range(10):
            runner.Runner.walk = 50
        self.assertEqual(Runner.walk, 50)

    def test_run(self):
        Runner(name='polo')
        for i in range(10):
            runner.Runner.run = 100
        self.assertEqual(Runner.run, 100)

    def test_chalenge(self):
        Runner(name='jump')
        Runner(name='polo')
        for i in range(10):
            runner.Runner.run = 100
            runner.Runner.walk = 50
        self.assertNotEqual(Runner.run, 300)
        self.assertNotEqual(Runner.walk, 400)


if __name__ == "__main__":
    unittest.main()
