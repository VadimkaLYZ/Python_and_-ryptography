#шифр Цезаря

import pyperclip

#Ця стрічка підлягає шифруванню/дешифруванню
message = 'This is my secret message.'

#Ключ шифрування
key = 13

#Встановвлення режиму роботи: шифрування або дешифрування

mode = 'encrypt' # 'encrypt' or 'decrypt'

#Всі символи які можуть бути  зашифровані
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
#Змінна яка зберігає зашифровану/дешифровану форму повідомлення
translated = ''

for symbol in message:
    #Замітка: шиф/деш можна тільки символи, які включені в строку SYMBOLS
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Виконати шифрування/дешифрування
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key


        # Опрацювати "завертання", якщо необхідно
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        #приєднання символу без шифрування
        translated = translated + symbol

#Виввід переброзаваной строки
print(translated)
pyperclip.copy(translated)

