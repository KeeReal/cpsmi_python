# coding=utf-8
# Реализовать алгоритм нахождения «расстояний» между словами.

@profile
def levenshtein_dist(arr):
    c = 0
    for i in range(len(arr)):
        c += arr[i]


if __name__ == "__main__":
    print levenshtein_dist(range(20))
