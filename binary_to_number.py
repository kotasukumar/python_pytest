def to_number(number):
    remainders = []
    for i in range(2):
        b = []
        for j in range(4):
            num = number % 2
            number = int(number / 2)
            b.append(num)
        remainders.append(b)
    temp = remainders[0]
    remainders[0] = remainders[1]
    remainders[1] = temp
    result = convert_to_binomial(remainders)
    return result


def convert_to_binomial(remainder):
    a = []
    for i in range(2):
        for j in range(4):
            a.append(remainder[i][j])
    n = 6
    result = 0
    for i in range(7):
        result = result + (a[i] * power(2, n))
        n -= 1
    return result


def power(base, expon):
    value = 1
    for i in range(expon):
        value = value * base
    return value


def test():
    rem = to_number(10)
    assert rem == 2
