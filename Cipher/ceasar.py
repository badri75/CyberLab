def encrypt(p,k):
    cipher = ""
    for i in p:
        if (i.isupper()):
            cipher += chr((ord(i) + k - 65) % 26 + 65)
        else:
            cipher += chr((ord(i) + k - 97) % 26 + 97)
    return cipher

def decrypt(c,k):
    original = ""
    for i in c:
        if (i.isupper()):
            original += chr((ord(i) - k - 65) % 26 + 65)
        else:
            original += chr((ord(i) - k - 97) % 26 + 97)
    return original

plain = input("Enter Plain Text: ")
key = int(input("Enter Key value: "))
cipher = encrypt(plain,key)
original = decrypt(cipher,key)
print("Encrypted Text: " + cipher)
print("Decrypted Text: " + original)