# coding=utf-8
# Реализовать алгоритм нахождения «расстояний» между словами.

@profile
def levenshtein_dist(s, len_s, t, len_t):
    if len_s == 0:
        return len_t

    if len_t == 0:
        return len_s

    cost = 0
    if s[len_s - 1] == t[len_t - 1]:
        cost = 0
    else:
        cost = 1

    return min(
        levenshtein_dist(s, len_s - 1, t, len_t) + 1,
        levenshtein_dist(s, len_s, t, len_t - 1) + 1,
        levenshtein_dist(s, len_s - 1, t, len_t - 1) + cost,
    )


if __name__ == "__main__":
    str1 = 'Lorem.'
    str2 = 'Donec posuere.'
    print levenshtein_dist(str1, len(str1), str2, len(str2))
