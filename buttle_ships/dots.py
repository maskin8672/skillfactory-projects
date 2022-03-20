class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Сделаем рабочими с нашими объектами методы списков
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Возвращает объект в "официальном" представлении
    # В последующем объект можно реконструировать
    # с помощью функции eval
    def __repr__(self):
        return f"Dot(x={self.x}, y={self.y})"


# DEBUG TEST:
# a = Dot(1, 1)
# b = Dot(3, 2)
# c = Dot(1, 1)
#
# print(a == c)
#
# list_dots = [Dot(1, 1), Dot(3, 4)]
# print(a in list_dots)
# print(list_dots.count(a))
