import math


def math_power(base, exponent):
    result = 1
    for i in range(exponent):
        result = result * base

    return result


def cal_interest(year, principle, rate):
    r = rate / (12 * 100)
    months = (12 * year)
    return (principle * r) / 1 - math_power((1 + r), months)


def test():
    result = cal_interest(5, 10000, 12)
    assert result >= 98.18
    print("intertest rate: ", result)
