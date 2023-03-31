"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def score_game(game_core_v3) ->int:
    """_За какое количество попыток в среднем угадывает наш алгоритм_

    Args:
        game_core_v3 (_type_): _функция угадывания_

    Returns:
        int: _среднее количество попыток_
    """
    count_lst = [] #список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости эксперимента
    random_array = np.random.randint(1,101, size=(1000)) #загадываем список чисел
    
    for number in random_array:
        count_lst.append(game_core_v3(number))
    
    score = int(np.mean(count_lst)) #находим среднее количество попыток
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return score


def game_core_v3(number: int = 1) -> int:
    """_Компьютер сам загадывает и сам угадывает число (угадывает с помощью алгоритма бинарного поиска)_

    Args:
        number (int, optional): _Загаданное число_. Defaults to 1.

    Returns:
        int: _Число попыток_
    """
    count = 1
    low,high = 0, 101 #задаем изначальные минимальное и максимальное значения для угадывания
    
    
    predict = (low + high)//2
    
    while number != predict:
        count += 1
        if number > predict:
            low = predict
        else:
            high = predict
        
        predict = (low + high)//2   
    
    return count    

print('Run benchmarking for game_core_v3: ', end='')
if __name__ == "__main__":
    # RUN
    score_game (game_core_v3)