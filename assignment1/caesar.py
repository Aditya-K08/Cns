import random
import string
import base64
alpha = "abcdefghijklmnopqrstuvwxyz"

def encrypt():
    pt = input("input the string")
    key =int( input("input the key"))

    result = ""

    for i in pt:
        result += chr((ord(i)+key-31)% 128 + 31)

    print(f'Cipher text : {result}')    


def monoEncrpyt():
    pt = input("input the string")
    l=list(alpha)
    random.shuffle(l)
    key = "".join(l)
    result = []
    for i in pt:
        if i.lower() in alpha:
            y = key[alpha.index(i.lower())]
            if(i.isupper()):
                y= y.upper()
            result.append(y)
        else:
            result.append(y)        
    return "".join(result)   


def polyEncrypt():
    pt = input("input the string")
    key = input("Enter the key of same length : ")
    pt_len = len(key)
    ptAscii = [ord(x) for x in pt]
    keyAscii = [ord(x) for x in key]

    result = ''

    for i in range (pt_len) :
        if pt[i].islower():
            val = chr((ptAscii[i]+keyAscii[i%pt_len] - 2*ord('a'))%26 + ord('a'))
            result+=val
        elif pt[i].isupper():
            val = chr((ptAscii[i]+keyAscii[i%pt_len] - 2*ord('A'))%26 + ord('A'))
            result+=val
        else:
            result+=pt[i]

    return result                
 


def railEncrypt():
    pt = input("Enteer the plain text : ")
    key  = int(input("Enter the no of rails : "))

    rail = [['\n' for i in range (len(pt))] for j in range (key)]

    border = False
    row=col=0
    for x in pt:
        if (row == 0) or (col == key-1):
            border = not border 

        rail[row][col]=x
        col=col+1

        if border:
            row=row+1
        else :
            row=row-1         

    result = []
    for i in range(key):
        for j in range (len(pt)):
            if(rail[i][j]!='\n'):
                result.append(rail[i][j])

    return "".join(result)            


def gen_key(x: int):
    key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(x))
    return key

def verman(key : int):
    
    tzt =  "".join(chr(ord(p)^ord(k)) for p,k in zip(pt,key))
    return base64.b64encode(tzt.encode()).decode()

if __name__ == '__main__':
    ch = int(input('------Caesar Cipher-----\n1. Encrypt\n2. Decrypt\n3. Exit\n4.poly\n-----------------\nYour Choice: '))
    if ch == 1:
         encrypt()
    if ch == 2:
        ans = monoEncrpyt()
        print(ans)
    elif ch == 3:
        ans = polyEncrypt()
        print(ans)
    elif ch == 4:

        ans = railEncrypt()
        print(ans)    
    elif ch == 5:
        pt = input("Enteer the plain text : ")
        key = gen_key(len(pt))
        ans = verman(key)
        print(ans)        
    else:
        print("Invalid Input!!") 