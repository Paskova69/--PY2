import doctest


class Drill:
    def __init__(self, rotation_speed: int, drill_on=False):
        """
        Создание и подготовка к работе объекта "Дрель"

        :param rotation_speed: Частота вращения, доступная при безопасной работе с дрелью
        :param drill_on: Состояние дрели (Включена/Выключена). По умолчанию выключена

        Пример:
        >>> drill = Drill(1200, True)  # Дрель включена
        >>> drill = Drill(1000)  # Дрель выключена
        """
        if not isinstance(rotation_speed, int):
            raise TypeError("Значение для числа вращения сверла должно быть типа int")
        if rotation_speed <= 0:
            raise ValueError("Значение для числа вращения сверла должно быть положительным числом")
        self.rotation_speed = rotation_speed

        if not isinstance(drill_on, bool):
            raise TypeError("Показатель состояния дрели должен быть типа bool")
        self.drill_on = drill_on

    def status_of_drill(self, status: bool) -> None:
        """
        Функция, которая изменяет состояние дрели: включена/выключена: True - дрель включена, False - дрель выключена

        :param status: Желаемое состояние дрели

        :raise TypeError: Функция, которая задает состояние дрели, должна быть типа bool

        :return: Новое состояние дрели

        Пример:
        >>> drill = Drill(1300, True)
        >>> drill.status_of_drill(False)  # Выключаем дрель
        """
        if not isinstance(status, bool):
            raise TypeError("Функция, которая задает состояние дрели, должна быть типа bool")
        ...

    def set_speed(self, speed: int) -> None:
        """
        Функция, которая включает желаемую частоту вращения сверла

        :param speed: Частота вращения сверла

        :raise ValueError: Значение частоты вращения превышает максимально возможную частоту на этом устройстве
        :raise TypeError: Функция задания частоты вызывается при выключенной дрели

        :return: Новое значение частоты вращения

        Пример:
        >>> drill = Drill(1300,True)
        >>> drill.set_speed(500)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()


class Mouse:
    def __init__(self, dpi: int, number_of_buttons: int, backlight=False):
        """
        Создание и подготовка к работе объекта "Компьютерная мышь"

        :param dpi: Разрешение датчика, лежит в пределах 200-12000 dpi
        :param number_of_buttons: Количество функциональных кнопок. Изначально количество - 6, добавить можно еще 4
        :param backlight: Наличие подсветки

        Пример:
        >>> mouse1 = Mouse(400, 6, True)
        """
        if not isinstance(dpi, int):
            raise TypeError("Разрешение датчика должно быть типа int")
        if (dpi < 200) or (dpi > 12000):
            raise ValueError("Разрешение датчика лежит в пределах 200-12000 dpi")
        self.dpi = dpi

        if not isinstance(number_of_buttons, int):
             raise TypeError("Количество функциональных кнопок мышки должно быть типа int")
        if (number_of_buttons < 6) or (number_of_buttons > 10):
            raise ValueError("Количество функциональных кнопок мышки не может быть меньше 6 или больше 10")
        self.numbers_of_buttons = number_of_buttons

        if not isinstance(backlight, bool):
            raise TypeError("Показатель наличия подстветки должен быть типа bool")
        self.backlight = backlight

    def backlight_check(self) -> None:
        """
        Функция, которая проверяет наличие подсветки у мышки

        :return: Светится ли подсветка у мышки

        Пример:
        >>> mouse1 = Mouse(400, 6, True)
        >>> mouse1.backlight_check()
        """
        ...

    def add_buttons(self, added_buttons: int) -> int:
        """
        Функция добавления функциональных кнопок мышки

        :param added_buttons: Число добавленных кнопок

        :raise ValueError: Если количество изначально заданных кнопок, вместе с количеством добавленных превышает 10, вызываетсяэта ошибка
        :raise TypeError: Число добавленных кнопок должно быть типа int

        :return: Новое значение функциональных кнопок

        Пример:
        >>> mouse1 = Mouse(400, 6, True)
        >>> mouse1.add_buttons(3)  # На выходе получится 9 кнопок
            """
        if not isinstance(added_buttons, int):
            raise TypeError("Число добавленных кнопок должно быть типа int")
        ...


class XmasTree:
    def __init__(self, height: int, xmas_decorations):
        """
        Создание и подготовка к работе объекта "Новогодняя ель"

        :param height: Высота ели в см
        :param xmas_decorations: Количество игрушек либо их отсутствие

        Пример:
        >>> xmas_tree = XmasTree(180, False)  # Высота елки 180 см, не украшена
        """
        if not isinstance(height, int):
            raise TypeError("Высота елки должна быть типа int")
        if height <= 0:
            raise ValueError("Высота елки должна быть положительным числом")
        self.hetght = height

        if not isinstance(xmas_decorations, int | None):
            raise TypeError("Количество новогодних украшений должно быть типа int, в случае их отсутствия - None")
        self.xmas_decorations = xmas_decorations

    def opportunity_of_decoration_with_star(self, height_of_person: int) -> bool:
        """
        Функция, которая проверяет, может ли человек установить звезду на вершну ели

        :param height_of_person: Рост человека

        :raise TypeError: Рост человека должен быть типа int

        :return: Сможет ли человек установить звезду

        Пример:
        >>> xmas_tree = XmasTree(180, False)
        >>> xmas_tree.opportunity_of_decoration_with_star(150)  # True (учитывается высота руки человека примерно 40 см)
        """
        if not isinstance(height_of_person, int):
            raise TypeError("Рост человека должен быть типа int")
        ...

    def is_the_tree_decorated(self) -> bool:
        """
        Функция, которая определяет, украшена ли елка

        :return: Украшена ли ель

        Пример:
        >>> xmas_tree = XmasTree(180,20)
         >>> xmas_tree.is_the_tree_decorated()  # True, елка украшена
        """
        ...