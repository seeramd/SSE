def caesar(encryptionKey, text, forward=True):
    #all my homies use list comprehension
    #key = list(map(int, encryptionKey))
    key = [int(x) for x in encryptionKey]

    #prepare list of character increment amounts from encryption key
    keyList = []
    j = 0;
    for i in range(len(text)):
        keyList.append(key[j])
        j+=1

        if j >= len(key):
            j = 0

    #when encrypting, increment the cypher forward
    #when de-encyrpting, increment backwards
    #return string of incremented characters
    if forward:
        cypher = []
        for n,c in enumerate(text):
            cypher.append(chr(ord(c) + keyList[n]))
        return "".join(cypher)
    else:
        clearText = []
        for n,c in enumerate(text):
            clearText.append(chr(ord(c) - keyList[n]))
        return "".join(clearText)

#user input
#Step 1: Choose encryption or de-encryption
print("""Are you encrypting or de-encrypting?

(1) Encrypting
(2) De-encrypting
""")

while True:
    selection = input("Enter your choice: ")

    if selection not in ['1','2']:
        print("Invalid selection")
        continue
    else:
        break

    
#step 2: Enter an encryption key
while True:
    key = input("Please enter an encryption key: ")

    if not key.isnumeric():
        print("Invalid key: numeric input only")
        continue
    else:
        break
#Step 3: get and read text file
while(True):
    
    fileName = input("Enter name of text file: ")
    try:
        with open(fileName + '.txt') as f:
            text = f.read()
        break
    except FileNotFoundError:
        print(f"\'{fileName}.txt\' not found in working directory")
        continue

#encrypt or de-encrypt based on selection
if selection == '1':
    newText = caesar(key, text, forward=True)
elif selection == '2':
    newText = caesar(key, text, forward=False)

#write new text to the text file
with open(fileName + '.txt','w',encoding="utf-8") as f:
    f.write(newText)

