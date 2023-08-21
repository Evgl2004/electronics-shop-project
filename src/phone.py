from src.item import Item


class Phone(Item):
    """
    Класс для представления телефонов в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if isinstance(number_of_sim, int) and number_of_sim > 0:
            self._number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self):
        return super().__repr__()[0:-1] + ", " + str(self.number_of_sim) + ")"
