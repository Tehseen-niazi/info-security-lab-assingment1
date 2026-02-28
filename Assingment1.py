# Function to encrypt a message using Caesar cipher
def caesar_encrypt(text, shift):
    encrypted_text = ""  # Initialize an empty string to store the encrypted result
    for char in text:  # Loop through each character in the input text
        if char.isalpha():  # Check if the character is a letter
            # Determine ASCII offset: 65 for uppercase letters, 97 for lowercase
            ascii_offset = 65 if char.isupper() else 97
            # Shift the character by the given value and wrap around using modulo 26
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            # Add the encrypted character to the result string
            encrypted_text += encrypted_char
        else:
            # If character is not a letter (punctuation, number, space), keep it unchanged
            encrypted_text += char
    return encrypted_text  # Return the final encrypted string

# Function to decrypt a message using Caesar cipher
def caesar_decrypt(ciphertext, shift):
    # Decryption is just encryption with a negative shift
    return caesar_encrypt(ciphertext, -shift)

# Main program block
if __name__ == "__main__":
    message = "Hello, World!"  # Original message to encrypt
    shift_value = 3  # Number of positions to shift in the Caesar cipher
    encrypted = caesar_encrypt(message, shift_value)  # Encrypt the message
    print("Encrypted:", encrypted)  # Print encrypted message
    decrypted = caesar_decrypt(encrypted, shift_value)  # Decrypt the message
    print("Decrypted:", decrypted)  # Print decrypted message (should match original)