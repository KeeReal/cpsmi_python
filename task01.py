# coding=utf-8
# Введенную с клавиатуры строку вывести на экран наоборот (использовать цикл).


def reverse_string(string):
    result = ""
    length = len(string)
    for i in range(length):
        result += string[length - i - 1]
    return result


if __name__ == '__main__':
    print 'type q to quit'
    string = ''
    while string != 'exit':
        string = raw_input("any string: ")
        print 'reverse: %s' % reverse_string(string)
