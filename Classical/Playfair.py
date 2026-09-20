def create_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix = []
    
    # Add unique letters from key
    for char in key:
        if char.isalpha() and char not in matrix:
            matrix.append(char)
            
    # Add remaining letters of alphabet (omitting J)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
            
    # Form 5x5 grid
    grid = []
    for i in range(0, 25, 5):
        grid.append(matrix[i:i+5])
    return grid

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def prepare_text(text):
    text = text.upper().replace('J', 'I')
    clean_text = ""
    for char in text:
        if char.isalpha():
            clean_text += char
            
    # Break into pairs and handle duplicate adjacent letters
    prepared = ""
    i = 0
    while i < len(clean_text):
        char1 = clean_text[i]
        if i + 1 < len(clean_text):
            char2 = clean_text[i + 1]
            if char1 == char2:
                filler = 'X' if char1 != 'X' else 'Z'
                prepared += char1 + filler
                i += 1
            else:
                prepared += char1 + char2
                i += 2
        else:
            filler = 'X' if char1 != 'X' else 'Z'
            prepared += char1 + filler
            i += 1
            
    return prepared

def encrypt(text, key):
    matrix = create_matrix(key)
    prepared_text = prepare_text(text)
    encrypted_text = ""
    
    for i in range(0, len(prepared_text), 2):
        row1, col1 = find_position(matrix, prepared_text[i])
        row2, col2 = find_position(matrix, prepared_text[i + 1])
        
        # Rule 1: Same row
        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 5]
            encrypted_text += matrix[row2][(col2 + 1) % 5]
        # Rule 2: Same column
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1]
            encrypted_text += matrix[(row2 + 1) % 5][col2]
        # Rule 3: Rectangle
        else:
            encrypted_text += matrix[row1][col2]
            encrypted_text += matrix[row2][col1]
            
    return encrypted_text

def decrypt(ciphertext, key):
    matrix = create_matrix(key)
    decrypted_text = ""
    
    clean_text = ""
    for char in ciphertext.upper().replace('J', 'I'):
        if char.isalpha():
            clean_text += char
            
    for i in range(0, len(clean_text), 2):
        if i + 1 >= len(clean_text):
            break
        row1, col1 = find_position(matrix, clean_text[i])
        row2, col2 = find_position(matrix, clean_text[i + 1])
        
        # Rule 1: Same row
        if row1 == row2:
            decrypted_text += matrix[row1][(col1 - 1) % 5]
            decrypted_text += matrix[row2][(col2 - 1) % 5]
        # Rule 2: Same column
        elif col1 == col2:
            decrypted_text += matrix[(row1 - 1) % 5][col1]
            decrypted_text += matrix[(row2 - 1) % 5][col2]
        # Rule 3: Rectangle
        else:
            decrypted_text += matrix[row1][col2]
            decrypted_text += matrix[row2][col1]
            
    return decrypted_text

if __name__== "__main__":
    key = input("Enter the key: ")
    text = input("Enter the text to encrypt: ")
    
    print("\nMatrix:")
    for row in create_matrix(key):
        print(" ".join(row))
    print()
    
    encrypted_text = encrypt(text, key)
    print("Encrypted text: ", encrypted_text)
    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted text: ", decrypted_text)
