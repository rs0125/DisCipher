import codecs


def encode(n, string):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    temp = ''
    string = string.upper()
    if n == 13:
        return (codecs.encode(string, 'rot13')).upper()
    for i in string:
        if i.isalpha():
            shift = (letters.index(i) + n)
            if shift >= 26:
                shift = 26 - shift
            temp = temp + letters[shift]
        else:
            temp = temp + i
    return temp


def decode(n, string):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    temp = ''
    string = string.upper()
    while n > 13:
        n = 26 - n
    if n == 13:
        return (codecs.encode(string, 'rot13')).upper()
    for i in string:
        if i.isalpha():
            shift = (letters.index(i) - n)
            if shift >=  26:
                shift = 26 - shift
            temp = temp + letters[shift]
        else:
            temp = temp + i
    return temp


def rot3encode(s):
    return (codecs.encode(s, 'rot13')).upper()


def rot3decode(s):
    return ((codecs.decode(s, 'rot13'))).upper()
