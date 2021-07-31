def check(num):
    '''input is always a postive integer
    :rule is starting on last number, add every other number backwards, then double the remaining number
    :and add up their individual digits. If total%10 is 0, valid card number'''
    part1 = 0
    part2 = ''
    part3 = 0
    num = str(num)
    for i in num[-1::-2]:
        #This is to find the rightmost and every other working backwards
        x = int(i)
        part1 += x
    for i in num[-2::-2]:
        #This is to find the remaining numbers working backwards and doubling the values, all in
        #str form
        part2 += str(int(i)*2)
    for i in range(len(part2)):
        #This is to seperate the digits and add them
        part3 += int(part2[i])
    if (part1 + part3)%10==0:
        return True
    else:
        return False

print(check(5))