message = input("Input your message: ")
message_encryption = []
#user enters message to be encrypted

for i in message:
    if ord(i) >= 97 and ord(i) <= 122:
        message_encryption.append(chr((ord(i) - 97 + 15) % 26 + 97))
    elif ord(i) >= 65 and ord(i) <= 90:
        message_encryption.append(chr((ord(i) - 65 + 15) % 26 + 65))
    else:
        message_encryption.append(i)
#loop through the chars in the message and perform caesar cypher
#retains case, formatting and non-letters
#by distinguishing between upper, lower, or non-letter chars

message = ''.join(message_encryption)
print(message)
#message var is reused to join encrypted message
#message is printed to console