import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """
        Проверяем, чтобы длина наименования товара не больше 10 символов.
        В противном случае, обрезать строку (оставить первые 10 символов).

        """
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv

        """
        with open("../src/items.csv", "rt", encoding="windows-1251") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row["name"], row["price"], row["quantity"])

    @staticmethod
    def string_to_number(input_str: str):
        """
        Статический метод, возвращающий число из числа-строки

        :param input_str: Число-строка.
        :return: Число из числа-строки.
        """
        if "." in input_str:
            return int(float(input_str))
        else:
            return int(input_str)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    # def __str__(self):
    #     return f'Item = "{self.id_operation}" | date_operation="{self.date_operation}"'

    def __repr__(self):
        return f'Item (name="{self.name}", price="{self.price}", quantity="{self.quantity}")'

