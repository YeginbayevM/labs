import check50
import check50.c

# Проверяем, что файл travel_expenses.c существует
@check50.check()
def exists():
    """Файл travel_expenses.c существует""" 
    check50.exists("travel_expenses.c")

# Проверяем, что файл travel_expenses.c успешно компилируется
@check50.check(exists)
def compiles():
    """Файл travel_expenses.c компилируется""" 
    check50.c.compile("travel_expenses.c", lcs50=True)

# Проверяем расчет общей суммы расходов за 3 дня
@check50.check(compiles)
def total_3_days():
    """travel_expenses рассчитывает общую сумму расходов за 3 дня""" 
    check_expenses(type="T", data=[50, 80, 120], expected="250.0")

# Проверяем расчет общей суммы расходов за 4 дня
@check50.check(compiles)
def total_4_days():
    """travel_expenses рассчитывает общую сумму расходов за 4 дня""" 
    check_expenses(type="T", data=[100, 75, 90, 60], expected="325.0")

# Проверяем расчет средних расходов за 3 дня
@check50.check(compiles)
def average_3_days():
    """travel_expenses рассчитывает средние расходы за 3 дня""" 
    check_expenses(type="A", data=[100, 50, 75], expected="75.0")

# Проверяем расчет средних расходов за 5 дней
@check50.check(compiles)
def average_5_days():
    """travel_expenses рассчитывает средние расходы за 5 дней""" 
    check_expenses(type="A", data=[200, 150, 80, 120, 95], expected="129.0")

# Вспомогательная функция для проверки расходов
def check_expenses(type: str, data: list, expected: str):
    program = check50.run("./travel_expenses").stdin(str(len(data)))
    for expense in data:
        program.stdin(str(expense))
    program.stdin(type).stdout(expected)