import math

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']


def num_to_string(num):
    if num > 9:
        return str(alphabet[num - 10])
    else:
        return str(num)


def string_to_num(numstr):
    if numstr.isalpha():
        return int(alphabet.index(numstr)) + 10
    else:
        return int(numstr)


def convert_from_base10(num, base, all_letters=False):
    new = []
    while num >= base:
        new.insert(0, num % base)
        num = num // base
    else:
        new.insert(0, num)
    if all_letters:
        return ''.join([alphabet[i] for i in new])
    else:
        return ''.join([num_to_string(i) for i in new])


def convert_to_base10(numstr, base, all_letters=False):
    number = 0
    chars = list(numstr)
    length = len(chars)
    for char in chars:
        length -= 1
        if all_letters:
            num = alphabet.index(char)
        else:
            num = string_to_num(char)
        number += num * base**length
    return number


def number_of_digits(num, base):
    return int(math.log(num, base) + 1)
