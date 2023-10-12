class Bag:
    pass

b1 = Bag()
qqq = Bag()

b1.money = 100
b1.book = 'Общая физика'
print(b1.money, b1.book)
print(b1)

qqq.money = 50
qqq.food = 'apple'
qqq.book = 'Унесенные ветром'

qqq.money += 200
print(qqq.money)
