
from pprint import pprint
import runner_and_tournamen
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls): #все результаты соревнований, переменная создается 1 раз в самом начале
        cls.all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self): #создаются участники тестирования каждый раз перед запуском тестов
        self.runner1 = runner_and_tournamen.Runner('Усэйн', speed= 10)
        self.runner2 = runner_and_tournamen.Runner('Андрей', speed= 9)
        self.runner3 = runner_and_tournamen.Runner('Ник', speed= 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def tearDown(self): # Запускается после любого тест-кейса
        pprint(self.all_results)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournamen1(self):
        tournamen1 = runner_and_tournamen.Tournament(90, self.runner1, self.runner3)

        results = tournamen1.start()
        pretty_results = {key: str(value) for key, value in results.items()}

        self.all_results.update(pretty_results)
        self.assertEqual(self.all_results[2], 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournamen2(self):
        tournamen2 = runner_and_tournamen.Tournament(90, self.runner2, self.runner3)

        results = tournamen2.start()
        pretty_results = {key: str(value) for key, value in results.items()}

        self.all_results.update(pretty_results)
        self.assertEqual(self.all_results[2], 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournamen3(self):
        tournamen3 = runner_and_tournamen.Tournament(90,self.runner1, self.runner2, self.runner3)

        results = tournamen3.start()
        pretty_results = {key: str(value) for key, value in results.items()}

        self.all_results.update(pretty_results)
        self.assertEqual(self.all_results[3], 'Ник')


if __name__ == '__main__':
    unittest.main()