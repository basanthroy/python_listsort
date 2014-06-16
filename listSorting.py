#!/usr/bin/python
import re
import sys

# Python program to sort strings and integers from a file and output to
# a different file.





# Regex to match non-numeric characters
INT_RE = re.compile(r"^[-]?\d+$")






# This function checks whether the input argument is a number.
# 
# Returns true if the arg is a number. Else returns false
#
# I got this regex check from http://stackoverflow.com/questions/1265665
def RepresentsInt(s):
    return INT_RE.match(str(s)) is not None







# This function removes all non-alphanumeric characters from the
# input string. However, if the input string start with a '-' char
# and if the rest of the string is a number, then it retains the
# '-' char at the 0th element.
#
# Returns a string stripped of non-alpahnumeric characters 
# (unless starts with '-'
def cleanWord(word):
    if str(word).startswith('-') and \
        RepresentsInt(re.sub("[^A-Za-z0-9 ]","",word,re.UNICODE)):
        return '-' + re.sub("[^A-Za-z0-9 ]","",word,re.UNICODE)
    else:
        return re.sub("[^A-Za-z0-9 ]","",word,re.UNICODE)   
   





        
# THis is the main processing method which
#    1. Opens and closes input and output files
#    2. splits the input string into component strings to construct a list
#    3. Loops in a nested way through this list.
#    4. Loops through the list and performs Selection-Sort on it with a twist.
#       The twist is that at each loop, if the current element is a string, then 
#       the inner loop iteration is restricted to strings. If the current element is an int, 
#       then the inner loop iteration is restricted to ints.
#    5. Completes Selection-Sort with O(N^2) time complexity and O(1) space complexity
def sortFile():
    
    # Check the number of arguments to the program
    if len(sys.argv) != 3:
        print "Incorrect number of arguments"
        return

    # try opening both input and output files
    try:
        fileInput = open(sys.argv[1], "r")
        fileOutput = open(sys.argv[2], "w")
    except:
        print "There was a problem opening either the input or the output file."
        print "Please try again with a valid file path/name"
        return
    
    inputLine = fileInput.read()
    
    # Initialize variables
    cleanedWords = inputLine.split()
    numWords = len(cleanedWords)
    cleanedWords = [cleanWord(word) for word in cleanedWords]
    
    
    # There is a nested loop in this program in order to implement Selection-Sort
    # The outer loop loops through the whole list; While the inner loop only 
    # goes through the rest of the list.
    for outerLoop in range(0, numWords):
        
        smallerValue = cleanedWords[outerLoop]
        currentValueIsInt = RepresentsInt(cleanedWords[outerLoop])
        foundSmallerValue = False
        smallerValueIndex = outerLoop + 1
        for innerLoop in range(outerLoop + 1, numWords):
            
            # While looping, first check if the outerLoop element is a string or an int.
            # THe inner loop should only be looped though elements of the same data type.
            # This is to conform to the program requirement that the nth element should
            # retain the same datatype as the original pre-sort string
            if (currentValueIsInt and not RepresentsInt(cleanedWords[innerLoop])) or \
                (not currentValueIsInt and RepresentsInt(cleanedWords[innerLoop])):
                continue
            
            # For the inner loop, the objective is to find the smallest element in the inner loop.
            # So it executes a comparison operator.
            if currentValueIsInt:
                if RepresentsInt(cleanedWords[innerLoop]) and int(smallerValue) > int(cleanedWords[innerLoop]):
                    foundSmallerValue = True
                    smallerValueIndex = innerLoop
                    smallerValue = cleanedWords[innerLoop]
                    currentValueIsInt = True
                else:
                    continue
            else:
                if RepresentsInt(cleanedWords[innerLoop]) or \
                    ((not RepresentsInt(cleanedWords[innerLoop])) and smallerValue > cleanedWords[innerLoop]):
                    foundSmallerValue = True
                    smallerValueIndex = innerLoop
                    smallerValue = cleanedWords[innerLoop]
                    if RepresentsInt(cleanedWords[innerLoop]):
                        currentValueIsInt = True
                    else:
                        currentValueIsInt = False
                else:
                    continue
        if foundSmallerValue:
            temp = cleanedWords[outerLoop]
            cleanedWords[outerLoop] = cleanedWords[smallerValueIndex]
            cleanedWords[smallerValueIndex] = temp
    
    
    # Constructs the output string and then writes it to a file
    # after stripping the last trailing whitespace
    newLine = ""
    for word in cleanedWords:
        newLine += (word + ' ')
    fileOutput.write(newLine.strip())
    fileOutput.write('\n')
    

    # Try closing the files
    try:
        fileInput.close()
        fileOutput.close()
    except:
        print "There was a problem closing either the input or the output file."
        print "The output file may not have been printed correctly"
        return
    
    print "String list sorted successfully. Please check the output file at " + sys.argv[2]
# END OF sortFile() method



# Invoke the main processing method
sortFile()





