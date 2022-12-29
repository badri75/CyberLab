def encrypt(p,k):
    enc=[[" " for i in range(len(p))] for j in range(k)]
    flag,row = 0,0
    cipher = ""
    for i in range(len(p)):
        enc[row][i]=p[i]
        if row==0:
            flag=0
        elif row==k-1:
            flag=1
        if flag==0:
            row+=1
        else:
            row-=1
    for i in range(k):
        for j in range(len(p)):
            if enc[i][j]!=' ':
                cipher += enc[i][j]
    return cipher

plain = input("Enter Plain Text: ")
key = int(input("Enter Key value: "))
cipher = encrypt(plain,key)
print("Encrypted Text: " + cipher)