#!/usr/bin/python3.8
import sys, array, tempfile, heapq


def read_strings_form_file(in_file):
    while True:
        strings = [next(in_file) for _ in range(5)]
        if not strings:  # если пустой массив, то прервыем цыкл
            break
        for i in strings:  # возвращаем поштучно инты
            yield i


if __name__ == '__main__':
    iters = []
    while True:
        in_arr = sys.stdin.buffer.readlines()  # читаем все
        print(in_arr)
        if not in_arr:  # если пустой то выходим
            break
        temp_file = tempfile.TemporaryFile()
        temp_file.writelines(sorted(in_arr))
        temp_file.seek(0)
        iters.append(read_strings_form_file(temp_file))

    in_arr = []
    for x in heapq.merge(*iters):
        in_arr.append(x)
        if len(in_arr) >= 5:
            sys.stdout.buffer.writelines(in_arr)
            del in_arr[:]
    if in_arr:
        sys.stdout.buffer.writelines(in_arr)

