"""
Run Spot Run => encrypt => Bex Czyd bex
Bex Czyd bex => decrypt => Run Spot run

You only need to implement the decrypt() and decryptFile() methods.
Use the encrypt() and encryptFile() methods as a reference / example.

When you encrypt, you add the sharedSecret to each character
When you decrypt, you subtract the sharedSecret from each character

By default: encryptFile will read in example.txt and create example.out with
   the encrypted text.
            decryptFile will read in example.out and create example.in with 
   the decrypted text.  example.in should match with example.txt.
"""

cmdEncryptFile = 1
cmdDecryptFile = 2
cmdSpecifyFileName = 3
cmdExit = 4

fileName = "example"
sharedSecret = 10


def processMenu():
    print(cmdEncryptFile, "... Encrypt File")
    print(cmdDecryptFile, "... Decrypt File")
    print(cmdSpecifyFileName, "... Specify File Name")
    print(cmdExit, "...Exit")
    while True:
        try:
            choice = int(input("choice:"))
            if choice < 1 or choice > cmdExit:
                raise Exception("choice not within range")
            return choice
        except ValueError:
            print("Need to enter an integer")
        except Exception as error:
            print("Exception:", error)

"""
    to do:
    use encrypt() as an example
        - subtract the secret
        - walk through the wrap around for the letters
"""


def decrypt(secret, word):

    return "todo"


"""
    to do:
       - use encryptFile as an example
"""


def decryptFile(secret):
    fileHandle = open(fileName + ".out")
    outFileHdl = open(fileName + ".in", "w")
    lst = list(fileHandle)

    for sentence in lst:
        print(sentence)
        # call decrypt() for each word in the sentence
        # write each word to outFileHdl

    outFileHdl.close()


def encrypt(secret, word):
    newWord = ""

    for nChar in word:
        if nChar >= "A" and nChar <= "Z":
            nChar = chr(ord(nChar) + secret)
            if ord(nChar) > ord("Z"):
                nChar = chr(ord("A") + ord(nChar) - ord("Z") - 1)

        if nChar >= "a" and nChar <= "z":
            nChar = chr(ord(nChar) + secret)
            if ord(nChar) > ord("z"):
                nChar = chr(ord("a") + ord(nChar) - ord("z") - 1)

        newWord += nChar
    return newWord


def encryptFile(secret):
    wordDict = {}
    fileHandle = open(fileName + ".txt")
    outFileHdl = open(fileName + ".out", "w")
    lst = list(fileHandle)

    for line in lst:
        print(line)
        line = line.strip()
        lineList = line.split()

        for i in range(len(lineList)):
            nWord = encrypt(secret, lineList[i])
            if i < len(lineList) - 1:
                nWord = nWord + " "
            else:
                nWord = nWord + "\n"
            outFileHdl.write(nWord)
    outFileHdl.close()


while True:
    choice = processMenu()
    print("choice: ", choice)

    if choice == cmdEncryptFile:
        encryptFile(sharedSecret)
    elif choice == cmdDecryptFile:
        decryptFile(sharedSecret)
    elif choice == cmdSpecifyFileName:
        fileName = input("Enter file name: (.txt will automatically be added) ")
        print("fileName has been set to:", fileName)
    elif choice == cmdExit:
        break
    print("Success")

encryptFile()
