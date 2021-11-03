word = "malayalam"
listOfIndeciesToIgnore = []

def game():
    lengthOfWord = len(word)
    print("Its a " + str(lengthOfWord) + " lettered word\nYou have 10 lives/attempts")
    x = 0
    numberOfGuesses = 10
    hiddenWord = ""

    for i in range(lengthOfWord):
        hiddenWord += "_"

    listofHiddenWord = list(hiddenWord)

    while numberOfGuesses != 0:
        if hiddenWord == word:
            print("You got it all correct gg ez\nWord: " + word)
            break
        letter = input("Enter the letter ")
        checkBoolean, i = check(letter)
        if checkBoolean:
            print("You got it right")
            listofHiddenWord[i] = letter
            hiddenWord = "".join(listofHiddenWord)
            print("Word: " + hiddenWord)
        else:
            numberOfGuesses -= 1
            print("You got it wrong\nNumber of guesses left " + str(numberOfGuesses))
        #x += 1
        
        if numberOfGuesses <= 0:
            print("You are hanged")
            break

def check(letter):
    #flag = True
    for x in range(len(word)):
        if not x in listOfIndeciesToIgnore:
            #print(x in listOfIndeciesToIgnore)
            if word[x] == letter:
                listOfIndeciesToIgnore.append(x)
                return True, x
    if x == len(word) - 1:
        return False, 0


game()