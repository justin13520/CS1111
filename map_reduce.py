def mymap(func,lst):
    '''Purpose of mymap is to perform the function on each number in the list.
    :func is the function to be performed. lst is the list that the function will
    :perform on.
    '''
    y = list(lst)
    for increment in range(0,len(lst)):
        y[increment] = func(lst[increment])
    return y
def myreduce(func,lst):
    '''purpose of myreduce is to perform the function on the first two numbers in the list, then
    :perform the function on the number found and the next number and repeat
    '''
    x = lst[0]
    y = list(lst)
    for increment in range(1,len(lst)):
        y[increment] = func(x,y[increment])
        x = y[increment]
    return y[len(y)-1]