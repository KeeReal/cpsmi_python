# coding=utf-8
# Дан текст. Найти множество встречающихся в тексте латинских букв.


# def get_all_latin
import re


def get_all_alphas(str):
    return re.findall('[a-zA-Z]', str)
