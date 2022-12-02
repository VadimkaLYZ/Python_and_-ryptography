#Програма шифрування на основі перестановочного шифру
import pyperclip

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    #Відобразити зашифровану строку в буфер обміну
    #ciphertext, вставив після неї символ '|' на випадок, якщо
    #в кінці зашифрованого повідомлення є пробіли
    print(ciphertext + '|')

    #Скопіювати зашифровану строку в буфер обміну
    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    #Кожна строка в списку ciphertext представляє стовбець таблиці
    ciphertext = [''] * key

    #Цикл по всім стовпцям в списку ciphertex
    for column in range(key):
        currentIndex = column

        #Цикл, поки значення currentIndex не буде більше чим довжина повідомлення
        while currentIndex < len(message):
            #Помістити в кінець даного стовпця в списку ciphertext
            #символ повідомлення з індексом currentIndex
            ciphertext[column] += message[currentIndex]

            #Збільшити значення currentIndex
            currentIndex += key

    #Повернення списка ciphertext в виді єдиної строки
    return ''.join(ciphertext)

if __name__=='__main__':
    main()