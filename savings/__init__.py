import check50
import check50.c

@check50.check()
def exists():
    """savings.c существует"""  # "savings.c exists"
    check50.exists("savings.c")

@check50.check(exists)
def compiles():
    """savings.c компилируется"""  # "savings.c compiles"
    check50.c.compile("savings.c", lcs50=True)

@check50.check(compiles)
def negative_start():
    """отклоняет отрицательный начальный баланс"""  # "rejects a negative starting balance"
    check50.run("./savings").stdin("-100").reject()

@check50.check(compiles)
def negative_interest():
    """отклоняет отрицательную процентную ставку"""  # "rejects a negative interest rate"
    check50.run("./savings").stdin("100").stdin("-5").reject()

@check50.check(compiles)
def negative_deposit():
    """отклоняет отрицательное ежегодное пополнение"""  # "rejects a negative annual deposit"
    check50.run("./savings").stdin("100").stdin("5").stdin("-50").reject()

@check50.check(compiles)
def low_end():
    """отклоняет конечный баланс меньше начального"""  # "rejects an end balance less than the start balance"
    check50.run("./savings").stdin("100").stdin("5").stdin("50").stdin("50").reject()

@check50.check(compiles)
def test_example():
    """обрабатывает пример из условия задачи"""  # "handles the example from the problem"
    check50.run("./savings").stdin("250000").stdin("13").stdin("90000").stdin("372500").stdout("Лет: 1\n").exit(0)

@check50.check(compiles)
def test_no_growth():
    """обрабатывает случай, когда конечный баланс равен начальному"""  # "handles the case where the end balance is the same as the start balance"
    check50.run("./savings").stdin("1000").stdin("5").stdin("0").stdin("1000").stdout("Лет: 0\n").exit(0)
