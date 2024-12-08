import unittest
import module_12_1
import module_12_2

New_test = unittest.TestSuite()
New_test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
New_test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(New_test)
