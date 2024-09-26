import check50
import check50.c

@check50.check()
def exists():
    """movies.c существует."""
    check50.exists("movies.c")

@check50.check(exists)
def compiles():
    """movies.c компилируется."""
    check50.c.compile("movies.c", lcs50=True)

@check50.check(compiles)
def test_sorting():
    """Проверяет корректность сортировки фильмов по рейтингу."""
    expected_output = """Список фильмов, отсортированных по рейтингу

The Shawshank Redemption: 9.3
The Godfather: 9.2
The Dark Knight: 9.0
Schindler's List: 9.0
The Lord of the Rings: The Return of the King: 8.9
Pulp Fiction: 8.9
The Good, the Bad and the Ugly: 8.8
Forrest Gump: 8.8
Inception: 8.8
The Empire Strikes Back: 8.7
La La Land: 8.3
Jumanji: 7.3
Transformers: 7.0
Sonic the Hedgehog 2: 6.5
A Quiet Place: Day One: 6.3
"""
    check50.run("./movies").stdout(expected_output).exit(0)


# Дополнительные проверки можно добавить по аналогии, например:
# @check50.check(compiles)
# def test_empty_list():
#     """Проверяет корректность обработки пустого списка фильмов."""
#     # ...