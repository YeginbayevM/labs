#include <cs50.h>
#include <stdio.h>

bool prime(int number);

int main(void)
{
    int min;
    do
    {
        min = get_int("Минимальное значение: ");
    }
    while (min < 1);

    int max;
    do
    {
        max = get_int("Максимальное значение: ");
    } 
    while (min >= max);
    
    for (int i = min; i <= max; i++)
    {
        if (prime(i))
        {
            printf("%i\n", i);
        }
    }
}

bool prime(int number)
{
    // TODO: Написать проверку на то, является ли число простым
    return false; // Пока что функция всегда возвращает false (не простое число)
}
