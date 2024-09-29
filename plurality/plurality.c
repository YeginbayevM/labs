#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Максимальное количество кандидатов
#define MAX 9

// Кандидаты имеют имя и количество голосов
typedef struct
{
    string name;
    int votes;
}
candidate;

// Массив кандидатов
candidate candidates[MAX];

// Количество кандидатов
int candidate_count;

// Прототипы функций
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Проверка на некорректное использование
    if (argc < 2)
    {
        printf("Запустите так: ./plurality [Кандидат_1 ...]\n");
        return 1;
    }

    // Заполнение массива кандидатов
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Максимальное количество кандидатов – %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Введите количество избирателей: ");

    // Цикл по всем избирателям
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Введите голос: ");

        // Проверка на некорректный голос
        if (!vote(name))
        {
            printf("Некорректный голос.\n");
        }
    }

    // Вывод победителя выборов
    print_winner();
}

// Обновление общего количества голосов с учетом нового голоса
bool vote(string name)
{
    // TODO: Проверить, существует ли кандидат с именем name.
    // Если да, увеличить количество голосов этого кандидата на 1 и вернуть true.
    // В противном случае вернуть false.
    return false;
}

// Вывод победителя (или победителей) выборов
void print_winner(void)
{
    // TODO: Найти кандидата с наибольшим количеством голосов.
    // Вывести имя этого кандидата и вернуть значение.
    return;
}