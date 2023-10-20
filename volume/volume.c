// Программа на изменение громкости аудиофайла
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Количество байт в заголовке файла .wav
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Проверить наличие аргументов командной строки
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Открыть файл и определить коэффициент масштабирования
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Скопировать заголовок входного файла в выходной файл

    // TODO: Считать данные сэмпла из входного файла и записать обновлённые данные в выходной файл

    // Закрыть файл
    fclose(input);
    fclose(output);
}
