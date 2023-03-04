mode = '' 
key = 0


while True:
    try:
        mode = str(input('Do you want to (e)ncrypt or (d)ecrypt? '))
        print(mode)
        if mode == 'e' or mode == 'd':
            break
        else:
            raise Exception
    except Exception:
        print("Enter 'e' or 'd'")



while True:
    try:
        if mode == 'e':
            key = int(input('Please enter the key (0 to 25) to use.'))
            if key >= 0 and key <= 25:
                break
            else:
                raise Exception
        elif mode == 'd':
            key = int(input('Please enter the key (0 to 26) to use.'))
            if key >=  0 and key <= 26:
                break
            else:
                raise Exception
        print(key)
    except Exception:
        print("Key out of range")
    


print(key)

def encrypt():
    msg = str(input("Enter the message to encrypt."))
    msg = msg.lower()
    msg_encr = ''
    for letter in msg:
        if letter.isalpha():
                msg_encr += chr((ord(letter) + (key - 97)) % 26 + 97)
        else:
            msg_encr += letter
    msg = msg.upper()
    print(msg_encr)

def decrypt():
    msg = str(input("Enter the message to decrypt."))
    msg = msg.lower()
    msg_decr = ''
    letters = "abcdefghijklmnopqrstuvwxyz"
    for char in msg:
        if char in letters:
            position = letters.find(char)
            new_position = (position - key) % 26
            new_char = letters[new_position]
            msg_decr += new_char
        else:
            msg_decr += char
    msg_decr = msg_decr.upper()
    print(msg_decr)


if mode == 'e':
    encrypt()
elif mode == 'd':
    decrypt()