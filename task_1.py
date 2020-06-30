import itertools


def clean_arr(arr, k):
    # set хранит только уникальные значения
    unique_arr = list(set(arr))
    if k % 2 == 0:  # если k - четное, то может быть пара (k/2, k/2)
        unique_arr.append(k // 2)
    return unique_arr


def search_pairs(arr, k):
    if not (isinstance(arr, list) and isinstance(k, int)):
        raise TypeError('Ban input, call search_pairs(list, int)')
    clear = clean_arr(arr, k)
    return [i for i in itertools.combinations(clear, 2) if sum(i) == k]


if __name__ == '__main__':
    arr = [7, 2, 6, 5, -3, 4, -7, 8, 3, 2]
    print(search_pairs(arr, 2))

# Ответ: O(n) - сложность по времени у itertools.combinations:
# https://stackoverflow.com/questions/53419536/what-is-the-computational-complexity-of-itertools-combinations-in-python
# Ответ: Оптимизируем через удаление повторяющихся элементов массива