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
    # Запускаем программу с одним раундом и получаем вывод
    result = check50.run("./scrabble").stdin("1").stdout()

    # Извлекаем набор букв из вывода
    letters = None
    for line in result.splitlines():
        if line.startswith("Набор букв: "):
            letters = line.split(": ")[1]
            break
    assert letters is not None, "Failed to find generated letters"

    # Продолжаем выполнение с теми же буквами и проверяем вывод
    check50.run(result).stdin("LETTERCASE").stdin("lettercase").stdout(check50.regex("[Tt]ie!?")).exit(0)

@check50.check(compiles)
def handles_punctuation():
    """ корректно обрабатывает знаки препинания """
    result = check50.run("./scrabble").stdin("1").stdout()
    letters = None
    for line in result.splitlines():
        if line.startswith("Набор букв: "):
            letters = line.split(": ")[1]
            break
    assert letters is not None, "Failed to find generated letters"

    check50.run(result).stdin("Punctuation!?!?").stdin("punctuation").stdout(check50.regex("[Tt]ie!?")).exit(0)

@check50.check(compiles)
def test_question_marks():
    """ 'Question?' и 'Question!' приводят к ничьей """
    result = check50.run("./scrabble").stdin("1").stdout()
    letters = None
    for line in result.splitlines():
        if line.startswith("Набор букв: "):
            letters = line.split(": ")[1]
            break
    assert letters is not None, "Failed to find generated letters"

    check50.run(result).stdin("Question?").stdin("Question!").stdout(check50.regex("[Tt]ie!?")).exit(0)

@check50.check(compiles)
def test_drawing_illustration():
    """ 'drawing' и 'illustration' приводят к ничьей """
    result = check50.run("./scrabble").stdin("1").stdout()
    letters = None
    for line in result.splitlines():
        if line.startswith("Набор букв: "):
            letters = line.split(": ")[1]
            break
    assert letters is not None, "Failed to find generated letters"

    check50.run(result).stdin("drawing").stdin("illustration").stdout(check50.regex("[Tt]ie!?")).exit(0)

@check50.check(compiles)
def test_hai_beats_oh():
    """ 'hai!' побеждает 'Oh,' """
    result = check50.run("./scrabble").stdin("1").stdout()
    letters = None
    for line in result.splitlines():
        if line.startswith("Набор букв: "):
            letters = line.split(": ")[1]
            break
    assert letters is not None, "Failed to find generated letters"

    check50.run(result).stdin("Oh,").stdin("hai!").stdout(check50.regex("[Pp]layer 2 [Ww]ins!?")).exit(0)

@check50.check(compiles)
def test_computer_beats_science():
    """ 'COMPUTER' побеждает 'science' """
    result = check50.run("./scrabble").stdin("1").stdout()
    letters = None
    for line in result.stdout.splitlines():
        if line.startswith("Набор букв: "):
            letters = line.split(": ")[1]
            break
    assert letters is not None, "Failed to find generated letters"

    check50.run(result).stdin("COMPUTER").stdin("science").stdout(check50.regex("[Pp]layer 1 [Ww]ins!?")).exit(0)

@check50.check(compiles)
def test_scrabble_beats_winner():
    """ 'Scrabble' побеждает 'wiNNeR' """
    result = check50.run("./scrabble").stdin("1").stdout()
    letters = None
    for line in result.stdout.splitlines():
        if line.startswith("Набор букв: "):
            letters = line.split(": ")[1]
            break
    assert letters is not None, "Failed to find generated letters"

    check50.run(result).stdin("Scrabble").stdin("wiNNeR").stdout(check50.regex("[Pp]layer 1 [Ww]ins!?")).exit(0)

@check50.check(compiles)
def test_pig_beats_dog():
    """ 'pig' побеждает 'dog' """
    result = check50.run("./scrabble").stdin("1").stdout()
    letters = None
    for line in result.splitlines():
        if line.startswith("Набор букв: "):
            letters = line.split(": ")[1]
            break
    assert letters is not None, "Failed to find generated letters"

    check50.run(result).stdin("pig").stdin("dog").stdout(check50.regex("[Pp]layer 1 [Ww]ins!?")).exit(0)

@check50.check(compiles)
def test_skating_beats_figure():
    """ 'Skating!' побеждает 'figure?' """
    result = check50.run("./scrabble").stdin("1").stdout()
    letters = None
    for line in result.stdout.splitlines():
        if line.startswith("Набор букв: "):
            letters = line.split(": ")[1]
            break
    assert letters is not None, "Failed to find generated letters"

    check50.run(result).stdin("figure?").stdin("Skating!").stdout(check50.regex("[Pp]layer 2 [Ww]ins!?")).exit(0)