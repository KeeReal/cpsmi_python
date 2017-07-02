# coding=utf-8
# Реализовать алгоритм нахождения «расстояний» между словами.


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

# /* base case: empty strings */
# if (len_s == 0) return len_t;
# if (len_t == 0) return len_s;
#
# /* test if last characters of the strings match */
# if (s[len_s-1] == t[len_t-1])
#     cost = 0;
# else
#     cost = 1;
#
# /* return minimum of delete char from s, delete char from t, and delete char from both */
# return minimum(LevenshteinDistance(s, len_s - 1, t, len_t    ) + 1,
#                LevenshteinDistance(s, len_s    , t, len_t - 1) + 1,
#                LevenshteinDistance(s, len_s - 1, t, len_t - 1) + cost);
# }
