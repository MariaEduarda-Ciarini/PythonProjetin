from datetime import date


class Employees:
    def __init__(self, nome, birth_date, wage):
        self._nome = nome
        self._birth_date = birth_date
        self._wage = wage

    @property
    def nome(self):
        return self._nome

    @property
    def wage(self):
        return self._wage

    def idade(self):
        broken_date_birth = self._birth_date.split('/')
        year_nasci = broken_date_birth[-1]
        current_year = date.today().year
        return current_year - int(year_nasci)

    def surname(self):
        full_name = self.nome.strip()
        broken_name = full_name.split(' ')
        return broken_name[-1]

    def ey_parter(self):
        surnames = ['Vivaldi', 'Milgrau', 'Daleste', 'Uchiha', 'Haruno', 'Ibn-Alah', 'Mohamed']
        return (self.wage >= 100000) and (self.surname() in surnames)

    def salary_decrease(self):
        if self.ey_parter():
            decrease = self.wage * 0.1
            self._wage = self._wage - decrease

    def calculate_bonus(self):
        value = self._wage * 0.1
        if value > 1000:
            value = 0
        return value

    def __str__(self):
        return f'Employee({self._nome}, {self._birth_date}, {self._wage})'
