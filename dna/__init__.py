import check50

@check50.check()
def exists():
    """dna.py exists"""
    check50.exists("dna.py")
    check50.include("sequences", "databases")

@check50.check(exists)
def test1():
    """Корректно идентифицирует файл sequences/1.txt"""
    check50.run("python3 dna.py databases/small.csv sequences/1.txt").stdout("^Bob", "Bob\n", timeout=5).exit()

@check50.check(exists)
def test2():
    """Корректно идентифицирует файл sequences/2.txt"""
    check50.run("python3 dna.py databases/small.csv sequences/2.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(exists)
def test3():
    """Корректно идентифицирует файл sequences/3.txt"""
    check50.run("python3 dna.py databases/small.csv sequences/3.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(exists)
def test4():
    """Корректно идентифицирует файл sequences/4.txt"""
    check50.run("python3 dna.py databases/small.csv sequences/4.txt").stdout("^Alice", "Alice\n", timeout=5).exit()

@check50.check(exists)
def test5():
    """Корректно идентифицирует файл sequences/5.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/5.txt").stdout("^Lavender", "Lavender\n", timeout=5).exit()

@check50.check(exists)
def test6():
    """Корректно идентифицирует файлs sequences/6.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/6.txt").stdout("^Luna", "Luna\n", timeout=5).exit()

@check50.check(exists)
def test7():
    """Корректно идентифицирует файл sequences/7.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/7.txt").stdout("^Ron", "Ron\n", timeout=5).exit()

@check50.check(exists)
def test8():
    """Корректно идентифицирует файл sequences/8.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/8.txt").stdout("^Ginny", "Ginny\n", timeout=5).exit()

@check50.check(exists)
def test9():
    """Корректно идентифицирует файл sequences/9.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/9.txt").stdout("^Draco", "Draco\n", timeout=5).exit()

@check50.check(exists)
def test10():
    """Корректно идентифицирует файл sequences/10.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/10.txt").stdout("^Albus", "Albus\n", timeout=5).exit()

@check50.check(exists)
def test11():
    """Корректно идентифицирует файл sequences/11.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/11.txt").stdout("^Hermione", "Hermione\n", timeout=5).exit()

@check50.check(exists)
def test12():
    """Корректно идентифицирует файл sequences/12.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/12.txt").stdout("^Lily", "Lily\n", timeout=5).exit()

@check50.check(exists)
def test13():
    """Корректно идентифицирует файл sequences/13.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/13.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(exists)
def test14():
    """Корректно идентифицирует файл sequences/14.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/14.txt").stdout("^Severus", "Severus\n", timeout=5).exit()

@check50.check(exists)
def test15():
    """Корректно идентифицирует файл sequences/15.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/15.txt").stdout("^Sirius", "Sirius\n", timeout=5).exit()

@check50.check(exists)
def test16():
    """Корректно идентифицирует файл sequences/16.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/16.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(exists)
def test17():
    """Корректно идентифицирует файл sequences/17.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/17.txt").stdout("^Harry", "Harry\n", timeout=5).exit()

@check50.check(exists)
def test18():
    """Корректно идентифицирует файл sequences/18.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/18.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(exists)
def test19():
    """Корректно идентифицирует файл sequences/19.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/19.txt").stdout("^Fred", "Fred\n", timeout=5).exit()

@check50.check(exists)
def test20():
    """Корректно идентифицирует файл sequences/20.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/20.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

