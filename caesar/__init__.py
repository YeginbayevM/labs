import check50
import check50.c

@check50.check()
def exists():
    """caesar.c существует."""
    check50.exists("caesar.c")

@check50.check(exists)
def compiles():
    """caesar.c компилируется."""
    check50.c.compile("caesar.c", lcs50=True)

@check50.check(compiles)
def encrypts_a_as_b():
    """символ "a" шифруется как "b" с помощью ключа 1"""
    check50.run("./caesar 1").stdin("a").stdout("[Cc]iphertext:\s*b\n", "ciphertext: b\n").exit(0)

@check50.check(compiles)
def encrypts_barfoo_as_yxocll():
    """сообщение "barfoo" шифруется как "yxocll" с помощью ключа 23"""
    check50.run("./caesar 23").stdin("barfoo").stdout("[Cc]iphertext:\s*yxocll\n", "ciphertext: yxocll\n").exit(0)

@check50.check(compiles)
def encrypts_BARFOO_as_EDUIRR():
    """сообщение "BARFOO" шифруется как "EDUIRR" с помощью ключа 3"""
    check50.run("./caesar 3").stdin("BARFOO").stdout("[Cc]iphertext:\s*EDUIRR\n", "ciphertext: EDUIRR\n").exit(0)

@check50.check(compiles)
def encrypts_BaRFoo_FeVJss():
    """сообщение "BaRFoo" шифруется как "FeVJss" с помощью ключа 4"""
    check50.run("./caesar 4").stdin("BaRFoo").stdout("[Cc]iphertext:\s*FeVJss\n", "ciphertext: FeVJss\n").exit(0)

@check50.check(compiles)
def encrypts_barfoo_as_onesbb():
    """сообщение "barfoo" шифруется как "onesbb" с помощью ключа 65"""
    check50.run("./caesar 65").stdin("barfoo").stdout("[Cc]iphertext:\s*onesbb\n", "ciphertext: onesbb\n").exit(0)

@check50.check(compiles)
def checks_for_handling_non_alpha():
    """сообщение "world, say hello!" шифруется как "iadxp, emk tqxxa!" с помощью ключа 12"""
    check50.run("./caesar 12").stdin("world, say hello!").stdout("[Cc]iphertext:\s*iadxp, emk tqxxa!\n", "ciphertext: iadxp, emk tqxxa!\n").exit(0)

@check50.check(compiles)
def handles_no_argv():
    """программа учитывает отсутствие аргументов командной строки"""
    check50.run("./caesar").exit(1)
    
@check50.check(compiles)
def handles_non_numeric_argv():
    """программа учитывает, что в аргументе командной строки в качестве ключа может быть только число"""
    check50.run("./caesar 2x").exit(1)
    
@check50.check(compiles)
def too_many_args():
    """программа учитывает, что может быть введено 2 и более агрументов командной строки"""
    check50.run("./caesar 1 2").exit(1)
