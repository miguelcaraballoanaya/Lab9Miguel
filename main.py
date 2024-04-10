from encode import *


def display_menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Exit\n")


if __name__ == "__main__":
    decoded = []
    while True:
        display_menu()
        menu = int(input("Please enter an option: "))
        if menu == 1:
            encode()
            pass
        if menu == 2:
            decode()
            pass
        if menu == 3:
            break
