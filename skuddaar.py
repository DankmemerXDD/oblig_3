def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    if year % 4 != 0:
        return False
    if year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return False

