import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def caeser(text,shift,direction):
  crypt = ""
  for character in text:
    if character not in alphabet:
      crypt = crypt + character
    else:
      position = alphabet.index(character)
      if direction == "encode":
        direction_position = position + shift
        alphabet_len = len(alphabet)-1
      else:
        direction_position = position - shift
        alphabet_len = len(alphabet)

      if direction_position > alphabet_len:
        diff = (direction_position) - alphabet_len
        crypt = crypt + alphabet[diff - 1]
      elif direction_position < 1:
        diff = direction_position + alphabet_len
        crypt = crypt + alphabet[diff]
      else:
        crypt = crypt + alphabet[direction_position]
  
  print(f"The {direction}d word is {crypt}")

is_exit = False

while not is_exit:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caeser(text,shift,direction)
  restart_program = input("Type 'yes' if you want to go again or 'no' :").lower()
  if not restart_program == "yes":
    is_exit = True
  
# def encrypt(text,shift):
#   encodedword=""
#   for character in text:
#     position = alphabet.index(character)
    
#     if position + shift > len(alphabet)-1:
#       diff = (position + shift) - len(alphabet-1)
#       encodedword = encodedword + alphabet[diff - 1]
#     else:
#       encodedword = encodedword + alphabet[position + shift]
#   print(f"The encoded text is {encodedword}")

# def decode():
#   decodedword=""
#   for character in text:
#     position = alphabet.index(character)
#     if position - shift < 1:
#       diff = (position - shift) + len(alphabet)
#       decodedword = decodedword + alphabet[diff]
#     else:
#       decodedword = decodedword + alphabet[position - shift]
#   print(f"The decoded text is {decodedword}")
