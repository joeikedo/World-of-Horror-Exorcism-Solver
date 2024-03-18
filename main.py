# TODO: Could add option for locking first two actions given from Rooftop Girl? Meh, idk...

def listElementAddHelper(inputList):
    returnList = []
    for element in inputList:
        returnList.append(element + 'B')
        returnList.append(element + 'C')

    return returnList

def generateEveryPossiblePermutation(numOfCharacters):
    returnList = ['B', 'C']
    if (numOfCharacters == 1):
        return returnList
    else:
        for i in range(numOfCharacters - 1):
            returnList = listElementAddHelper(returnList)
        return returnList


def checkElementIsMatchHelper(attemptedPermutation, listElement, numCharsThatShouldMatch):
    numCharsThatShouldNotMatch = len(attemptedPermutation) - int(numCharsThatShouldMatch)
    matchCounter = 0
    notMatchCounter = 0
    for i in range(len(listElement)):
        if(listElement[i] == attemptedPermutation[i]):
            matchCounter += 1
        else:
            notMatchCounter += 1
        
        if( (matchCounter > int(numCharsThatShouldMatch)) or (notMatchCounter > numCharsThatShouldNotMatch)):
            return False
    
    return True


def narrowDownList(possiblePermutationsList, attemptedPermutation, numberCharsCorrect):
    returnList = []
    for element in possiblePermutationsList:
        if(checkElementIsMatchHelper(attemptedPermutation, element, numberCharsCorrect)):
            returnList.append(element)
    
    print(returnList)
    return returnList


def main():
    possiblePermutationsList = generateEveryPossiblePermutation(3)
    print(possiblePermutationsList)
    while(True):
        attemptedPermutation = input("Enter attempted permutation: ")
        numberCharsCorrect = input("Enter number of chars correct: ")
        print(attemptedPermutation)
        print(numberCharsCorrect)
        possiblePermutationsList = narrowDownList(possiblePermutationsList, attemptedPermutation, numberCharsCorrect)


if __name__ == '__main__':
    main()