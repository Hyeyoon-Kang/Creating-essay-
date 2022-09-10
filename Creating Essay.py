'''
This program aims to read a selected text and choose random words to form a paragraph 
by putting the random words together into a paragrph form. The program will also remove punctuation
and be able to categorize words by their alphabetical order and length 

Author: Hyeyoon Kang
Student Number: 20205774
Date: November. 2021 

'''
global longestWordLength 

#define global variables
longestWordLength = 0

#import necessary modules to run the program 
import ssl
import urllib.request #to read a website 
import string
import random 

#define writeToFile to be used when called 
def writeToFile(text):
    """
    This function takes a string as a parameter and opens a file called "essay.txt" and writes the 
    text string to the file.
    Parameters: text - string that adds words 
    Return: strings that get written into the file essay.txt
    """
    #use while loop to check that the text is opened successfully
    while True:
        #try function will loop through until the file is open 
        try:
            #set a variable equal to text opening 
            textFile = open(text, 'a')
            #exit loop 
            break
        #using except would display message if a file did not open 
        except IOError:
            print('Could not open file!')
    
    #set so strings will be written into the file 
    textFile.write(text)
    
    #close file
    textFile.close()

def readWebPage(url):
    """
    This function takes one parameter, the URL from which to read the text, and it returns a list where 
    each element is a word in the text found on the website. The function will read the contents of the 
    website into a string and convert the string to a list of words.
    Parameters: url - source that contains list of words 
    Return: list of words from the url 
    """
    #use try to make sure the url opens 
    try:
        #set wordList as an empty list 
        wordList = []
        #prevents unverified errors 
        ssl._create_default_https_context = ssl._create_unverified_context
        #opens url 
        response = urllib.request.urlopen(url)
        #reads through url 
        data = response.read().decode('utf-8')
        #splits the words in the text from url 
        wordList = data.split()

        return wordList
    #except incase the Url does not open 
    except IOError:
        print('Url was not opened successfully')
        return []

def convertToDictionary(wordList):
    """
    This function takes list of word in the text found on the website and returns a dictionary of key/value 
    pairs where the value is a list of words that all begin with the same letter and are the same length.
    Parameters: wordList - list of words from the text 
    Return: words to dictionary in alphabetical and length order
    """
    #making a copy of the list 
    lst = wordList
    
    #make a dictionary variable 
    dictionary = {}
    #goes through the all the words in the list and measures length of each word
    for i in range(len(lst)):
        #indicate first letter of the word 
        firstCharacter = lst[i][0:1]
        #measure word length 
        wordLength = len(lst[i])
        #declare key as the first letter and the length number
        key = firstCharacter + wordLength. join(key) 

        #check if the key already exists 
        #if it does not exists the if statement will not run
        if dictionary.get(key, 0) == 0:
            #set a list to put all the words into a key made
            temporaryList = ()
            #runs through all the words that fits key to put into temporaryList
            for i in range(len(lst)):
                #if the word's letter and length matches existing key add to the list
                if firstCharacter == lst[i][0:1] and wordLength == len(lst[i]):
                    #add to the list 
                    list.append(temporaryList[i])
                                          
def removePunctuation(wordList):
    """
    This function takes list of words from the created list and removes punctuation marks that appear at the 
    end of some of the words. 
    Parameters: wordList - list of words from the text 
    Return: None 
    """
    #set newList as empty list for now 
    newList = []
    #runs through all the words in the wordList
    for i in wordList:
        #goes through each letter in each words of the wordlist
        for letter in i:
            #considers punctuation behind each string letter 
            if letter in string.punctuation:
                #replaces punctuation with blank 
                i = i.replace(letter, "")
        #adds new words with no punctuation
        newList.append(i)

def makeParagraph (dictionaryOfWords, numberofWords):
    """
    This function takes the dictionary of words and creates a paragraph (a string) consisting of numberofWords 
    word. 
    parameter: dictionaryOfWords - dictionary that contains list of words 
             : numberofWords - total numberofWords contained in a paragraph 
    return: paragraph
    """
    paragraph = ""
    #runs through each letter to create a paragraph with given random generation
    for i in range(numberofWords):
        while True:
            #must be within range of 1 to longestword 
            randNumber = random.randint(1, longestWordLength)
            randLetter = random.choice(string.ascii_letters.lower())
            #random number and letter concatenated makes up the key value 
            key = randNumber + randLetter 
            
            #makes sure the key exists within 
            if dictionaryOfWords.get(key, 0) != 0:
                #adds up random words into the list 
                paragraph += random.choice(dictionaryOfWords.get(key))
                
                #checks to make sure it loops right amount of time 
                if i != numberofWords:
                    #adds a space after everyword 
                    paragraph += " "
                #breaks the loop 
                break
        #adds period at the end 
        paragraph += "."
        
        return paragraph

def createEssay(dictionaryOfWords):
    """
    This function asks the user for number of paragraphs and words and generates essay based on the info
    inputted by the user 
    Parameter: dictionaryOfWords - strings that contain words that make up list of words to be used in essay
    Return: essay
    """
    #user determines number of paragraph and words per paragraph 
    numberOfParagraph = int(input('Please enter how many paragraph to generate: '))
    numberOfWords = int(input('Please enter number of words per paragraph: '))
    
    #sets variable essay to empty 
    essay = ""
    #checks to see that chosen paragraph and word is within the range
    for i in range(numberOfParagraph):
        #make essay value to add every word to paragraph
        essay += makeParagraph(dictionaryOfWords, numberOfWords)
        #add a new line after every paragraph 
        essay += "\n"
        
    return essay 

def main():
    text = 'essay.txt'
    writeToFile(text)
    url = 'https://www.cs.queensu.ca/home/cords2/cs.txt'
    wordList = readWebPage(url)
    convertToDictionary(wordList)
    dictionaryOfWords = removePunctuation(wordList)
    numberofWords = len(wordList)
    makeParagraph(dictionaryOfWords, numberofWords)
    createEssay(dictionaryOfWords)

main()