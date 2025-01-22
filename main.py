def caesar_cipher(text, shift, mode):
    result = ""
    shift = shift % 26  # Ensure the shift value is within the alphabet range

    for char in text:
        if char.isalpha():
            # Determine the shift direction
            shift_amount = shift if mode == "encrypt" else -shift
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift_amount) % 26 + start)
            result += new_char
        else:
            result += char  # Keep non-alphabetic characters unchanged

    return result


def get_input():
    message = input("Enter the message: ")
    while True:
        try:
            shift = int(input("Enter the shift value (integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the shift value.")
    return message, shift


if __name__ == "__main__":
    print("Caesar Cipher Program")
    while True:
        message, shift = get_input()
        mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()

        if mode in ["encrypt", "decrypt"]:
            result = caesar_cipher(message, shift, mode)
            print(f"The resulting message is: {result}")
        else:
            print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")

        # Check if the user wants to continue
        continue_choice = input("Do you want to continue? Type 'done' to finish or press Enter to continue: ").strip().lower()
        if continue_choice == "done":
            print("Thank you for using the Caesar Cipher Program! Goodbye!")
            break
