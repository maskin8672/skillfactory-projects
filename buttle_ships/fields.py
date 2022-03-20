from dots import Dot
from ships import Ship
from exceptions import BoardOutException, BoardUsedException, BoardWrongShipException


class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid
        # Кол-во поражённых кораблей
        self.count = 0
        # Сетка игрового поля, где храним состояние поля
        self.field = [["0"] * size for _ in range(size)]
        # Занятые точки (корабли и выстрелы)
        self.busy = []
        # Список кораблей на доске
        self.ships = []

    # Отображаем игровое поле
    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("▨", "0")
        return res

    # Проверяем выход за пределы игрового поля
    def out(self, dot):
        return not ((0 <= dot.x < self.size) and (0 <= dot.y < self.size))

    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for dot in ship.dots:
            for dotx, doty in near:
                cur = Dot(dot.x + dotx, dot.y + doty)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)

    def add_ship(self, ship):
        for dot in ship.dots:
            if self.out(dot) or dot in self.busy:
                raise BoardWrongShipException()
        for dot in ship.dots:
            self.field[dot.x][dot.y] = "▨"
            self.busy.append(dot)

        self.ships.append(ship)
        self.contour(ship)

    def shot(self, dot):
        if self.out(dot):
            raise BoardOutException()

        if dot in self.busy:
            raise BoardUsedException()

        self.busy.append(dot)

        for ship in self.ships:
            if dot in ship.dots:
                ship.ship_health -= 1
                self.field[dot.x][dot.y] = "x"
                if ship.ship_health == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[dot.x][dot.y] = "."
        print("Мимо!")
        return False

    def begin(self):
        self.busy = []

# board = Board()
# board.add_ship(Ship(Dot(1, 2), 4, 0))
# board.add_ship(Ship(Dot(0, 0), 1, 0))
# print(board)
# print(board.busy)
