# coding=utf-8
# В квадратной матрице a(n, n) в каждой строке элемент, расположенный на диагонали,
# увеличить на значение минимального элемента соответствующего столбца. Матрица —
# список списков.


def increase_items_at_main_diag(size, mat):
    # for each col find y of min element
    col_mins = []
    while len(col_mins) < size:
        col_mins.append(None)

    for x in range(size):
        for y in range(size):
            if col_mins[x] is None:
                col_mins[x] = mat[y][x]
            elif col_mins[x] > mat[y][x]:
                col_mins[x] = mat[y][x]

    for i in range(size):
        mat[i][i] += col_mins[i]

    return mat
