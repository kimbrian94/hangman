from sys import argv
from random_words import *

rw = RandomWords()
answer = rw.random_word() # randomly generate a word
answerList = list(answer)
solved = False # boolean for whether the word is solved
attemptNum = 10 # numbers of attempts given
correctNum = 0 # number of correct attempts
difficulty = 'normal'

# according to each difficulty randomly generate a word until 
# a number of specific characters is generated
if len(argv) == 2:
    difficulty = argv[1]
    if difficulty == 'easy':
        while(len(answerList) != 5):
            answer = rw.random_word()
            answerList = list(answer)
    elif difficulty == 'normal':
        while(len(answerList) != 6):
            answer = rw.random_word()
            answerList = list(answer)
    elif difficulty == 'hard':
        while(len(answerList) != 7):
            answer = rw.random_word()
            answerList = list(answer)
    else:
        print("Enter a valid difficulty")
        exit(0)
else:
    while(len(answerList) != 6):
        answer = rw.random_word()
        answerList = list(answer)


#copy list of alphabets of answer to point it to wordList list
wordList = answerList.copy()

# set the wordList elements to be underscore (_) for not yet found
i = 0
while(i < len(wordList)):
    wordList[i] = '_'
    i += 1

print(answer)

print(
"""|---------------------------|
|[H] [A] [N] [G] [M] [A] [N]|
|---------------------------|""")

# run while puzzle is not solved and there are at least one attempt left
while solved == False and attemptNum > 0:
    # current game output
    print("________________________")
    print("Number of attempts: {}".format(attemptNum))
    if difficulty == 'easy':
        print("Current: {} {} {} {} {}".format(wordList[0], wordList[1], wordList[2], \
            wordList[3], wordList[4]))
    elif difficulty == 'normal':
        print("Current: {} {} {} {} {} {}".format(wordList[0], wordList[1], wordList[2], \
            wordList[3], wordList[4], wordList[5]))
    elif difficulty == 'hard':
        print("Current: {} {} {} {} {} {} {}".format(wordList[0], wordList[1], wordList[2], \
            wordList[3], wordList[4], wordList[5], wordList[6]))
    guess = input("> ") # take input from user
    
    #if given input is composed of alphabetical characters
    if guess.isalpha() == True and len(guess) == 1:
        i = 0
        while(i < len(answerList)):
            if wordList[i] == '_' and answerList[i] == guess: # correct guess
                print("Correct guess!")
                wordList[i] = guess
                correctNum += 1
                break
            i += 1
            if i == len(answerList): # wrong guess
                print("Try again!")
                attemptNum -= 1
        
        if correctNum == len(wordList):
            print(f"You win! The word was: {answer}")
            solved = True
        elif attemptNum == 0:
            print(f"You lose! The word was: {answer}")
    
    # if given input was a whole word check
    elif guess.isalpha() == True and len(guess) > 1:
        if guess == answer:
            print(f"You win! The word was: {answer}")
        else:
            print(f"You lose! The word was: {answer}")
        break

    # input given is not composed of alphabetical characters
    else:
        print("Enter alphabets only!")
