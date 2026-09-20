def char_to_number(char):
    return ord(char.upper())-ord('A')

def number_to_char(number):
    return chr(number+ord('A'))

def encrypt(text,shift):
    encrypted_text=""
    for char in text:
        if char.isalpha():
            encrypted_text+=number_to_char((char_to_number(char)+shift)%26)
        else:
            encrypted_text+=char
    return encrypted_text

def decrypt(text,shift):
    return encrypt(text,-shift)

if __name__== "__main__": 
    text=input("Enter the text to encrypt: ")
    shift=int(input("Enter the shift value: "))
    encrypted_text=encrypt(text,shift)
    print("Encrypted text: ",encrypted_text)
    decrypted_text=decrypt(encrypted_text,shift)
    print("Decrypted text: ",decrypted_text)