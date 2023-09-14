import check50
import check50.c


@check50.check()
def exists():
    """debug.c exists"""
    check50.exists("debug.c")


@check50.check(exists)
def compiles():
    """debug.c compiles"""
    check50.c.compile("debug.c", lcs50=True)


@check50.check(compiles)
def frodo():
    """Input of \"Frodo\" and \"Shire\" produces output \"Hello, Frodo, from Shire!\""""
    check_debug(name="Frodo", place="Shire")


@check50.check(compiles)
def dumbledore():
    """Input of \"Dumbledore\" and \"Mould-on-the-Wold\" produces output \"Hello, Dumbledore, from Mould-on-the-Wold!\""""
    check_debug(name="Dumbledore", place="Mould-on-the-Wold")


# Helpers
def check_debug(name: str, place: str):
    check50.run("./debug").stdin(name).stdin(place).stdout(f"Hello, {name}, from {place}!")
