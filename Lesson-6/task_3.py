class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return 'Полное имя сотрудника - {self.name} {self.surname}'

    def get_total_income(self):
        total_income = 0
        for key, value in self._income.items():
            total_income += value
        return 'Доход сотрудника равен {total_income}'


person_1 = Position('Иван', 'Иванов', 'разработчик', {'оклад': 50000, 'премия': 20000})
person_2 = Position('Алексей', 'Алексеев', 'ведущий разработчик', {'оклад': 50000, 'премия': 50000})
print(f'{person_1.get_full_name()}. {person_1.get_total_income()}')
print(f'{person_2.get_full_name()}. {person_2.get_total_income()}')
print(person_1.position)
print(person_2.position)
