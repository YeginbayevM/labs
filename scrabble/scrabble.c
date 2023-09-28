#include <cs50.h>
#include <stdio.h>

// Баллы, присвоенные каждой букве алфавита
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Запрос на ввод слова от обоих игроков
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Подсчёт очков каждого игрока
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Вывод сообщения о победителе
}

int compute_score(string word)
{
    // TODO: Вычисление и возврат полученного результата (суммы баллов) для строки (word)
}