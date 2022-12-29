def generatekey(p,k):
    if len(p) != len(k):
        for i in k:
            k += i
            if len(p) == len(k):
                break
    return k

def encrypt(p, k):
    c = ""
    start = ord('A')
    for i, j in zip(p, k):
        pos = start + (ord(i) + ord(j)) % 26
        c += chr(pos)
    return c

def decrypt(c, k):
    o = ""
    start = ord('A')
    for i, j in zip(c, k):
        pos = start + (ord(i) - ord(j) + 26) % 26
        o += chr(pos)
    return o

plain = input("Enter Plain Text: ").upper()
keyword = input("Enter keyword: ").upper()
key = generatekey(plain,keyword)
cipher = encrypt(plain,key)
original = decrypt(cipher,key)
print("Encrypted Text: " + cipher)
print("Decrypted Text: " + original)