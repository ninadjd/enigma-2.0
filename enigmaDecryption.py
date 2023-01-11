#!usr/bin/env python

import subprocess
import math
import random
import string
import statistics
import time
# import enigmaMain

def page_3_decrypt():
    subprocess.call("clear")
    print("MESSAGE DECRYPTION:")
    username = input("Enter your Username>>")
    tagNum = input("Enter your Tag Number>>")
    userPrivKey = input("Enter your Private Key>>")
    userPubKey = input("\nEnter your Public Key>>")

    def decToBin(char):
        value = 0
        if char == "a":
            value = 1
        elif char == "b":
            value = 2
        elif char == "c":
            value = 3
        elif char == "d":
            value = 4
        elif char == "e":
            value = 5
        elif char == "f":
            value = 6
        elif char == "g":
            value = 7
        elif char == "h":
            value = 8
        elif char == "i":
            value = 9
        elif char == "j":
            value = 10
        elif char == "k":
            value = 11
        elif char == "l":
            value = 12
        elif char == "m":
            value = 13
        elif char == "n":
            value = 14
        elif char == "o":
            value = 15
        elif char == "p":
            value = 16
        elif char == "q":
            value = 17
        elif char == "r":
            value = 18
        elif char == "s":
            value = 19
        elif char == "t":
            value = 20
        elif char == "u":
            value = 21
        elif char == "v":
            value = 22
        elif char == "w":
            value = 23
        elif char == "x":
            value = 24
        elif char == "y":
            value = 25
        elif char == "z":
            value = 26
        elif char == "A":
            value = 27
        elif char == "B":
            value = 28
        elif char == "C":
            value = 29
        elif char == "D":
            value = 30
        elif char == "E":
            value = 31
        elif char == "F":
            value = 32
        elif char == "G":
            value = 33
        elif char == "H":
            value = 34
        elif char == "I":
            value = 35
        elif char == "J":
            value = 36
        elif char == "K":
            value = 37
        elif char == "L":
            value = 38
        elif char == "M":
            value = 39
        elif char == "N":
            value = 40
        elif char == "O":
            value = 41
        elif char == "P":
            value = 42
        elif char == "Q":
            value = 43
        elif char == "R":
            value = 44
        elif char == "S":
            value = 45
        elif char == "T":
            value = 46
        elif char == "U":
            value = 47
        elif char == "V":
            value = 48
        elif char == "W":
            value = 49
        elif char == "X":
            value = 50
        elif char == "Y":
            value = 51
        elif char == "Z":
            value = 52
        elif char == "0":
            value = 53
        elif char == "1":
            value = 54
        elif char == "2":
            value = 55
        elif char == "3":
            value = 56
        elif char == "4":
            value = 57
        elif char == "5":
            value = 58
        elif char == "6":
            value = 59
        elif char == "7":
            value = 60
        elif char == "8":
            value = 61
        elif char == "9":
            value = 62
        elif char == " ":
            value = 63
        elif char == ".":
            value = 64
        elif char == ",":
            value = 65
        elif char == "?":
            value = 66
        elif char == "!":
            value = 67
        elif char == "/":
            value = 68
        elif char == "<":
            value = 69
        elif char == ">":
            value = 70
        elif char == ";":
            value = 71
        elif char == ":":
            value = 72
        elif char == "[":
            value = 73
        elif char == "]":
            value = 74
        elif char == "{":
            value = 75
        elif char == "}":
            value = 76
        elif char == "(":
            value = 77
        elif char == ")":
            value = 78
        elif char == "@":
            value = 79
        elif char == "#":
            value = 80
        elif char == "~":
            value = 81
        elif char == "^":
            value = 82
        elif char == "$":
            value = 83
        elif char == "%":
            value = 84
        elif char == "&":
            value = 85
        elif char == "*":
            value = 86
        elif char == "+":
            value = 87
        elif char == "-":
            value = 88
        elif char == "_":
            value = 89
        elif char == "|":
            value = 90
        elif char == "=":
            value = 91
        else:
            value = 0
        return value

    def binToChar(enc_num):
        char = ""
        if enc_num == 1:
            char = "a"
        elif enc_num == 2:
            char = "b"
        elif enc_num == 3:
            char = "c"
        elif enc_num == 4:
            char = "d"
        elif enc_num == 5:
            char = "e"
        elif enc_num == 6:
            char = "f"
        elif enc_num == 7:
            char = "g"
        elif enc_num == 8:
            char = "h"
        elif enc_num == 9:
            char = "i"
        elif enc_num == 10:
            char = "j"
        elif enc_num == 11:
            char = "k"
        elif enc_num == 12:
            char = "l"
        elif enc_num == 13:
            char = "m"
        elif enc_num == 14:
            char = "n"
        elif enc_num == 15:
            char = "o"
        elif enc_num == 16:
            char = "p"
        elif enc_num == 17:
            char = "q"
        elif enc_num == 18:
            char = "r"
        elif enc_num == 19:
            char = "s"
        elif enc_num == 20:
            char = "t"
        elif enc_num == 21:
            char = "u"
        elif enc_num == 22:
            char = "v"
        elif enc_num == 23:
            char = "w"
        elif enc_num == 24:
            char = "x"
        elif enc_num == 25:
            char = "y"
        elif enc_num == 26:
            char = "z"
        elif enc_num == 27:
            char = "A"
        elif enc_num == 28:
            char = "B"
        elif enc_num == 29:
            char = "C"
        elif enc_num == 30:
            char = "D"
        elif enc_num == 31:
            char = "E"
        elif enc_num == 32:
            char = "F"
        elif enc_num == 33:
            char = "G"
        elif enc_num == 34:
            char = "H"
        elif enc_num == 35:
            char = "I"
        elif enc_num == 36:
            char = "J"
        elif enc_num == 37:
            char = "K"
        elif enc_num == 38:
            char = "L"
        elif enc_num == 39:
            char = "M"
        elif enc_num == 40:
            char = "N"
        elif enc_num == 41:
            char = "O"
        elif enc_num == 42:
            char = "P"
        elif enc_num == 43:
            char = "Q"
        elif enc_num == 44:
            char = "R"
        elif enc_num == 45:
            char = "S"
        elif enc_num == 46:
            char = "T"
        elif enc_num == 47:
            char = "U"
        elif enc_num == 48:
            char = "V"
        elif enc_num == 49:
            char = "W"
        elif enc_num == 50:
            char = "X"
        elif enc_num == 51:
            char = "Y"
        elif enc_num == 52:
            char = "Z"
        elif enc_num == 53:
            char = "0"
        elif enc_num == 54:
            char = "1"
        elif enc_num == 55:
            char = "2"
        elif enc_num == 56:
            char = "3"
        elif enc_num == 57:
            char = "4"
        elif enc_num == 58:
            char = "5"
        elif enc_num == 59:
            char = "6"
        elif enc_num == 60:
            char = "7"
        elif enc_num == 61:
            char = "8"
        elif enc_num == 62:
            char = "9"
        elif enc_num == 63:
            char = " "
        elif enc_num == 64:
            char = "."
        elif enc_num == 65:
            char = ","
        elif enc_num == 66:
            char = "?"
        elif enc_num == 67:
            char = "!"
        elif enc_num == 68:
            char = "/"
        elif enc_num == 69:
            char = "<"
        elif enc_num == 70:
            char = ">"
        elif enc_num == 71:
            char = ";"
        elif enc_num == 72:
            char = ":"
        elif enc_num == 73:
            char = "["
        elif enc_num == 74:
            char = "]"
        elif enc_num == 75:
            char = "{"
        elif enc_num == 76:
            char = "}"
        elif enc_num == 77:
            char = "("
        elif enc_num == 78:
            char = ")"
        elif enc_num == 79:
            char = "@"
        elif enc_num == 80:
            char = "#"
        elif enc_num == 81:
            char = "~"
        elif enc_num == 82:
            char = "^"
        elif enc_num == 83:
            char = "$"
        elif enc_num == 84:
            char = "%"
        elif enc_num == 85:
            char = "&"
        elif enc_num == 86:
            char = "*"
        elif enc_num == 87:
            char = "+"
        elif enc_num == 88:
            char = "-"
        elif enc_num == 89:
            char = "_"
        elif enc_num == 90:
            char = "|"
        elif enc_num == 91:
            char = "="
        else:
            char = ""
        return char

    def publicKeyConverter(priv):
        public_key_1_gen = ""
        public_key_2_gen = ""
        j = "1"
        for char in priv:
            if j == "1":
                public_key_1_gen = public_key_1_gen + char
                j = "2"
                # j = j+1
            else:
                public_key_2_gen = public_key_2_gen + char
                j = "1"
                # j = j+1
        public_key_gen = public_key_1_gen + public_key_2_gen
        return public_key_gen

    def stringToList(string):
        list = []
        list[0:] = string
        return list

    def listToString(list):
        string = ''
        for char in list:
            string = string + char
        return string

    def spaceExtractor(publicKey):
        publicKeyList = stringToList(publicKey)
        spacer = publicKeyList[500]
        publicKeyList.pop(500)
        finalPublicKey = listToString(publicKeyList)
        return finalPublicKey, spacer

    def supported_chars(char):
        upper_case_chars = ["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z"]
        lower_case_chars = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"]
        numerics = ["0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]
        symbols = [" " , "." , "," , "?" , "!" , "/" , "<" , ">" , ";" , ":" , "[" , "]" , "{" , "}" , "(" , ")" , "@" , "#" , "~" , "^" , "$" , "%" , "&" , "*" , "+" , "-" , "_" , "|" , "="]
        if char in upper_case_chars:
            return char
        elif char in lower_case_chars:
            return char
        elif char in numerics:
            return char
        elif char in symbols:
            return char
        else:
            print("The charachter - " + char + " is not supported!")
            exit()

    def rec_pub_key():
        rec_key = input("\nEnter the Sender's Public Key>>")
        return rec_key

    def message():
        msg_list = []
        msg = input("\nEnter the Message to be encrypted>>")
        for char in msg:
            msg_list.append(supported_chars(char))
        checkedMsg = listToString(msg_list)
        return checkedMsg

    def meanFinder(m1, m2):
        return math.floor((m1 + m2)/2)

    def decrypt1(string):
        finalStr = ''
        arr1 = slice(0, round(len(string) / 2))
        arr2 = slice(round(len(string) / 2), round(len(string)))
        str1 = string[arr1]
        str2 = string[arr2]
        try:
            for j in range(len(string)):
                if str1[j]:
                    finalStr = finalStr + str1[j]
                if str2[j]:
                    finalStr = finalStr + str2[j]
        except IndexError:
            pass
        return finalStr

    def keySpacer(key, spacer):
        temp = spacer
        charList = []
        for i in range(182):
            charList.append(key[temp])
            temp = temp + spacer
        return charList

    def charToFourBit(list):
        i = 1
        listStr = ''
        finalList = []
        for j in range(len(list)):
            if i == 1:
                listStr = listStr + list[j]
                i = 2
            elif i == 2:
                listStr = listStr + list[j]
                i = 3
            elif i == 3:
                listStr = listStr + list[j]
                i = 4
            elif i == 4:
                listStr = listStr + list[j]
                finalList.append(listStr)
                listStr = ''
                i = 1
        return finalList

    def decrypt2(user1Key, user2Key, msg, mean):
        list1 = keySpacer(user1Key, mean)
        list2 = keySpacer(user2Key, mean)
        initlist = []
        for j in range(182):
            initlist.append(list1[j])
            initlist.append(list2[j])

        fourBitList = charToFourBit(initlist)
        charStr = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,?!/<>;:[]{}()@#~^$%&*+-_|='
        charList = stringToList(charStr)
        decMsg = ''
        msgList = charToFourBit(msg)
        for char in msgList:
            decMsg = decMsg + charList[fourBitList.index(char)]
        return decMsg

    def binarySubtraction(realBin, keyBin):
        realValue = 0
        if realBin >= keyBin:
            realValue = realBin - keyBin
        else:
            realBin = realBin + 91
            realValue = realBin - keyBin
        return realValue

    def decrypt3(user1Key, user2Key, msg):
        user1KeyList = stringToList(user1Key)
        user2KeyList = stringToList(user2Key)
        keyList = []
        count = len(msg)
        for j in range(count):
            keyList.append(user1KeyList[j])
            keyList.append(user2KeyList[j])
        decryptedStr = ''
        for j in range(count):
            realBin = decToBin(msg[j])
            keyBin = decToBin(keyList[j])
            decryptedBinary = binarySubtraction(realBin, keyBin)
            decryptedChar = binToChar(decryptedBinary)
            decryptedStr = decryptedStr + decryptedChar

        return decryptedStr

    def decryption(user1Key, user2Key, spacer1, spacer2):
        msg = message()
        decOne = decrypt1(msg)
        mean = meanFinder(int(spacer1), int(spacer2))
        decTwo = decrypt2(user1Key, user2Key, decOne, mean)
        decThree = decrypt3(user1Key, user2Key, decTwo)
        print("\nDecrypted Message >> " + decThree)
        print("\nYou can now exit this program or get back to the Main Page!")
        exit()
        # resp = input("\n\nDo you want to go back to the Main Page for Encryption and Decryption?[Y/N]>> ")
        # if resp == "y" or resp == "Y":
        #     print("[+]Proceeding....!")
        #     enigmaMain.main_func()
        # elif resp == "n" or resp == "N":
        #     # print("[+]Not proceeding!!")
        #     exit()
        # else:
        #     print("[-]Error!")
        #     exit()

    def decryptMain():
        if username in userPrivKey and tagNum in userPrivKey:
            realPublicKey = publicKeyConverter(userPrivKey)
            extractedInfo = spaceExtractor(userPubKey)
            if realPublicKey == extractedInfo[0]:
                senKey = rec_pub_key()
                senInfo = spaceExtractor(senKey)
                decryption(senInfo[0], extractedInfo[0], senInfo[1], extractedInfo[1])
            else:
                print("Enter Valid Detalis")
                exit()
        else:
            print("Enter Valid Details!")
            exit()
    decryptMain()