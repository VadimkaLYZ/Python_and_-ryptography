#Програма дешифрування перестановочного шифру

import math, pyperclip

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = decryptMessage(myKey, myMessage)

    #Вивести текст з закінчими символом '|' на випадок
    #якщо в кінці дешифрованого повідомлення є пробіли

    print(plaintext + '|')

    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    #Функція розшифрування перестановочного шифру буде імітувати
    #стовпці і строки таблиці, в які вписаний простий текст,
    #використовуючи список строк. Спочатку обчислюємо декілька значень.

    #Кількість стовпців в перестановачні таблиці
    numOfColumns = int(math.ceil(len(message) / float(key)))
    #Кількість строк в таблиці
    numOFRows = key
    #Кількість "заштрихованих" ячейок в останьому стовпці
    numOFShadedBoxes = (numOfColumns * numOFRows) - len(message)

    #Кожна стрічка в списку plaintext представляє стовпець
    plaintext = [''] * numOfColumns

    #Змінні column і row вказують в яку ячейку повинен
    #бути поміщений символ зашифрованого повідомлення
    column = 0
    row= 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 #вказівник на наступний стовбець

        #Якщо більше немає стовпців АБО ми потрапили в "зашитриховані"
        #ячейки, перейти до першого стовпця наступної строки

        if (column == numOfColumns) or (column == numOfColumns - 1
            and row >= numOFRows -numOFShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)

#Якщо файл transpositionDecrypt.py виконується як програма
#(а не імпортується як модуль), визвати функцію main()
if __name__=='__main__':
    main()