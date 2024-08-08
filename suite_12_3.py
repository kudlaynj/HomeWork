import unittest
import test_12_2

rtt = unittest.TestSuite()
rtt.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.RunnerTest))
rtt.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.TournamentTest))

result = unittest.TextTestRunner(verbosity=2)
result.run(rtt)
