import rt_with_exceptions
import unittest
import logging


class RunnerTest(unittest.TestCase):
    logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log', encoding="UTF-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")

    def test_walk(self):
        try:
            runner_tested = rt_with_exceptions.Runner('Name', speed=-1)
            for i in range(0, 10):
                runner_tested.walk()
            self.assertEqual(runner_tested.distance, 50)
            logging.info(f"test_walk успешно выполнен!")
        except:
            logging.error("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            runner_tested = rt_with_exceptions.Runner(25)
            for i in range(0, 10):
                runner_tested.run()
            self.assertEqual(runner_tested.distance, 100)
            logging.info(f"test_run успешно выполнен!")
        except:
            logging.error("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        runner_tested1 = rt_with_exceptions.Runner('1')
        runner_tested2 = rt_with_exceptions.Runner('2')
        for i in range(0, 10):
            runner_tested1.run()
            runner_tested2.walk()
        self.assertNotEqual(runner_tested1.distance, runner_tested2.distance)


if __name__ == '__main__':
    unittest.main()

