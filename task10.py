# coding=utf-8
# Подсчитать количество несовпадающих пар символов заданного текста (не считая
# пробелы!) при условии, что пары формируются с начала и с конца текста (1-й и последний
# символы, 2-й и предпоследний и т.д.).


def num_pairs(string):
    slen = len(string)
    half = len(string) / 2

    result = 0
    for i in range(half):
        left = string[i]
        right = string[slen - 1 - i]

        if left == ' ' or right == ' ':
            continue
        elif left == right:
            result += 1

    return result
