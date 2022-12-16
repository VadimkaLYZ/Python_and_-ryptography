#Модуль розпізанавання англійської мови

#Щоб використовувати даний модуль, введіть наступний код:
#   import detectEnglish
#   detectEnglish.isEnglish(someString) #Повертає True or False
#В каталозі програми повинен існувати файл dictionary.txt,
#маючи по одному слові в строці.
UPPERLETTERS ='ABCDEFGHIJKLMNOPQRSTUVWXXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    dictionaryFile = open('file/dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0 # слова відстутні, тому повертає 0.0

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1

    return float(matches) / len(possibleWords)

def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def isEnglish(message, wordPercentage=20, letterPercentage=85):
    #За заумовчуванням 20% слів повині бути в файлі словаря,
    #а 85% символів повідомленея повині бути буквами або
    #пробілами(а не знаками або числама)
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch