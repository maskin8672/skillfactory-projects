from dots import Dot


class Ship:
    def __init__(self, bow_ship, len_ship, ship_orient):
        self.bow_ship = bow_ship
        self.len_ship = len_ship
        self.ship_orient = ship_orient
        self.ship_health = len_ship

    # Все точки корабля. Метод вычисляющий свойство корабля.
    @property
    def dots(self):
        ship_dots = []
        for i in range(self.len_ship):
            curr_x = self.bow_ship.x
            curr_y = self.bow_ship.y

            if self.ship_orient == 0:
                curr_x += i

            elif self.ship_orient == 1:
                curr_y += i

            ship_dots.append(Dot(curr_x, curr_y))

        return ship_dots

    def hit(self, shot):
        return shot in self.dots


# ship = Ship(bow_ship=Dot(1, 2), len_ship=4, ship_orient=0)
# print(ship.dots)
# print(ship.hit(Dot(2, 2)))
# print(ship.hit(Dot(2, 3)))
