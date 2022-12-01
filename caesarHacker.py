#Програма для взолму шифру Цезаря

message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#Цикл по всім можливим значенням ключа

for key in range(len(SYMBOLS)):
    translated = ''

    #Цикл по всім повідомленням
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Опрацювання "завертання"
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            #Приєднання дешифрованого символу
            translated = translated + SYMBOLS[translatedIndex]

        else:
            #Приєднати символ без шифрування/дешифрування
            translated = translated + symbol

    #Відобразати кожнний варіант розшифрування
    print('Key #%s: %s' % (key, translated))




