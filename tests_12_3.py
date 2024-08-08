import runner_and_tournament
from runner_and_tournament import Runner, Tournament
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        Runner(name='Андрей')
        for i in range(10):
            runner_and_tournament.Runner.walk = 50
        self.assertEqual(Runner.walk, 50)

    def test_run(self):
        Runner(name='Усэйн')
        for i in range(10):
            runner_and_tournament.Runner.run = 100
        self.assertEqual(Runner.run, 100)

    def test_chalenge(self):
        Runner(name='Андрей')
        Runner(name='Ник')
        for i in range(10):
            runner_and_tournament.Runner.run = 100
            runner_and_tournament.Runner.walk = 50
        self.assertNotEqual(Runner.run, 300)
        self.assertNotEqual(Runner.walk, 400)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def setUpClass(self):
        self.all_finishers = {}
        print(self.all_finishers)

    def setUp(self):
        self.runer_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runer_2 = runner_and_tournament.Runner('Андрей', 9)
        self.runer_3 = runner_and_tournament.Runner('Ник', 3)

    def tearDownClass(self):
        for i in self.all_finishers:
            print(i)

    def race_1_test(self):
        race_1 = runner_and_tournament.Tournament(90, self.runer_1, self.runer_3)
        result = race_1.start()
        print(result[list(result.keys())[-1]] == 'Ник')
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Error!')
        self.all_finishers[1] = result
        self.assertEqual(Tournament.start, 90)

    def race_2_test(self):
        race_2 = runner_and_tournament.Tournament(90, self.runer_2, self.runer_3)
        result = race_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Error!')
        self.all_finishers[2] = result
        self.assertEqual(Tournament.start, 90)

    def race_3_test(self):
        race_3 = runner_and_tournament.Tournament(90, self.runer_1, self.runer_2, self.runer_3)
        result = race_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Error!')
        self.all_finishers[3] = result
        self.assertEqual(Tournament.start, 90)

    if __name__ == "__main__":
        unittest.main()
