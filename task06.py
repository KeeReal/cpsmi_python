# coding=utf-8
# В матрице a(n, m) поменять местами столбцы с минимальным и максимальным
# количествами четных элементов. Матрица — список списков.

# a[row][col]


def swap_min_max_cols(rows, cols, mat):
    if cols <= 1:
        return mat

    # array of zeroes with len of rows
    counters = []
    while len(counters) < cols:
        counters.append(0)

    # count num even numbers
    for x in range(cols):
        for y in range(rows):
            if mat[y][x] % 2 == 0:
                counters[x] += 1

    index_min = counters.index(min(counters))
    index_max = counters.index(max(counters))

    # swap
    for y in range(rows):
        temp = mat[y][index_min]
        mat[y][index_min] = mat[y][index_max]
        mat[y][index_max] = temp

    return mat
