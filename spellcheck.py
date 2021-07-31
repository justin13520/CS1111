import urllib.request

# Get all the words in a list
url = 'http://cs1110.cs.virginia.edu/files/words.txt'
print('Type text; enter a blank line to end. ')
stream = urllib.request.urlopen(url)
lst = []
#lst is back up of the stream
for word in stream:
    words = word.decode('utf-8').strip()
    lst.append(words)
# Check user input
line = input('').split()
lst1 = []

for up1 in range(len(lst)):
    #copies lst of words and makes all upper to avoid case sensitivity
    #This is for the first line
    lst1.append(lst[up1].upper())


while line != []:
    #If the user puts in nothing, the while loop stops and the program terminates
    for k in range(len(line)):
        #gets rid of all things not a letter on either side
        line[k] = line[k].strip(".?!,;()\"'")

        if (line[k].upper() in lst1) & (k==len(line)-1):
            #line[k].upper() in lst1 checks if each element in line, which is the input,
            #is actually in the list of words created
            #line[k].upper() makes it so that it is case insensitive.
            #The k==len(line)-1 makes it so that once the whole line is read,
            #it asks for another input
            line = input('').split()
            continue
        elif (k==len(line)-1) & (line[k].upper() not in lst1):
            #if not in list, prints misspelled and tells you what is.
            print('  MISSPELLED: '+line[k])
            line = input('').split()
        elif (line[k].upper() not in lst1):
            print('  MISSPELLED: '+line[k])
        elif line[k] in lst1:
            #If the word is in list, moves on
            continue
