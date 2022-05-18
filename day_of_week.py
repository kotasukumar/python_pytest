def calculate(y, m, d):
    day_list = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    year = y - (14 - m) / 12
    x = year + year/4 - year/100 + year/400
    month = m + 12 * ((14 - m) / 12) - 2
    day = int(d + x + 31 * month / 12) % 7
    return day_list[day]


def test():
    result = calculate(2015, 3, 5)
    assert result == "thursday"
    print(result)
