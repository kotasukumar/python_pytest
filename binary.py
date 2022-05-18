def binary(num):
    power_of_two = []
    while num != 1:
        num = int(num / 2)
        power_of_two.append(num)
    return num


def test_my_test():
    result = binary(10)
    assert result == 1

