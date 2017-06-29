# coding=utf-8
# В последовательности a(n) найти сумму целых элементов, расположенных между
# минимальным и максимальным элементами.


def sum_between_min_max(numbers):
    index_min = numbers.index(min(numbers))
    index_max = numbers.index(max(numbers))

    if index_max < index_min:
        return -1

    return sum(numbers[index_min:index_max + 1])