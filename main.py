# Main script to run
# Made by hecatonchire#4292
#!/usr/bin/python

# checker si il exite .hecrypt.config à chaque fois, stocker dedans la langue
# -f pour outrepasser le get_use()
# inventer une fonction ?
# faire un requierements.txt
# prend forcément un fichier en input 

from colorama import init
from termcolor import colored
from encrypt_heca import *
import sys
import getopt
import os

init()

print("")
print("*@@@@*  *@@@@**           mm@***@m@                                 @@   ")
print("  @@      @@            m@@*     *@                                 @@   ")
print("  @@      @@     mm@*@@ @@*       * @@@m@@@ *@@*   *@@**@@@@@@@@m @@@@@@ ")
print("  @@@@@@@@@@    m@*   @@@@           @@* **   @@   m@    @@   *@@   @@   ")
print("  !@      @!    !@*   **@!m          @!        @@ m!     !@    @@   @@   ")
print("  !@      @!    !@m*** m*!@          @!         @@!      !@    !@   @!   ")
print("  :!      !!    !!      !!!          !!         @!!      !@!   !!   !!   ")
print("  :!      :!    :!!     :!!:     !*  !:         !!:      !@   !!!   !!   ")
print("::: :   : :!::   : : ::   : : : :! : :::        !!       :!: : :    ::: :")
print("                                              ::!        ::              ")
print("                                            :::        : : ::                                @hecarch_")
print("")

def verify_os():
    if os.name == "nt":
        print("This tool can't be run on a windows machine, please install a real OS.")

def verify_file(argv):
    filename = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:],"h:i:")
    except getopt.GetoptError:
        print("usage : main.py -i <filename>")
        sys.exit(2)
    for (opt, arg) in opts:
        if opt == "-h":
            print("usage : main.py -i <filename>")
        elif opt == ("-i"):
            filename = arg
            print("Input file is", filename)
            return filename
        elif opt != "-i":
                print("Input file must be provided !")  # TODO si l'user ne rentre pas de filename, le dire et exit
                sys.exit()

verify_os()
filename = verify_file(sys.argv[1:])
encrypt_heca.recup_file(filename)

def choice_encrypt():
    print("Encrypt here")

def choice_decrypt():
    print("Decrypt here")

def choice_recognize_hash():
    print("Recognize here")

def choice_try_functions():
    print("Try functions here")

def get_use():
    print(colored("[+]   Please make your choice    >", "green"))
    print("")
    print("     <|  1 > encrypt")
    print("     <|  2 > decrypt")
    print("     <|  3 > recognize hash")
    print("     <|  4 > try many simple function")
    print("     <|  exit/quit > leave the programm")
    print("")

    main_choice = str(input("  >> "))
    l = ["1", "2", "3", "4", "exit", "quit"]
    
    if main_choice not in l:
        print("Please type a proper integer between 1 and 4.")
        get_use()
    
    if main_choice == "1":
        encrypt_choice()
    elif main_choice == "2":
        choice_decrypt()
    elif main_choice == "3":
        choice_recognize_hash()
    elif main_choice == "4":
        choice_try_functions()
    elif main_choice == "exit" or main_choice == "quit":
        exit()

get_use()

