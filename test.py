#!/usr/bin/python3.8
import sys, array, tempfile, heapq


def get_names(stream, bytes_frame=100):
    half_part = ''
    while True:
        big_string = stream.readline(bytes_frame).decode("utf-8")  # get n bytes
        if len(big_string) == 0:
            break
        string_list = big_string.split(',')
        string_list = [x for x in string_list if not x == '']  # deletes blank element of list

        if not (string_list[0].count('\"') == 2):  # we have a cut tail
            string_list[0] = half_part + string_list[0]
            half_part = ''

        if not string_list[-1].count('\"') == 2:  # we have a cut head
            half_part = string_list[-1]
            del string_list[-1]

        for name in string_list:
            yield name


if __name__ == '__main__':

    k = get_names(sys.stdin.buffer, 1000000)
    for i in k:
        print(i)
