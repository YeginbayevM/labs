#include <cs50.h>
#include <stdio.h>

// Очки, присвоенные каждой букве алфавита
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Получить количество раундов от пользователя
    int num_rounds = get_int("Введите количество раундов: ");
    
    // Отслеживать количество очков для каждого игрока
    int score1 = 0;
    int score2 = 0;

    /* TODO: Реализовать игровой цикл, который в каждом раунде получает слова от обоих игроков, 
    подсчитывает очки для каждого слова, выводит очки раунда для каждого игрока и обновляет общее количество очков. */

    

    // TODO:  Определить победителя игры, сравнив итоговые очки игроков, и вывести результаты игры,  включая итоговые очки каждого игрока и имя победителя (или сообщение о ничьей).

}

int compute_score(string word)
{
    // TODO: Вычислить и вернуть результат (сумму очков) для строки (word)

}