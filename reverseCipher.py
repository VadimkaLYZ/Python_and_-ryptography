#Програма зворотнього шифрування

message = 'There can keep a secret, if two of them are dead.'

transleted = ''

i = len(message) - 1
while i >= 0:
    transleted = transleted + message[i]
    i = i - 1
    
print(transleted)

