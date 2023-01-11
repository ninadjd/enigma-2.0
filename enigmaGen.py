#!usr/bin/env python

import subprocess
import random
import string
import statistics
# import enigmaMain

def page_1_generate():
    subprocess.call("clear")
    username = input("Enter a Username >> ")

    def tag():
        num = []
        tag_string = ''
        for i in range(8):
            num.append(random.randint(0, 9))
            tag_string = tag_string + str(num[i])
        mean = round(statistics.mean(num))
        return tag_string, str(mean)

    def key_append():
        pri_1 = key_gen()
        pri_2 = key_gen()
        pri_3 = key_gen()
        tag_num, mean = tag()
        pri = pri_1 + username + pri_2 + tag_num + pri_3
        pub = public_key_converter(pri, mean)
        return pri, pub, tag_num

    def key_gen():
        private_key_gen = ""
        # public_key_1_gen = ""
        # public_key_2_gen = ""
        # j = "1"
        for i in range(500):
            # for j in range(4):
            charachter = random.choice(string.ascii_letters + string.digits)
            private_key_gen = private_key_gen + charachter

        # public_key_gen = public_key_1_gen + public_key_2_gen
        return private_key_gen

    def public_key_converter(priv, spacer):
        publicKey1 = []
        publicKey2 = []
        j = "1"
        for char in priv:
            if j == "1":
                publicKey1.append(char)
                j = "2"
            else:
                publicKey2.append(char)
                j = "1"
        publicKey = publicKey1 + publicKey2
        # realPublicKey = list(publicKey)
        publicKey.insert(500, spacer)
        # print(type(publicKey))
        # publicKeyString = ''
        publicKeyString = ''.join(publicKey)
        return publicKeyString

    private_key, public_key, tag_number = key_append()
    print("-----------------------------------------------------------------------------")
    print("Your Username is >> " + username)
    print("Your Tag Number is >> " + tag_number)
    print("Your Private Key is >>\n\n" + private_key)
    print("\nYour Public Key is >>\n\n" + public_key)
    print("\nSave all these details somewhere! All these details will be required during the time of Encryption and Decryption!")
    print("\nYou can now go back to the Main Page for Encryption and Decryption!")
    print("\nDon't Worry! You can exit the program now and come back later. Just save these details!")
    exit()
