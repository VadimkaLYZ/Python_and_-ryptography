#Тестування перестановачного шифру

import random, sys, transpositionEncrypt, transpositionDecrypt

def main():
    random.seed(42) #завдання "затравочного" значення

    for i in range(20): #виконуємо 20 тестів
        #Генурування вмпадкових повідомлень для тестування
        #Повідомлення буде мати довільну довжину
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        #Перетворення рядка в список для перемішування
        message = list(message)
        random.shuffle(message)
        message = ''.join(message) #зворотннє перетворення в рядок

        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        #Перервіряємо всі можливі ключі для кожного повідомлення
        for key in range(1, int(len(message)/2)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            #Якщо дешифрований текст не співпадає з оригінальним,
            #вивести повідомлення про помилку і закінчитись
            if message != decrypted:
                print("Mismatch with key %s and message %s." % (key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()

    print('Transposition cipher test passed.')

#Якщо файл transposition.py виконується як програма
#(а не імпортується як модуль), визвати функцію main()
if __name__=="__main__":
    main()