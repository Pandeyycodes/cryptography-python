import math


def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # choose e such that gcd(e, phi) = 1
    e = 2
    while e < phi:
        if math.gcd(e, phi) == 1:
            break
        e += 1

    # find d such that (d * e) % phi = 1
    d = pow(e, -1, phi)

    return (e, n), (d, n)


def encrypt(message, public_key):
    e, n = public_key
    encrypted = []

    for char in message:
        number = ord(char)
        encrypted.append(pow(number, e, n))

    return encrypted


def decrypt(encrypted, private_key):
    d, n = private_key
    message = ""

    for number in encrypted:
        message += chr(pow(number, d, n))

    return message


# RSA example

p = 61
q = 53

public_key, private_key = generate_keys(p, q)

print("Public key:", public_key)
print("Private key:", private_key)

message = input("Enter message: ")

encrypted = encrypt(message, public_key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, private_key)
print("Decrypted:", decrypted)