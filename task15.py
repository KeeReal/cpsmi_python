# coding=utf-8
# За минимальное количество шагов проверить, есть ли в упорядоченной по убыванию
# последовательности a(n) некоторая величина b. Если есть, то указать ее порядковый номер.

def contains(v, arr):
    if len(arr) == 0:
        return False

    # best case :)
    if arr[0] < v or arr[-1] > v:
        return False

    if arr[0] == v or arr[-1] == v:
        return True

    get_half = lambda l, r: l + (r - l) / 2

    left = 0
    right = len(arr) - 1
    half = get_half(left, right)  # left + (right - left) / 2
    while half != left and half != right:
        # print "l:%d h:%d r:%d" % (left, half, right)
        if arr[half] == v:
            return True
        elif arr[half] > v:
            left = half
            half = get_half(left, right)
        elif arr[half] < v:
            right = half
            half = get_half(left, right)
    return False