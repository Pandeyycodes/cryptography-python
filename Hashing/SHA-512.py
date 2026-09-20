import hashlib

def sha512_hash(text):
    return hashlib.sha512(text.encode()).hexdigest()

def verify_hash(text, expected_hash):
    return sha512_hash(text).lower() == expected_hash.strip().lower()

if __name__ == "__main__":
    text = input("Enter the text to hash: ")
    hashed_text = sha512_hash(text)
    print("SHA-512 Hash: ", hashed_text)
    print("Length (characters): ", len(hashed_text))
    print("Length (bits): ", len(hashed_text) * 4)
