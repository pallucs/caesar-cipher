alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
if direction == 'encode':
  def encrypt(text, shift):
    encrypted_word = ''
    for x in text:
      if x == ' ':
        encrypted_word += ' '
        continue
      index = alphabet.index(x)
      total_shift = index + shift
      if total_shift > len(alphabet) and alphabet[index] == alphabet[-1]:
        # word_shift = ''.join(alphabet[0:shift])
        encrypted_word +=str(alphabet[0:shift][-1])
      elif total_shift > len(alphabet) and alphabet[index] != alphabet[-1]:
        first_shift = alphabet[index+1:]
        # word_shift = str(alphabet[0:shift - len(first_shift)])
        encrypted_word += str(alphabet[0:shift - len(first_shift)][-1])
      else:
        word_shift = alphabet[index + shift]
        encrypted_word += word_shift
    return encrypted_word

  word = encrypt(text, shift)
  print(word)

if direction == 'decode':
  def decode(text, shift):
    decrypted_word = ''
    for x in text:
      if x == ' ':
        decrypted_word += ' '
        continue
      index = alphabet.index(x)
      total_shift = index - shift
      if total_shift < 0 and alphabet[index] == alphabet[0]:
        # word_shift = ''.join(alphabet[-1:-(shift)])
        decrypted_word += str(alphabet[total_shift])
        # decrypted_word +=alphabet[total_shift]
      elif total_shift < 0 and alphabet[index] != alphabet[0]:
        first_shift = alphabet[0:index]
        # word_shift =  str(alphabet[-1:-(shift - len(first_shift))])
        decrypted_word += str(alphabet[-(shift - len(first_shift))])
        # decrypted_word +=alphabet[total_shift]
      else:
        word_shift = alphabet[index - shift]
        decrypted_word += word_shift
    return decrypted_word
  
  word = decode(text, shift)
  print(word)

