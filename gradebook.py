points = {}
possible_points = {}
def assignment(kind,grade,weight=1):
    """
    The function assignment totals the points earned every assignment and keeps track of
    the running total amount of points that could have been earned in two dictionaries.
    :param kind: assignment type
    :param grade: 0-100 grade
    :param weight: usually one, relative to the others in its assignment type
    :return: total grades
    """
    global points
    global possible_points
    if points == {}:
        #this is in case assignment is called before total. It creates the assignmnet type,
        #and adds the grade in. This forces points to the else below.
        points[kind] = grade*weight
        possible_points[kind] = 100*weight
    else:
        if kind in points.keys():
            #If the kind of assignment exists already, then it just adds it to the total points
            #and adds 100*weight to possible points
            points[kind] += grade*weight
            possible_points[kind] += 100*weight
        else:
            #This is if the kind doesn't exist. This else adds it in and forces it into the
            #if statement above to add if that type of assignment comes up again.
            points[kind] = grade*weight
            possible_points[kind] = 100*weight

def total(proportions):
    """
    The function total calculates the grade by dividing current points by possible points,
    and then multiplying it by the ratio of the assignment type. This is then multiplied by
    100 to get a percent grade.
    :param proportions is the syllabus it takes in
    :return: the grade of the class
    """
    global points
    global possible_points
    x = 0
    if points == {}:
        #This is in case total is called before assignment function. It gives points and
        #possible_points the assignment types. This interacts with the first else in
        #the assignment function
        for key in proportions:
            points[key] = 0
            possible_points[key] = 0
    else:
        #This is the calculation part of total. This accounts for if there is a assignment type
        #not in the syllabus in the points dictionary, if just ignores it.
        for key in proportions:
            if key in points and possible_points[key] != 0:
                #When the points dictionary does not have all the keys filled with values
                #greater than 0, it prevents it from calculating to avoid division by 0.
                x += (points[key] / possible_points[key]) * proportions[key] * 100
    return x