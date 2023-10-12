class Segment1:
    """ Одномерный отрезок."""

    # инициализация объекта класса (конструктор объекта класса)
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish
        dist = self.length()
        self.dist = dist

    # метод
    def length(self):
        """ Возвращает длину отрезка """
        return self.finish - self.start
    
    def shift(self, dx):
        """ Сдвигает ЭТОТ отрезок на dx """
        # b.shift(2)
        self.start = self.start + dx
        self.finish += dx

a = Segment1(2, 10)      # 1) выделяется память, 2) расписать память данными (инициализация объекта)
b = Segment1(-6, 1)

d = a.length()      # Segment1.length(a)
print(f'Отрезок от {a.start} до {a.finish} длиной {d}')

d = b.length()
print(f'Отрезок от {b.start} до {b.finish} длиной {d}') # -6 1
b.shift(2)
print(f'Отрезок от {b.start} до {b.finish} длиной {d}') # -4 3
