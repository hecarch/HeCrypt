# Main script to run
# Made by hecatonchire#4292
#!/usr/bin/env python

# checker si il exite .hecrypt.config à chaque fois, stocker dedans la langue
# -f pour outrepasser le get_use()
# inventer une fonction ?
# faire un requierements.txt

from colorama import init
from termcolor import colored
from encrypt import encrypt_choice

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

