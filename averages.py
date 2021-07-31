def mean(a,b,c):
    return (a+b+c)/3
def median(a,b,c):
    if a > b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c
    else:
        if a > c:
            return a
        elif b < c:
            return b
        else:
            return c
def rms(a,b,c):
    x = mean(a**2, b**2, c**2)
    return x**.5
def middle_average(a,b,c):
    x = mean(a,b,c)
    y = median(a,b,c)
    z = rms(a,b,c)
    return median(x,y,z)