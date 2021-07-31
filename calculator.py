def binop(calc):
    '''This function takes a string that is an equation and calculates the value.
    :Each conditional isolates the parts of the equation before and after the operator.
    :This is done by going through the string in a loop and finding the index of the operator.
    :The two numbers are then found and typecasted into ints, which are then performed by the
    :operator found.
    '''
    count = 0
    while count < len(calc):
        if calc[count] == '+':
            a = int(calc[0:count])
            b = int(calc[count+1:])
            return a + b
        elif calc[count] == '-':
            a = int(calc[0:count])
            b = int(calc[count + 1:])
            return a-b
        elif calc[count] == '*':
            a = int(calc[0:count])
            b = int(calc[count + 1:])
            return a*b
        elif calc[count] == '/':
            a = int(calc[0:count])
            b = int(calc[count + 1:])
            return a/b
        elif count == len(calc)-1:
            return int(calc)
        else:
            count += 1
