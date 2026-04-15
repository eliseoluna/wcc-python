import string


usr_input1 = input("Do you want to [E]ncrypt or [D]ecrypt: ").upper()
usr_input2 = input("Please enter your message: ").upper()

letters = string.ascii_uppercase


encrypt_dict = {}
decrypt_dict = {}

for i in range(len(letters)):
    encrypt_dict[letters[i]] = letters[(i + 2) % 26]
    decrypt_dict[letters[(i + 2) % 26]] = letters[i]

def encrypt(message):
    result = ""
    for ch in message:
        if ch in encrypt_dict:
            result += encrypt_dict[ch]
        else:
            result += ch
    return result

def decrypt(message):
    result = ""
    for ch in message:
        if ch in decrypt_dict:
            result += decrypt_dict[ch]
        else:
            result += ch
    return result

if usr_input1 == "E":
    print(encrypt(usr_input2))
elif usr_input1 == "D":
    print(decrypt(usr_input2))
