#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Максимальное число кандидатов
#define MAX 9

// У кандидатов есть имя и подсчёт голосов
typedef struct
{
    string name;
    int votes;
}
candidate;

// Массив кандидатов
candidate candidates[MAX];

// Число кандидатов
int candidate_count;

//Прототипы функций
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Провервка на недопустимое использование
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Заполнение массива кандидатов
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Перебор всех избирателей
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Проверка на недействительность голосования
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Вывод победителя выборов
    print_winner();
}

// Обновление итогового результата голосования с учётом нового голоса
bool vote(string name)
{
    // TODO
    return false;
}

// Вывод победителя или победителей выборов
void print_winner(void)
{
    // TODO
    return;
}