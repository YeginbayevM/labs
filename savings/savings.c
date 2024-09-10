#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Запросить начальный баланс и проверить его корректность (start_balance)


    // TODO: Запросить процентную ставку и проверить её корректность (interest_rate)
   

    // TODO: Запросить ежегодное пополнение и проверить его корректность (yearly_deposit)
  

    // TODO: Запросить целевой баланс и проверить его корректность (target_balance)


    // TODO: Вычислить количество лет, необходимых для хранения целевого баланса (current_balance)
    
    int years = 0;
    int current_balance = start_balance;

    while (current_balance < target_balance) 
    {
        // TODO: Вычислить количество лет, необходимых для достижения целевого баланса
        years++; 
    }

    // TODO: Вывести результат

    return 0;
}