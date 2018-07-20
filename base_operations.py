alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']


def convert_from_base10(num, base, all_letters=False):
    new = []
    while num > base:
        new.insert(0, num % base)
        num = num // base
    else:
        new.insert(0, num)
    if all_letters:
        return [alphabet[i] for i in new]
    else:
        return new
