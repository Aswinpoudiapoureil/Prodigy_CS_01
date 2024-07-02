def encrypt(text, shift):
    result = ""


    for char in text:

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""

    for char in text:

        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)

        else:
            result += char

    return result


def main():
    while True:

        choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()

        message = input("Enter your message: ")

        shift = int(input("Enter the shift value: "))

        if choice == 'e':
            encrypted_message = encrypt(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == 'd':
            decrypted_message = decrypt(message, shift)
            print("Decrypted message:", decrypted_message)
        else:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

        go_again = input("Do you want to go again? (y/n): ").lower()
        if go_again != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
    print("Thanks for using the tool!")