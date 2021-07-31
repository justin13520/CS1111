GPA = 0
credits = 0
def add_course(x, y= None):
    global GPA
    global credits
    if y is None:
        credits += 3
        GPA = (GPA*(credits-3) + x * 3) / credits
    else:
        credits += y
        GPA = (GPA * (credits-y) + x * y) / credits
def gpa():
    global GPA
    return GPA
def credit_total():
    global credits
    return credits
