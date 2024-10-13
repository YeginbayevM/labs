import check50
import check50.c

HASHES = ["268f2deee976fcc8dcc915be63cd3d4ac003a73a4b8bfd6f7b95c441a42ed1ec", "4481b5a438d359718000dfd58e2a32a7b109eb4a5590e0650c6bd295979c64fc", "3d83603745302935c067379b704573e5addb4356ad407041f0a698070e6e4e7b"]

@check50.check()
def exists():
    """volume.c существует"""
    check50.exists("volume.c")
    check50.include("input.wav")

@check50.check(exists)
def compiles():
    """volume.c компилируется"""
    check50.c.compile("volume.c", lcs50=True)

@check50.check(compiles)
def audio_half():
    """громкость звука корректно уменьшается в 0.5 раза"""
    check50.run("./volume input.wav output.wav 0.5").exit(0)
    if check50.hash("output.wav") != HASHES[0]:
        raise check50.Failure("Изменение громкости аудио не было выполнено корректно. Примененный коэффициент: 0.5")

@check50.check(compiles)
def audio_tenth():
    """громкость звука корректно уменьшается в 0.1 раза"""
    check50.run("./volume input.wav output.wav 0.1").exit(0)
    if check50.hash("output.wav") != HASHES[1]:
        raise check50.Failure("Изменение громкости аудио не было выполнено корректно. Примененный коэффициент: 0.1")

@check50.check(compiles)
def audio_x2():
    """громкость звука корректно увеличивается в 2 раза"""
    check50.run("./volume input.wav output.wav 2").exit(0)
    if check50.hash("output.wav") != HASHES[2]:
        raise check50.Failure("Изменение громкости аудио не было выполнено корректно. Примененный коэффициент: 2")

