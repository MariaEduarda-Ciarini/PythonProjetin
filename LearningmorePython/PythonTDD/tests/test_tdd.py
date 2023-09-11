from employees import Employees

class TestClass:
    def test_when_age_receives_15_04_1452_deve_retornar_571(self):
        entrada = '15/04/1452'  # Given - context
        esperado = 571

        employee_test = Employees('LdVinci', entrada, 2500)
        resultado = employee_test.idade()  # When - action

        assert resultado == esperado  # Then - outcome

    def test_when_last_name_receives_Leonardo_dVinci_it_must_return_dVinci(self):
        entrada = 'Leonardo dVinci'  # Given - context
        esperado = 'dVinci'

        vincipi = Employees(entrada, '15/04/1452', 5000)
        resultado = vincipi.surname()  # When - action

        assert resultado == esperado  # Then - outcome


def test_when_salary_decrease_receives100000_must_return_90000():
    entrada_salary = 100000  # Give - context
    entrada_nome = 'Antonio Vivaldi'
    esperado = 90000

    employee_test = Employees(entrada_nome, '04/03/1678', entrada_salary)
    employee_test.salary_decrease()
    resultado = employee_test.wage  # When - action

    assert resultado == esperado, f"Esperado {esperado}, mas obteve {resultado}"  # Then - result


def test_when_calculating_bonus_receive_1300_must_return_100():
    entrada = 1000  # Given - context
    esperado = 100

    employee_test = Employees('teste', '03/04/1999', entrada)
    resultado = employee_test.calculate_bonus()  # When - action

    assert resultado == esperado  # Then - outcome

