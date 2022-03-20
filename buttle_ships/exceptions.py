# Родительский класс исключений позволяет отлавливать все дочерние исключения.

class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за доску!"


class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"


# Исключение не для пользователя
class BoardWrongShipException(BoardException):
    pass
