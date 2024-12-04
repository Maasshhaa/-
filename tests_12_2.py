"""
ТЕСТИРУЕМЫЙ КОД
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
"""
from pprint import pprint
import runner_and_tournamen
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls): #все результаты соревнований, переменная создается 1 раз в самом начале
        cls.all_results = {}

    def setUp(self): #создаются участники тестирования каждый раз перед запуском тестов
        self.runner1 = runner_and_tournamen.Runner('Усэйн', speed= 10)
        self.runner2 = runner_and_tournamen.Runner('Андрей', speed= 9)
        self.runner3 = runner_and_tournamen.Runner('Ник', speed= 3)

    def tearDown(self): # Запускается после любого тест-кейса
        pprint(self.all_results)


    def test_tournamen1(self):
        tournamen1 = runner_and_tournamen.Tournament(90, self.runner1, self.runner3)

        results = tournamen1.start()
        pretty_results = {key: str(value) for key, value in results.items()}

        self.all_results.update(pretty_results)
        self.assertEqual(self.all_results[2], 'Ник')


    def test_tournamen2(self):
        tournamen2 = runner_and_tournamen.Tournament(90, self.runner2, self.runner3)

        results = tournamen2.start()
        pretty_results = {key: str(value) for key, value in results.items()}

        self.all_results.update(pretty_results)
        self.assertEqual(self.all_results[2], 'Ник')


    def test_tournamen3(self):
        tournamen3 = runner_and_tournamen.Tournament(90,self.runner1, self.runner2, self.runner3)

        results = tournamen3.start()
        pretty_results = {key: str(value) for key, value in results.items()}

        self.all_results.update(pretty_results)
        self.assertEqual(self.all_results[3], 'Ник')


if __name__ == '__main__':
    unittest.main()