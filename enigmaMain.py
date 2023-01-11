#!usr/bin/env python

import subprocess
import enigmaGen, enigmaEncryption, enigmaDecryption

def main_func():
    subprocess.call("clear")
    print("Welcome to ENIGMA - An Extra Layer Of Security")
    print("\n")
    print("Choose from the following:-")
    print("1.Generate Keys")
    print("2.Encrypt Message")
    print("3.Decrypt Message")
    print("4.Exit")
    print("\nRespond by pressing appropriate numbers!")
    user_response = input("\nYour Response >> ")
    user_response = str(user_response)
    print(type(user_response))
    if user_response == "1":
        print(user_response)
        enigmaGen.page_1_generate()
    elif user_response == "2":
        enigmaEncryption.page_2_encrypt()
    elif user_response == "3":
        enigmaDecryption.page_3_decrypt()
    elif user_response == "4":
        print("\n[+]Exiting...\n")
        exit()
    else:
        print("\nEnter a valid choice.\n")
        exit()

try:
    main_func()
except KeyboardInterrupt:
    print("\n")
    pass