#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Запрашиваем начальный баланс и проверяем его корректность
    int start_balance;
    do
    {
        start_balance = get_int("Начальный баланс:")
    } 
    while (start_balance <= 0); 

    // Запрашиваем процентную ставку и проверяем ее корректность
    float interest_rate;
    do
    {
        interest_rate = get_float("Процентная ставка:")
    } 
    while (interest_rate <= 0);

    // Запрашиваем ежегодное пополнение и проверяем его корректность
    int yearly_deposit;
    do
    {
       yearly_depost = get_double("Ежегодное пополнение:")
    } 
    while (yearly_deposit <= 0); 

    // Запрашиваем целевой баланс и проверяем его корректность
    int target_balance;
    do
    {
        target_balance = get_double("Целевой баланс:")
    } 
    while (target_balance <= start_balance);

    // Вычисляем количество лет, необходимых для достижения целевого баланса
    int years = 0;
    int current_balance = start_balance;

    while (current_balance < target_balance) 
    {
        // TODO: Реализуйте логику начисления процентов и пополнения счета
        years++; 
    }

    // Выводим результат
    printf("Years: %d\n", years);

    return 0;
}