#!/usr/bin/python3.8
import sys


def calc_alp_sum(string):
    string_sum = 0
    for i in string.lower():
        value = ord(i) - 96
        if value > 0:
            string_sum += value
    return string_sum


if __name__ == '__main__':
    out_sum = 0
    counter = 1
    while True:
        name = sys.stdin.readline().replace('\"', '').replace('\'', '').replace(' ', '') \
            .replace('\n', '').replace('\r', '')
        if not name:
            break
        word_sum = calc_alp_sum(name) * counter
        print(name, calc_alp_sum(name))
        out_sum += word_sum
        counter += 1

    print(out_sum)

# Используем командную строку Linux, чтобы привести данные в удобный для работы вид
# cat ./names.txt | tr , \\n | sort | ./task_2.py
# Ответ: 871853874