import check50
import check50.c


@check50.check()
def exists():
    """prime.c существует"""
    check50.exists("prime.c")


@check50.check(exists)
def compiles():
    """prime.c компилируется"""
    check50.c.compile("prime.c", lcs50=True)


@check50.check(compiles)
def up_to_10():
    """Ввод 1 и 10 выдаёт все простые числа между 1 и 10, включительно"""
    check50.run("./prime").stdin("1").stdin("10").stdout("2\n3\n5\n7")


@check50.check(compiles)
def between_10_and_50():
    """Ввод 10 и 25 выдаёт все простые числа между 10 и 25, включительно"""
    check50.run("./prime").stdin("10").stdin("25").stdout("11\n13\n17\n19\n23")


@check50.check(compiles)
def between_50_and_60():
    """Ввод 50 и 60 выдаёт все простые числа между 50 и 60, включительно"""
    check50.run("./prime").stdin("50").stdin("60").stdout("53\n59")