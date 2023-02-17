from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def expense(self):
        pass


class Coat(Clothes):

    @property
    def expense(self):
        return round(self.param / 6.5 + 0.5, 2)


class Suit(Clothes):

    @property
    def expense(self):
        return round(self.param * 2 + 0.3, 2)


coat = Coat(48)
suit = Suit(1.75)
print(f'Расход ткани на пальто: {coat.expense}')
print(f'Расход ткани на костюм: {suit.expense}')
print(f'Общий расход ткани: {suit.expense + coat.expense}')
