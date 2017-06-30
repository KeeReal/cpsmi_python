# coding=utf-8
# В последовательности a(n) найти количество отрицательных элементов, расположенных
# между двумя первыми нулевыми элементами.


def num_negatives_between_two_first_zeroes(arr):
    index_left = -1
    index_right = -1

    for i in range(len(arr)):
        if arr[i] == 0:
            if index_left == -1:
                index_left = i
                continue

            if index_right == -1:
                index_right = i

    if index_left == -1 or index_right == -1:
        return -1

    if index_left == index_right - 1:
        return 0

    part = arr[index_left + 1:index_right]

    num_negatives = 0
    for i in range(len(part)):
        if part[i] < 0:
            num_negatives += 1

    return num_negatives
