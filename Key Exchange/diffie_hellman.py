# vulnerable for man in the middle 
# often uses signatures like rsa or certificates to prevent it 
# pow(base,exp,mod) is used for modular exponentiation 

def diffie_hellman(p, g):
    a = int(input("Enter the private key of Alice: "))
    b = int(input("Enter the private key of Bob: "))

    A = pow(g, a, p)
    B = pow(g, b, p)

    print("Alice's public key: ", A)
    print("Bob's public key: ", B)

    shared_key_alice = pow(B, a, p)
    shared_key_bob = pow(A, b, p)

    print("Shared key for Alice: ", shared_key_alice)
    print("Shared key for Bob: ", shared_key_bob)

    if shared_key_alice == shared_key_bob:
        print("Success! Keys matched: ", shared_key_alice)

if __name__ == "__main__":
    p = int(input("Enter prime number (p): "))
    g = int(input("Enter base/generator (g): "))
    diffie_hellman(p, g)
