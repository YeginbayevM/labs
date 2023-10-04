import check50
import check50.c


@check50.check()
def exists():
    """password.c существует."""
    check50.exists("password.c")


@check50.check(exists)
def compiles():
    """password.c компилируется."""
    check50.c.compile("password.c", lcs50=True)


@check50.check(compiles)
def valid():
    """Пароль 3PQvbQ6_GvneW!3R действителен."""
    check_password(password="3PQvbQ6_GvneW!3R", valid=True)


@check50.check(compiles)
def no_uppercase():
    """Пароль hqsk3wb. не действителен из-за отсутствия заглавного символа."""
    check_password(password="hqsk3wb.", valid=False)


@check50.check(compiles)
def no_lowercase():
    """Пароль F-WH8PQP не действителен из-за отсутствия строчного символа."""
    check_password(password="F-WH8PQP", valid=False)


@check50.check(compiles)
def no_symbol():
    """Пароль VnrHMtV4 не действителен из-за отсутствия печатываемого символа (не буква и не цифра)."""
    check_password(password="VnrHMtV4", valid=False)


@check50.check(compiles)
def no_number():
    """Пароль iWnktW*q не действителен из-за отсутствия чисел."""
    check_password(password="iWnktW*q", valid=False)


# Helpers
def check_password(password: str, valid: bool):
    program = check50.run("./password").stdin(password)
    if valid:
        program.stdout("Ваш пароль действителен!")
    else:
        program.stdout("В вашем пароле должна быть по крайней мере одна заглавная буква, строчная буква, цифра и символ!")