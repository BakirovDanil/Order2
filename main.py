# Описание цифр
from Neuron import Neuron

num0 = list('111101101101111')
num1 = list('001001001001001')
num2 = list('111001111100111')
num3 = list('111001111001111')
num4 = list('101101111001001')
num5 = list('111100111001111')
num6 = list('111100111101111')
num7 = list('111001001001001')
num8 = list('111101111101111')
num9 = list('111101111001111')

# то, как может выглядеть цифра 6
num61 = list('111100011011111')
num62 = list('011100111101111')
num63 = list('111100110101111')
num64 = list('010100011011111')
num65 = list('010100110101111')
num66 = list('111100111101111')

tema = 6  # обучение цифре 6
n_sensor = 15  # количество сенсоров
porog = 11  # порог, для функции активации
weights = [1 for i in range(n_sensor)] # зададим веса каждого сенсора (пусть будет 1)

# создание объекта класса Neuron
neuron = Neuron(weights, n_sensor, porog)

print("Узнал 6 - 1? ", neuron.proverka(num61)) # вызов функции
print("Узнал 6 - 2? ", neuron.proverka(num62))
print("Узнал 6 - 3? ", neuron.proverka(num63))
print("Узнал 6 - 4? ", neuron.proverka(num64))
print("Узнал 6 - 5? ", neuron.proverka(num65))
print("Узнал 6 - 6? ", neuron.proverka(num66))
