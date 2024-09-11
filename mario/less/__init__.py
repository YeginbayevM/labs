import check50
import check50.c

@check50.check()
def exists():
    """mario.c exists"""
    check50.exists("mario.c")
    check50.include("1.txt", "2.txt", "8.txt")

@check50.check(exists)
def compiles():
    """mario.c compiles"""
    check50.c.compile("mario.c", lcs50=True)

@check50.check(compiles)
def test_reject_invalid_height():
    """rejects heights that are not positive integers between 1 and 8"""
    check50.run("./mario").stdin("-1").reject()
    check50.run("./mario").stdin("0").reject()
    check50.run("./mario").stdin("9").reject()
    check50.run("./mario").stdin("foo").reject()
    check50.run("./mario").stdin("").reject()

@check50.check(compiles)
def test_correct_outputs():
    """handles heights of 1, 2, and 8 correctly"""
    check50.c.inputs("1", "2", "8").run("./mario").stdout(open("1.txt").read(), open("2.txt").read(), open("8.txt").read()).exit(0)


def check_pyramid(output, correct):
    if output == correct:
        return

    output = [line for line in output.splitlines() if line != ""]
    correct = correct.splitlines()

    help = None
    if len(output) == len(correct):
        if all(ol.rstrip() == cl for ol, cl in zip(output, correct)):
            help = "did you add too much trailing whitespace to the end of your pyramid?"
        elif all(ol[1:] == cl for ol, cl in zip(output, correct)):
            help = "are you printing an additional character at the beginning of each line?"

    raise check50.Mismatch(correct, output, help=help) 1