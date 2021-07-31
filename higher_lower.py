import random
ans = int(input('What should the answer be? '))
if ans == -1:
    ans = random.randrange(2,100)
guesses = int(input('How many guesses? '))
count = 0
while count <= guesses:
    guess = int(input('Guess a number: '))
    if guess == ans:
        print('You Win!')
        count = guesses+10
    elif count == guesses-1:
        print('You lose; the number was '+ str(ans))
        count = guesses+10
    elif guess > ans:
        print('The number is lower than that.')
        count += 1
    elif guess < ans:
        print('The number is higher than that.')
        count += 1

