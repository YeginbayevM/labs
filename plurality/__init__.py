import check50
import check50.c
import re

@check50.check()
def exists():
    """plurality.c существует"""
    check50.exists("plurality.c")
    check50.include("testing.c")


@check50.check(exists)
def compiles():
    """plurality компилируется"""
    check50.c.compile("plurality.c", lcs50=True)
    plurality = re.sub("int\s+main", "int distro_main", open("plurality.c").read())
    testing = open("testing.c").read()
    with open("plurality_test.c", "w") as f:
        f.write(plurality)
        f.write("\n")
        f.write(testing)
    check50.c.compile("plurality_test.c", lcs50=True)

@check50.check(compiles)
@check50.hidden("vote function did not return true")
def vote_finds_name_first():
    """vote возвращает значение true, если указано имя первого кандидата"""
    check50.run("./plurality_test 0 0").stdout("true").exit(0)

@check50.check(compiles)
@check50.hidden("vote function did not return true")
def vote_finds_name_middle():
    """vote возвращает значение true, если указано имя кандидата в середине списка"""
    check50.run("./plurality_test 0 1").stdout("true").exit(0)

@check50.check(compiles)
@check50.hidden("vote function did not return true")
def vote_finds_name_last():
    """vote возвращает значение true, если указано имя последнего кандидата"""
    check50.run("./plurality_test 0 2").stdout("true").exit(0)

@check50.check(compiles)
@check50.hidden("vote function did not return false")
def vote_returns_false():
    """vote возвращает значение false, если указано имя недействительного кандидата"""
    check50.run("./plurality_test 0 3").stdout("false").exit(0)

@check50.check(compiles)
@check50.hidden("vote function did not correctly update vote totals")
def first_vote_totals_correct():
    """vote приводит к правильному подсчету голосов, когда все голоса равны нулю"""
    check50.run("./plurality_test 0 4").stdout("1 0 0").exit(0)

@check50.check(compiles)
@check50.hidden("vote function did not correctly update vote totals")
def subsequent_vote_totals_correct():
    """vote приводит к правильному подсчету голосов после того, как некоторые из них уже проголосовали"""
    check50.run("./plurality_test 0 5").stdout("2 8 0").exit(0)

@check50.check(compiles)
@check50.hidden("vote function modified vote totals incorrectly")
def invalid_vote_votes_unchanged():
    """vote оставляет подсчет голосов без изменений при голосовании за недействительного кандидата"""
    check50.run("./plurality_test 0 6").stdout("2 8 0").exit(0)

@check50.check(compiles)
@check50.hidden("print_winner function did not print winner of election")
def print_winner0():
    """print_winner определяет Alice как победителя выборов"""
    check50.run("./plurality_test 0 7").stdout("^Alice\n?$").exit(0)

@check50.check(compiles)
@check50.hidden("print_winner function did not print winner of election")
def print_winner1():
    """print_winner определяет Bob как победителя выборов"""
    check50.run("./plurality_test 0 8").stdout("^Bob\n?$").exit(0)

@check50.check(compiles)
@check50.hidden("print_winner function did not print winner of election")
def print_winner2():
    """print_winner определяет Charlie как победителя выборов"""
    check50.run("./plurality_test 0 9").stdout("^Charlie\n?$").exit(0)

@check50.check(compiles)
@check50.hidden("print_winner function did not print both winners of election")
def print_winner3():
    """print_winner выводит несколько победителей в случае ничьей"""
    result = check50.run("./plurality_test 0 10").stdout()
    if set(result.split("\n")) - {""} != {"Alice", "Bob"}:
        raise check50.Mismatch("Alice\nBob\nCharlie\n", result)

@check50.check(compiles)
@check50.hidden("print_winner function did not print all three winners of election")
def print_winner4():
    """print_winner печатает все имена кандидатов, когда число голосов всех кандидатов равны"""
    result = check50.run("./plurality_test 0 11").stdout()
    if set(result.split("\n")) - {""} != {"Alice", "Bob", "Charlie"}:
        raise check50.Mismatch("Alice\nBob\nCharlie\n", result)
