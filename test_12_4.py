import logging


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только числом, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        try:
            logging.info(f'{"test_run"} выполнен успешно')
            return self.distance + self.speed * 2
        except ValueError:
            logging.warning(f'"Неверный тип данных для объекта Runner"')

    def walk(self):
        try:
            logging.info(f'{"test_walk"} выполнен успешно')
            return self.distance + self.speed
        except ValueError:
            logging.warning(f'"Неверный скорость для Runner"')
            return 0

    def __str__(self):
        return self.name

    def __repr__(self):
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
                if participant.distance <= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

    if __name__ == '__main__':
        fileHandler = logging.FileHandler(filename='runner_tests.log', encoding='utf-8')
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        fileHandler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)


first = Runner('Вася', 10)
second = Runner(5)
third = Runner('Арсен', 12)

t = Tournament(101, first, second)
print(t.start())
