import base64
import os
from colorama import init
from termcolor import colored

def encode_bs64():
    command = "base64 " + filename  # idée : créer un fichier qui contient le contenu de l'input, avec un nom déterminé, caché, réécris à chaque request
    output = os.system(command)
    print(" <==== BASE64 ====>")
    print(output)

def encrypt_choice():
    print(colored("[+]   Please make your choice    >", "green"))
    print("")
    print("     <|  1 > base64")
    print("     <|  2 > md5")
    print("     <|  3 > sha1")
    print("     <|  4 > sha256")
    print("     <|  5 > sha512")
    print("     <|  6 > base32")
    print("     <|  7 > base58")
    print("     <|  8 > xor")
    print("     <|  9 > hex")
    print("     <|  10 > binary")
    print("     <|  exit/quit > leave the programm")
    print("")

    e_choice = str(input("  >> "))
    e_l = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "exit", "quit"]

    if e_choice not in e_l:
        print("Please enter a proper integer between 1 and 10")
        encrypt_choice()

    if e_choice == "1":
        encode_bs64()
    if e_choice == "2":
        print("md5 coming")
    if e_choice == "3":
        print("sha1 coming")
    if e_choice == "4":
        print("sha256 comming")
    if e_choice == "5":
        print("sha512 coming")
    if e_choice == "6":
        print("base32 coming")
    if e_choice == "7":
        print("base58 coming")
    if e_choice == "8":
        print("xor coming")
    if e_choice == "9":
        print ("hex coming")
    if e_choice == "10":
        print("binary coming")
    if e_choice == "exit" or e_choice == "quit":
        sys.exit()