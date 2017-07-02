# coding=utf-8
# Написать программу, умеющую делать так:
# «По рзелульаттам илссеовадний одонго анлигйсокго унвиертисета, не иеемт занчнеия, в кокам пряокде рсапожолены бкувы в солве. Галвоне, чотбы преавя и пслоендяя бквуы блыи на мсете. Осатьлыне бкувы мгоут селдовтаь в плоонм бсепордяке, все-рвано ткест чтаитсея без побрелм. Пичрионй эгото ялвятеся то, что мы не чиатем кдаужю бкуву по отдльенотси, а все солво цликеом.»


# input string
# split by words
# shuffle letters in each word but first and last
# join???

import random

PUNCTUATION = list(" ,.-!")

str = "Dear president Blatter, colleagues of the executive committee."


# for i in range(len(str)):

# ok
def shuffle_word(word, seed=None):
    if seed is not None:
        random.seed(seed)

    if len(word) <= 3:
        return word

    shuffled = word[0]
    mid = list(word[1:-1])

    while len(mid) > 0:
        ind = random.randint(0, len(mid) - 1)
        shuffled += mid.pop(ind)

    return shuffled + word[-1]


def shuffle_text(text, seed=None):
    result = ""
    word = ""
    for i in range(len(text)):
        ch = text[i]
        if ch in PUNCTUATION:
            if len(word) > 0:
                result += shuffle_word(word, seed)
                word = ''
            result += ch
        else:
            word += ch
    return result