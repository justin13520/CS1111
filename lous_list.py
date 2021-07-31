import urllib.request
url = 'http://cs1110.cs.virginia.edu/files/louslist/'
def instructors(department):
    """
    The function instructors takes in the url of department's courses and finds the
    instructors and then sorts them alphabetically. No instructor is repeated.
    :param department: Department wanted, added on to the end of url to find the courses
    :return:list of instructors in the department in alphabetical order
    """
    global url
    stream = urllib.request.urlopen(url+department)
    lst = []
    for line in stream:
        course = line.decode('utf-8').split('|')
        for i in course[4]:
            if '+' in course[4]:
                a = course[4].index('+')
                course[4] = course[4][0:a]
            if course[4] not in lst:
                lst.append(course[4])
    lst.sort()
    return lst
def class_search(dept_name, has_seat_available=True, level = None, not_before=None, not_after=None):
    """
    class_search function takes in parameters and matches them to each line on the website.
    If all the parameters match that line, that course's line is added to a list and then that list is
    returned, a filter mechanic
    :param dept_name: department name wanted
    :param has_seat_available: True or False value. If True, has to check if there is seats, if not,
    moves on
    :param level: course number. Same level or any level, ie 3000 can have 3102, 3100, 3560, ect.
    :param not_before: Time that the classes are not suppose to  start before or anytime start if not_after is also equal to None
    :param not_after: Time that the classes are not suppose to start after or anytime start if not_before is also equal to None
    :return:list of lists that match the parameters
    """
    global url
    stream = urllib.request.urlopen(url + dept_name)
    lst = []
    for line in stream:
        course = line.decode('utf-8').split('|')
        if has_seat_available:
            if int(course[15]) < int(course[16]):
                if level == None:
                    if not_before == None:
                        if not_after == None:
                            lst.append(course)
                        else:
                            if not_after >= int(course[12]):
                                lst.append(course)
                            else:
                                continue
                    else:
                        if int(course[12]) >= not_before:
                            if not_after == None:
                                lst.append(course)
                        else:
                            continue
                else:
                    if int(course[1]) // 1000 == level / 1000:
                        if not_before == None:
                            if not_after == None:
                                lst.append(course)
                        else:
                            if int(course[12])>= not_before:
                                if not_after == None:
                                    lst.append(course)
                                else:
                                    if int(course[12])<=not_after:
                                        lst.append(course)
                                        continue
                                    else:
                                        continue
                            else:
                                continue
                    else:
                        continue
            else:
                continue
        else:
                if level == None:
                    if not_before == None:
                        if not_after == None:
                            lst.append(course)
                        else:
                            if not_after >= int(course[12]):
                                lst.append(course)
                            else:
                                continue
                    else:
                        if int(course[12]) >= not_before:
                            if not_after == None:
                                lst.append(course)
                        else:
                            continue
                else:
                    if int(course[1]) // 1000 == level / 1000:
                        if not_before == None:
                            if not_after == None:
                                lst.append(course)
                            else:
                                if not_after>=int(course[12]):
                                    lst.append(course)
                                else:
                                    continue
                        else:
                            if int(course[12])>= not_before:
                                if not_after == None:
                                    lst.append(course)
                                else:
                                    if int(course[12])<=not_after:
                                        lst.append(course)
                                        continue
                                    else:
                                        continue
                            else:
                                continue
                    else:
                        continue
    return lst