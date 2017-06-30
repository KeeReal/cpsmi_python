# coding=utf-8
# Из последовательности a(n) удалить все нулевые элементы, расположенные после ее
# максимального элемента.


def del_all_zeroes_after_max_item(arr):
    if len(arr) == 0:
        return arr

    index_max = arr.index(max(arr))
    before = arr[:index_max + 1]

    for i in range(index_max + 1, len(arr)):
        if arr[i] > 0:
            before.append(arr[i])

    return before
