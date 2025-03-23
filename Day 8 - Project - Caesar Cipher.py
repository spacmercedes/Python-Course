alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type encode or decode:  \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
       shifted_position =  alphabet.index(letter) + shift_amount
       shifted_position %= len(alphabet)
       cipher_text += alphabet[shifted_position]

    print(f"Here is the encided result: {cipher_text}")
# encrypt(text, shift)


def decrypt(original_text, shift_amount):
    decoded_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        decoded_text += alphabet[shifted_position]
    print(f"Here is the decoded result: {decoded_text}")



def caesar(direction_input):
    if direction_input == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)

caesar(direction)