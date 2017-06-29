# coding=utf-8
# В последовательности a(n) найти среднее арифметическое положительных элементов,
# расположенных после последнего нуля.


def avg_sum_after_last_zero(numbers):
    index_last_zero = -1
    for i in range(len(numbers)):
        if numbers[i] == 0:
            index_last_zero = i

    if index_last_zero == -1 or index_last_zero == len(numbers):
        return -1

    part = numbers[index_last_zero + 1:]
    if len(part) == 0:
        return -1

    return sum(part) / len(part)
