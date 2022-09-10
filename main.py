alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))




def encrypt(t,s):
  array=""

  for i in t:
    c=alphabet.index(i)+s
    array+=alphabet[c]
  print(array)




def decrypt(t,s):
  array=""

  for i in t:
    c=alphabet.index(i)-s
    array+=alphabet[c]
  print(array)

if(direction=="encode"):
  encrypt(t=text,s=shift)
else:
  decrypt(t=text,s=shift)