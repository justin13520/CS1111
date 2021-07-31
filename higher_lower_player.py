print('Think of a number between 1 and 100 and I\'ll guess it.')
guesses = int(input('How many guesses do I get? '))
count = 0
upper = 100
lower = 1
while count < guesses:
    c = int((upper+lower)//2)
    x = input('Is the number higher, lower, or the same as '+ str(c)+'? ')
    if x == 'lower':
        upper = c-1
        count += 1
    if x == 'higher':
        lower = c+1
        count += 1
    if x == 'same':
        print('I won!')
        count = guesses+1
    if lower > upper:
        print('Wait; how can it be both higher than '+str(lower)+' and lower than '+str(upper)+'?')
        count = guesses + 1
if count == guesses:
    ask = int(input('I lost; what was the answer? '))
    if ask<lower:
        print('That can\'t be; you said it was higher than '+str(lower-1)+'!')
    elif ask>upper:
        print('That can\'t be; you said it was less that '+str(upper)+'!')
    else:
        print('Well played!')

