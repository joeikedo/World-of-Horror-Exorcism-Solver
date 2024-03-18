def addLetterHelper(index, inputString):
    if(index == 0):
        return inputString + 'B'
    else:
        return inputString + 'C'


def listElementAddHelper(inputList):
    returnList = []
    for element in inputList:
        returnList.append(element + 'B')
        returnList.append(element + 'C')

    return returnList

def generateEveryPossiblePermutation2(numOfCharacters):
    returnList = ['B', 'C']
    if (numOfCharacters == 1):
        return returnList
    else:
        for i in range(numOfCharacters):
            returnList = listElementAddHelper(returnList)
        return returnList


# TODO: For fun, refactor this to be a function with variable number of characters, not just 5 hardcoded loops.
def generateEveryPossiblePermutation():
    permutationList = []
    currentPermutationString = ''
    for i in range(2):
        currentPermutationString = addLetterHelper(i, currentPermutationString)
        for j in range(2):
            currentPermutationString = addLetterHelper(j, currentPermutationString)
            for k in range(2):
                currentPermutationString = addLetterHelper(k, currentPermutationString)
                for l in range(2):
                    currentPermutationString = addLetterHelper(l, currentPermutationString) 
                    for m in range(2):
                        currentPermutationString = addLetterHelper(m, currentPermutationString) 
                        permutationList.append(currentPermutationString)
                        # Remove last character of string to clear for next iteration of this loop.
                        currentPermutationString = currentPermutationString[:-1] 

                    # Clear fourth (l) iteration         
                    currentPermutationString = currentPermutationString[:-1]   

                # Clear third (k) iteration         
                currentPermutationString = currentPermutationString[:-1]   

            # Clear second (j) iteration         
            currentPermutationString = currentPermutationString[:-1]     

        # Clear outermost (i) iteration
        currentPermutationString = ''
    
    return permutationList
        

def main():
    list = generateEveryPossiblePermutation()
    print(list)
    print(len(list))

    list = generateEveryPossiblePermutation2(4)
    print(list)
    print(len(list))


if __name__ == '__main__':
    main()