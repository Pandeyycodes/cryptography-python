import numpy as np

def char_to_number(char):
    return ord(char.upper()) - ord('A')

def number_to_char(number):
    return chr(number + ord('A'))

def mod_inverse(a, m=26):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def create_key_matrix(key):
    if isinstance(key, np.ndarray):
        return key
    vals = [char_to_number(c) for c in key if c.isalpha()]
    n = int(len(vals) ** 0.5)
    if n * n != len(vals) or n < 2:
        return None
    return np.array(vals).reshape(n, n)

def get_matrix_inverse(matrix):
    det = int(round(np.linalg.det(matrix))) % 26
    det_inv = mod_inverse(det, 26)
    if det_inv is None:
        return None
    adj = np.round(np.linalg.inv(matrix) * np.linalg.det(matrix)).astype(int) % 26
    inv_matrix = (det_inv * adj) % 26
    return inv_matrix

def prepare_text(text, n):
    clean_text = "".join(c.upper() for c in text if c.isalpha())
    while len(clean_text) % n != 0:
        clean_text += 'X'
    return clean_text

def encrypt(text, key):
    matrix = create_key_matrix(key)
    if matrix is None:
        return ""

    det = int(round(np.linalg.det(matrix))) % 26
    if mod_inverse(det, 26) is None:
        print("Key matrix is not invertible mod 26")
        return ""

    n = len(matrix)
    prepared_text = prepare_text(text, n)
    encrypted_text = ""

    for i in range(0, len(prepared_text), n):
        block = np.array([char_to_number(c) for c in prepared_text[i:i + n]])
        cipher_block = (matrix @ block) % 26
        for num in cipher_block:
            encrypted_text += number_to_char(num)

    return encrypted_text

def decrypt(ciphertext, key):
    matrix = create_key_matrix(key)
    if matrix is None:
        return ""

    inv_matrix = get_matrix_inverse(matrix)
    if inv_matrix is None:
        print("Key matrix is not invertible mod 26")
        return ""

    n = len(inv_matrix)
    clean_text = "".join(c.upper() for c in ciphertext if c.isalpha())
    decrypted_text = ""

    for i in range(0, len(clean_text), n):
        if i + n > len(clean_text):
            break
        block = np.array([char_to_number(c) for c in clean_text[i:i + n]])
        plain_block = (inv_matrix @ block) % 26
        for num in plain_block:
            decrypted_text += number_to_char(num)

    return decrypted_text

if __name__ == "__main__":
    key = input("Enter the key: ")
    text = input("Enter the text to encrypt: ")

    matrix = create_key_matrix(key)
    if matrix is not None:
        print("\nKey Matrix:")
        print(matrix)
        print()

    encrypted_text = encrypt(text, key)
    print("Encrypted text: ", encrypted_text)
    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted text: ", decrypted_text)
