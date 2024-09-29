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
def total_3_days():
    """travel_expenses calculates total expenses over 3 days."""
    check_expenses(type="T", data=[50, 80, 120], expected="250.0")

@check50.check(compiles)
def total_4_days():
    """travel_expenses calculates total expenses over 4 days."""
    check_expenses(type="T", data=[100, 75, 90, 60], expected="325.0")

@check50.check(compiles)
def average_3_days():
    """travel_expenses calculates average expenses over 3 days."""
    check_expenses(type="A", data=[100, 50, 75], expected="75.0")

@check50.check(compiles)
def average_5_days():
    """travel_expenses calculates average expenses over 5 days."""
    check_expenses(type="A", data=[200, 150, 80, 120, 95], expected="129.0")

# Вспомогательная функция для проверки расходов
def check_expenses(type: str, data: list, expected: str):
    program = check50.run("./travel_expenses").stdin(str(len(data)))
    for i, expense in enumerate(data):
        program.stdin(str(expense)).stdout(f"Расходы за день {i}: ")  # Изменено здесь
    program.stdin(type).stdout(expected)