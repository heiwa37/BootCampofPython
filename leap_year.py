def leap_notleap(year):

    yr = ''
    if year <= 1917:
        if year % 4 == 0:
            yr = 'leap'
        else:
            yr = 'not leap'
    elif year >= 1919:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            yr = 'leap'
        else:
            yr = 'not leap'
    else:
        yr = 'none actually, since feb had only 14 days'

    return yr

year=int(input("please enter the year: "))
