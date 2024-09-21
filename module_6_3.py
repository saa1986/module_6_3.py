class Horse:
    x_distance = 0  # Инициализация атрибута пройденного пути

    sound = 'Frrr'  # Инициализация атрибута звука лошади

    def run(self, dx):  # Метод движения лошади
        self.x_distance += dx  # Увеличение пройденного пути на dx


class Eagle:
    y_distance = 0  # Инициализация атрибута высоты полёта

    sound = 'I train, eat, sleep, and repeat'  # Инициализация атрибута звука орла

    def fly(self, dy):  # Метод полёта орла
        self.y_distance += dy  # Увеличение высоты полёта на dy


class Pegasus(Eagle, Horse):  # Наследование от Horse и Eagle
    def move(self, dx, dy):  # Метод перемещения пегаса
        super().run(dx)  # Вызов метода run родительского класса Horse
        super().fly(dy)  # Вызов метода fly родительского класса Eagle

    def get_pos(self):  # Метод для получения текущей позиции пегаса
        return self.x_distance, self.y_distance  # Возвращает кортеж (x_distance, y_distance)

    def voice(self):  # Метод для издания звука пегаса
        print(self.sound)  # Вывод звука пегаса


# Создание объекта класса Pegasus
p1 = Pegasus()

# Проверка работы методов
print(p1.get_pos())  # Вывод текущей позиции
p1.move(10, 15)  # Перемещение пегаса
print(p1.get_pos())  # Вывод новой позиции
p1.move(-5, 20)  # Перемещение пегаса
print(p1.get_pos())  # Вывод окончательной позиции

p1.voice()  # Издание звука пегаса