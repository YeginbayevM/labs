import check50
import check50.c

@check50.check()
def exists():
    """scrabble.c существует"""
    check50.exists("scrabble.c")

@check50.check(exists)
def compiles():
    """scrabble.c компилируется"""
    check50.c.compile("scrabble.c", lcs50=True)

@check50.check(compiles)
def tie_letter_case():
    """в программе верно обрабатывается регистр символов, например 'а' на 'A', или наоборот"""
    check50.run("./scrabble").stdin("1").stdin("LETTERCASE").stdin("lettercase").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compiles)
def tie_punctuation():
    """в программе верно обрабатываются знаки препинания"""
    check50.run("./scrabble").stdin("1").stdin("Punctuation!?!?").stdin("punctuation").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compiles)
def test1():
    """слова 'Question?' и 'Question!' верно учитываются и считаются ничьёй"""
    check50.run("./scrabble").stdin("1").stdin("Question?").stdin("Question!").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compiles)
def test2():
    """слова 'drawing' и 'illustration' верно учитываются и считаются ничьёй"""
    check50.run("./scrabble").stdin("1").stdin("drawing").stdin("illustration").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compiles)
def test3():
    """слово 'hai!' верно учитывается и преобладает над словом 'Oh,'"""
    check50.run("./scrabble").stdin("1").stdin("Oh,").stdin("hai!").stdout("[Pp]layer 2 [Ww]ins!?", "Player 2 wins!").exit(0)

@check50.check(compiles)
def test4():
    """слово 'COMPUTER' верно учитывается и преобладает над словом 'science'"""
    check50.run("./scrabble").stdin("1").stdin("COMPUTER").stdin("science").stdout("[Pp]layer 1 [Ww]ins!?", "Player 1 wins!").exit(0)

@check50.check(compiles)
def test5():
    """слово 'Scrabble' верно учитывается и преобладает над словом 'wiNNeR'"""
    check50.run("./scrabble").stdin("1").stdin("Scrabble").stdin("wiNNeR").stdout("[Pp]layer 1 [Ww]ins!?", "Player 1 wins!").exit(0)

@check50.check(compiles)
def test6():
    """слово 'pig' верно учитывается и преобладает над словом 'dog'"""
    check50.run("./scrabble").stdin("1").stdin("pig").stdin("dog").stdout("[Pp]layer 1 [Ww]ins!?", "Player 1 wins!").exit(0)

@check50.check(compiles)
def complex_case():
    """слово 'Skating!' верно учитывается и преобладает над словом 'figure?'"""
    check50.run("./scrabble").stdin("1").stdin("figure?").stdin("Skating!").stdout("[Pp]layer 2 [Ww]ins!?", "Player 2 wins!").exit(0)

