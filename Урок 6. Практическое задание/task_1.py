"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

import time
class TrafficLight:
    _color = None
    _colors = ['красный', 'жёлтый', 'зелёный']

    def __init__(self):
        self._color = self._colors[0]

    def running(self):
        i = 0
        while i < 3:
            for el in TrafficLight._colors :
                print(el)
                if el == 'красный':
                    time.sleep(7)
                if el == 'жёлтый':
                    time.sleep(2)
                if el == 'зелёный':
                    time.sleep(5)
                i += 1

traffic = TrafficLight()
traffic.running()
