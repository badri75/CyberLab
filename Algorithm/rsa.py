import math
p,q,e,k = 3,7,2,2
n = p*q
phi = (p-1)*(q-1)
while(e<phi):
    if(math.gcd(e,phi) == 1):
        break
    else:
        e += 1
d = (1+(k*phi))/e
msg = int(input("Enter a Number: "))
c = pow(msg,e)%n
print("Encrypted Data: ",c)
m = int(pow(c,d)%n)
print("Decrypted data: ",m)