#Шифрування/дешифрування файлів з допомогою перестановочного шифру

import time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():
    inputFilename = 'file/frankenstein.txt'
    #Будьте уважні: якщо файл з іменем outputFilename
    #вже існує, програма перезапише його
    outputFilename = 'file/frankenstein.encrypted.txt'
    myKey = 10
    myMode = 'encrypt'

    #Якщо вхідного файлу не існує, програма завершується
    if not os.path.exists(inputFilename):
        print("The file %s does not exist. Quitting..." % (inputFilename))
        sys.exit()

    #Яущо вихідний файл існує, задати користувачу питання
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    #Прочитати файл з вхідного файлу
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print("%string..." % (myMode.title()))

    #Виміряти, як довго відбувається шифрування/дешифрування
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s second' % (myMode.title(), totalTime))

    #Записати трансльованк повідомлення в вихідний файл
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s character).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))

if __name__ == '__main__':
    main()

