from alphabet import alphabet
from logo import logo
print(logo)

def encrypt(plain_text , shift_amount):
    shifted_text = "" #blank str for fresh word applied shift
    for ch in plain_text:
        position = alphabet.index(ch)
        new_position = position + shift_amount
        # yeni harfi bulalım
        new_letter = alphabet[new_position]
        shifted_text += new_letter
    print(f"The encoded text is: {shifted_text}") 

def decrypth(plain_text , shift_amount):
    shift_amount = -1 * shift_amount
    shifted_text = ""
    for ch in plain_text:
        position = alphabet.index(ch)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        shifted_text += new_letter
    print(f"The decoded text is: {shifted_text}")
    
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt. Type stop for exit...:\n")
    if direction == "stop":
        break
    
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(plain_text=text, shift_amount=shift) 
        
    elif direction == "decode":
        decrypth(plain_text= text , shift_amount=shift)
    else:
        print("invalid text given try again")
