import check50
import check50.c

@check50.check()
def exists():
    """mario.c существует"""  # "mario.c exists"
    check50.exists("mario.c")
    check50.include("1.txt", "2.txt", "8.txt")

@check50.check(exists)
def compiles():
    """mario.c компилируется"""  # "mario.c compiles"
    check50.c.compile("mario.c", lcs50=True)

@check50.check(compiles)
def test_reject_negative():
    """отклоняет высоту -1"""  # "rejects a height of -1"
    check50.run("./mario").stdin("-1").reject()

@check50.check(compiles)
def test0():
    """отклоняет высоту 0"""  # "rejects a height of 0"
    check50.run("./mario").stdin("0").reject()

@check50.check(compiles)
def test1():
    """корректно обрабатывает высоту 1"""  # "handles a height of 1 correctly"
    out = check50.run("./mario").stdin("1").stdout()
    check_pyramid(out, open("1.txt").read())

@check50.check(compiles)
def test2():
    """корректно обрабатывает высоту 2"""  # "handles a height of 2 correctly"
    out = check50.run("./mario").stdin("2").stdout()
    check_pyramid(out, open("2.txt").read())

@check50.check(compiles)
def test8():
    """корректно обрабатывает высоту 8"""  # "handles a height of 8 correctly"
    out = check50.run("./mario").stdin("8").stdout()
    check_pyramid(out, open("8.txt").read())

@check50.check(compiles)
def test9():
    """отклоняет высоту -1, а затем принимает высоту 2"""  # "rejects a height of -1, and then accepts a height of 2"
    out = check50.run("./mario").stdin("-1").reject().stdin("2").stdout()
    check_pyramid(out, open("2.txt").read())

@check50.check(compiles)
def test_reject_foo():
    """отклоняет нечисловую высоту \"foo\"" """  # "rejects a non-numeric height of "foo" "
    check50.run("./mario").stdin("foo").reject()

@check50.check(compiles)
def test_reject_empty():
    """отклоняет нечисловую высоту \"\"" """  # "rejects a non-numeric height of "" "
    check50.run("./mario").stdin("").reject()


def check_pyramid(output, correct):
    if output == correct:
        return

    output = [line for line in output.splitlines() if line != ""]
    correct = correct.splitlines()

    help = None
    if len(output) == len(correct):
        if all(ol.rstrip() == cl for ol, cl in zip(output, correct)):
            help = "вы добавили слишком много пробелов в конце пирамиды?"  # "did you add too much trailing whitespace to the end of your pyramid?"
        elif all(ol[1:] == cl for ol, cl in zip(output, correct)):
            help = "вы печатаете дополнительный символ в начале каждой строки?"  # "are you printing an additional character at the beginning of each line?"

    raise check50.Mismatch(correct, output, help=help)