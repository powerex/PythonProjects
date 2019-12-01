import datetime


def get_easter_day(year: int) -> datetime:
    x = year
    a = x % 19
    b = x % 4
    c = x % 7
    d = (19 * a + 15) % 30
    e = (2 * b + 4 * c + 6 * d + 6) % 7
    f = int(d + e)
    if f <= 9:
        day = datetime.date(x, 3, 22)
        day += datetime.timedelta(days=f)
    else:
        f -= 3
        day = datetime.date(x, 4, f)
        day -= datetime.timedelta(days=6)
    if x / 100 > 18:
        day += datetime.timedelta(days=13)
    return day


def is_cirio(day: datetime) -> bool:
    return day == datetime.date(day.year, 4, 7)


# print(get_easter_day(2002))

for i in range(1986, 2076):
    d = get_easter_day(i)
    if is_cirio(d):
        print(d, "Cirio")
    else:
        print(d)
