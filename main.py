# one time pad functions

def encrypt(message,key):
    wordList=message.split()
    keyWordList=key.split()
    
    messList=[]
    for i in wordList:
        for j in range(len(i)):
            messList.append(int(ord(i[j])-97))
    
    keyList=[]
    for i in keyWordList:
        for j in range(len(i)):
            keyList.append(int(ord(i[j])-97))  
    
    encryptMess=[]
    for i in range(len(messList)):
        crypt=(messList[i]+keyList[i])%26
        encryptMess.append(chr(crypt+97))

    return ''.join(encryptMess)
    
def decrypt(encmess,key):
    encMessageWordList=encmess.split()
    keyWordList=key.split()
    
    encList=[]
    for i in encMessageWordList:
        for j in range(len(i)):
            encList.append(int(ord(i[j])-97))
    
    keyList=[]
    for i in keyWordList:
        for j in range(len(i)):
            keyList.append(int(ord(i[j])-97))  
    
    message=[]
    for i in range(len(encList)):
        if(encList[i]-keyList[i]<0):
            mess=(encList[i]-keyList[i])+26
        else:
            mess=(encList[i]-keyList[i])
        message.append(chr(mess+97))

    return ''.join(message)
    
message=input("Please input the message you wish to encrypt: ")
key=input("Please input the key. The key size must be atleast the size of the message: ")

encryptedMess=encrypt(message,key)
print(encryptedMess)

decryptedMess=decrypt(encryptedMess,key)
print(decryptedMess)
