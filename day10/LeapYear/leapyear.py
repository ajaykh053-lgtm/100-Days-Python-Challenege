def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print((is_leap_year(2000)))
print((is_leap_year(2020)))
print((is_leap_year(2024)))
print((is_leap_year(2400)))
print((is_leap_year(1700)))
print((is_leap_year(2100)))

"""Docstring
its docstring 
it aollows us to make multiple line as comments"""
