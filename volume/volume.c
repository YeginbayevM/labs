// Изменяет громкость аудиофайла

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Размер заголовка файла .wav в байтах
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Проверка аргументов командной строки
    if (argc != 4)
    {
        printf("Использование: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Открытие файлов и определение коэффициента масштабирования
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Не удалось открыть файл.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Не удалось открыть файл.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Скопировать заголовок из входного файла в выходной файл

    // TODO: Прочитать сэмплы из входного файла и записать обновленные данные в выходной файл

    // Закрытие файлов
    fclose(input);
    fclose(output);
}