import check50
import check50.c

@check50.check()
def exists():
    """population.c существует"""
    check50.exists("population.c")

@check50.check(exists)
def compiles():
    """population.c компилируется"""
    check50.c.compile("population.c", lcs50=True)

@check50.check(compiles)
def start_less():
    """программа обрабатывает начальные значения меньше 9"""
    check50.run("./population").stdin("8").stdin("8").reject()

@check50.check(compiles)
def end_less():
    """программа обрабатывает отправку значений, меньших начальных значений"""
    check50.run("./population").stdin("50").stdin("49").reject()

@check50.check(compiles)
def decimal_truncation():
    """программа усекает десятичное количество лошадей (усечение чисел, truncation)"""
    check50.run("./population").stdin("1100").stdin("1192").stdout("Years: 2").exit(0)

@check50.check(compiles)
def same_value():
    """обрабатывает одинаковые начальные и конечные размеры"""
    check50.run("./population").stdin("100").stdin("100").stdout("Years: 0").exit(0)

@check50.check(compiles)
def test1():
    """программа рассчитана на начальное значение популяции в 1200 лошадей"""
    check50.run("./population").stdin("1200").stdin("1300").stdout("Years: 1").exit(0)

@check50.check(compiles)
def test2():
    """программа отклоняет недопустимые значения популяции и затем обрабатывает значение популяции: 9"""
    check50.run("./population").stdin("-5").stdin("3").stdin("9").stdin("5").stdin("18").stdout("Years: 8").exit(0)

@check50.check(compiles)
def test3():
    """программа отклоняет недопустимые значения популяции и затем обрабатывает значение популяци: 20"""
    check50.run("./population").stdin("20").stdin("1").stdin("10").stdin("100").stdout("Years: 20").exit(0)

@check50.check(compiles)
def test4():
    """программа обрабатывает начальное значение популяции в 100 лошадей"""
    check50.run("./population").stdin("100").stdin("1000000").stdout("Years: 115").exit(0)
