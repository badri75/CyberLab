print('****************************Caesar Cipher********************************')
while(True):
    key = int(input('Enter the key to Encrypt: '))
    if str(key).isnumeric():
        result = ''
        s = input('Enter the String: ')
        for i in range(len(s)):
            c = s[i]
            if c.isupper():
                result += chr(((ord(s[i])+key-64) %26) +65)
            else:
                result += chr(((ord(s[i])+key-96) %26) +97)
        print(result)
    break
