"""Класс Neuron, в котором описывается структура нейрона и его метод"""


# Для создания объекта класса нужно передать ему веса каждого сенсора,
# количество сенсоров, и порог активации
class Neuron:
    def __init__(self, weights, n_sensor, porog):
        self.weights = weights
        self.n_sensor = n_sensor
        self.porog = porog

    # функция, которая будет распознавать число,
    # то есть умножать значение сенсора на его вес
    def proverka(self, num):
        summa = 0

        for i in range(self.n_sensor):
            summa += int(num[i]) * self.weights[i]
        if summa >= self.porog:
            print("Сумма сенсоров: ", summa)
            return True
        else:
            return False
