def char_to_number(char):
    return ord(char.upper())-ord('A')

def number_to_char(number):
    return chr(number+ord('A'))

def encrypt(text,key):
    encrypted_text=""
    key_index=0
    for char in text:
        if char.isalpha():
            encrypted_text+=number_to_char((char_to_number(char)+char_to_number(key[key_index%len(key)]))%26)
            key_index+=1
        else:
            encrypted_text+=char
    return encrypted_text

def decrypt(text,key):
    encrypted_text=""
    key_index=0
    for char in text:
        if char.isalpha():
            encrypted_text+=number_to_char((char_to_number(char)-char_to_number(key[key_index%len(key)]))%26)
            key_index+=1
        else:
            encrypted_text+=char
    return encrypted_text

if __name__== "__main__":
    text=input("Enter the text to encrypt: ")
    key=input("Enter the key: ")
    encrypted_text=encrypt(text,key)
    print("Encrypted text: ",encrypted_text)
    decrypted_text=decrypt(encrypted_text,key)
    print("Decrypted text: ",decrypted_text)