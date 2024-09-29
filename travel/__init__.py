import check50
import check50.c

@check50.check()
def exists():
    """travel_expenses.c exists"""
    check50.exists("travel_expenses.c")

@check50.check(exists)
def compiles():
    """travel_expenses.c compiles"""
    check50.c.compile("travel_expenses.c", lcs50=True)

@check50.check(compiles)
def test_total_expenses_3_days():
    """Проверяет расчет общей суммы расходов за 3 дня."""
    check_expenses(type="T", data=[100, 150, 200], expected="450.0")

@check50.check(compiles)
def test_average_expenses_4_days():
    """Проверяет расчет среднего расхода за день для 4 дней."""
    check_expenses(type="A", data=[50, 60, 70, 80], expected="65.0")


# Вспомогательная функция для проверки расходов
def check_expenses(type: str, data: list, expected: str):
    program = check50.run("./travel_expenses").stdin(str(len(data)))
    for i, expense in enumerate(data):
        program.stdin(str(expense))
    program.stdin(type).stdout(expected)