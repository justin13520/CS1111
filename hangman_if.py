word = input('Enter word: ')
underscored = ''
for letter in word:
    underscored+=' '+'_'
print(underscored)
while '_' in underscored:
    guess = input('Guess a letter: ')
    if guess in word:
        underscored= underscored.replace(guess+'_', guess+guess)
        print(underscored[1::2])
        #suppose to print with under scored
