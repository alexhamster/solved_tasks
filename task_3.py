import itertools
import math


def get_zeros(n):
    """
    Задача нахождения кол-ва нулей в !n, сводится к нахождению
    всех сомножетелей числа n делящихся на 5 с некоторыми оговорками
    """
    parts = [i + 1 for i in range(n)]
    divided_by_five = []

    count_five = 0
    count_two = 0
    for part in parts:
        if part % 5 == 0:
            divided_by_five.append(part)
            count_five += 1
        if part % 2 == 0:
            count_two += part // 2

    """
    10 = 2 * 5; Количество уникальных пар 
    пятерок и двоек определяют кол во нулей в конце числа.
    Обычно кол-во двоек на порядок больше пятерок, но лучше
    дополнительно проверить 
    """
    if count_two < count_five:
        return count_two

    """
    Но есть числа типа 25, 125, 625, ...: 25 = 5 * 5; 125 = 5 * 5 * 5;
    Необходимо найти эти числа и проверить, в какие другие числа делящиеся
    на 5 они входят множетялями.
    
    Eсть набор чисел N, у которых Log5(N) - целое число(принадлежит множеству Z).
    Наибольшее число N1 из набора И, которое является множителем для M,
    увеличивает кол-во нулей на Log5(N1)-1. 
    """
    n = []  # соддержит кортежи виды (число, сколько нулей добавляет)
    for i in divided_by_five:
        log = math.log(i, 5)
        if log % 1 == .0 and not i == 5:
            n.append((i, int(log - 1)))

    n.reverse()  # начинаем проверять с самых больших
    for x in n:
        for j in divided_by_five:
            if j % x[0] == 0:
                count_five += x[1]
                divided_by_five.remove(j)  # удаляем, чтобы не посчитать дважды
    return count_five


if __name__ == '__main__':
    # Ответ: Сложность O(n)
    print(get_zeros(5))
