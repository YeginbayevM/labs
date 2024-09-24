import check50
import check50.c

@check50.check()
def exists():
    """ "scrabble.c" существует """ 
    check50.exists("scrabble.c")

@check50.check(exists)
def compiles():
    """ "scrabble.c" компилируется """
    check50.c.compile("scrabble.c", lcs50=True)

@check50.check(compiles)
def handles_case():
    """ корректно обрабатывает регистр букв, например, 'а' и 'A' """
    # Добавляем набор букв перед словами игроков
    check50.run("./scrabble").stdin("AELRSTXY").stdin("LETTERCASE").stdin("lettercase").stdout(check50.regex("[Tt]ie!?")).exit(0)

@check50.check(compiles)
def handles_punctuation():
    """ корректно обрабатывает знаки препинания """
    # Добавляем набор букв перед словами игроков
    check50.run("./scrabble").stdin("AEINOPSTU").stdin("Punctuation!?!?").stdin("punctuation").stdout(check50.regex("[Tt]ie!?")).exit(0)

@check50.check(compiles)
def test_question_marks():
    """ 'Question?' и 'Question!' приводят к ничьей """
    # Добавляем набор букв перед словами игроков
    check50.run("./scrabble").stdin("EEINQSTU").stdin("Question?").stdin("Question!").stdout(check50.regex("[Tt]ie!?")).exit(0)

@check50.check(compiles)
def test_drawing_illustration():
    """ 'drawing' и 'illustration' приводят к ничьей """
    # Добавляем набор букв перед словами игроков
    check50.run("./scrabble").stdin("ADEGILNORST").stdin("drawing").stdin("illustration").stdout(check50.regex("[Tt]ie!?")).exit(0)

@check50.check(compiles)
def test_hai_beats_oh():
    """ 'hai!' побеждает 'Oh,' """
    # Добавляем набор букв перед словами игроков
    check50.run("./scrabble").stdin("AEHIOLST").stdin("Oh,").stdin("hai!").stdout(check50.regex("[Pp]layer 2 [Ww]ins!?")).exit(0)

@check50.check(compiles)
def test_computer_beats_science():
    """ 'COMPUTER' побеждает 'science' """
    # Добавляем набор букв перед словами игроков
    check50.run("./scrabble").stdin("CEMOPRTU").stdin("COMPUTER").stdin("science").stdout(check50.regex("[Pp]layer 1 [Ww]ins!?")).exit(0)

@check50.check(compiles)
def test_scrabble_beats_winner():
    """ 'Scrabble' побеждает 'wiNNeR' """
    # Добавляем набор букв перед словами игроков
    check50.run("./scrabble").stdin("ABCEILNRRS").stdin("Scrabble").stdin("wiNNeR").stdout(check50.regex("[Pp]layer 1 [Ww]ins!?")).exit(0)

@check50.check(compiles)
def test_pig_beats_dog():
    """ 'pig' побеждает 'dog' """
    # Добавляем набор букв перед словами игроков
    check50.run("./scrabble").stdin("DGIP").stdin("pig").stdin("dog").stdout(check50.regex("[Pp]layer 1 [Ww]ins!?")).exit(0)

@check50.check(compiles)
def test_skating_beats_figure():
    """ 'Skating!' побеждает 'figure?' """
    # Добавляем набор букв перед словами игроков
    check50.run("./scrabble").stdin("AEFGIKNRST").stdin("figure?").stdin("Skating!").stdout(check50.regex("[Pp]layer 2 [Ww]ins!?")).exit(0)