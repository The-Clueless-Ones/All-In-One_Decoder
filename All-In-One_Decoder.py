"""
Title: All-In-One Decoder/Converter

Creator: Haris "5w464l1c10u5"

Purpose: To make one script that can decode text easily, mostly meant for CTF Challenges.

This Script Decodes/converts:
base64
base32
hex to decimal
hex to binary
binary to hex
binary to decimal
decimal to binary
decimal to hex
decimal to Ascii
Ascii to decimal
Octal to decimal
Morse code to Ascii
Vigenere Cipher ---- NOT DONE
Ceasar Box Cipher ---- NOT DONE
Rail Fence Cipher
ROT13 (1-26)
At-bash Cipher
"""
#!/usr/local/bin/python3
import base64
import codecs

#base64
def base64_decode(x):
    b64_decode = base64.b64decode(x)
    b64_decode = str(b64_decode)
    final = b64_decode.replace("b'", "").replace("'", "")
    print('Base64 Decode ----------------> ' + final)

#base32
def base32_decode(x):
    b32_decode = base64.b32decode(x)
    b32_decode = str(b32_decode)
    final = b32_decode.replace("b'", "").replace("'", "")
    print('Base32 Decode ----------------> ' + final)
#Hex to Decimal
def Hex2Decimal(x):
    dec = int(x, 16);
    print('Hex to Decimal -------------> ',str(dec));

#Hex to Binary
def Hex2Binary(x):
    dec = int(x, 16);
    print('Hex to Binary -----------------> ' + bin(dec).replace('b',''))

#Binary to Hex
def Binary2Hex(x):
    x = x.replace(" ","")
    Hex = hex(int(x, 2))
    print('Binary to Hex ------------------> ' + Hex)

#Binary to Decimal
def Binary2Decimal(x):
    x = x.replace(" ","")
    Hex = hex(int(x, 2))
    dec = int(Hex, 16);
    print('Binary to Decimal -----------------> ' + str(dec))

#Decimal to Binary
def Decimal2Binary(x):
    dec = bin(int(x)).replace('b','')
    print('Decimal to Binary ------------------> ' + dec)

#Decimal to Hex
def Decimal2Hex(n):
    Hex = hex(int(n))
    print('Decimal to Hex ---------------->' + Hex)

#Decimal to Ascii
def Decimal2Ascii(x):
    list = x.split()
    print('------------Decimal to Ascii: START ------------------')
    for x in list:
        x = int(x)
        x = chr(x)
        print(x)
    print('------------Decimal to Ascii: END --------------------')

#Ascii to Decimal
def Ascii2Decimal(x):
    split = list(x)
    print('------------Ascii to Decimal: START ------------------')
    for x in split:
        x = ord(x)
        print(x)
    print('------------Ascii to Decimal: END --------------------')

#Octal to Decimal
def Octal2Decimal(x):
    decimal = int(x, 8)
    print('Octal to Decimal --------------------> ' + str(decimal))

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

CODE_REVERSED = {value:key for key,value in CODE.items()}

#Morse code to Ascii
def MorseCode2Ascii(s):
    Ascii = ''.join(CODE_REVERSED.get(i) for i in s.split())
    print('Morse Code to Ascii ------------------> ' + Ascii)

#Fence for the Rail-Fence
def fence(lst, numrails):
    fence = [[None] * len(lst) for n in range(numrails)]
    rails = list(range(numrails - 1)) + list(range(numrails - 1, 0, -1))
    for n, x in enumerate(lst):
        fence[rails[n % len(rails)]][n] = x

    if 0: # debug
        for rail in fence:
            print(''.join('.' if c is None else str(c) for c in rail))

    return [c for rail in fence for c in rail if c is not None]

#Rail-Fence Decoder
def Rail_Fence_Decode(text, n):
    rng = list(range(len(text)))
    pos = fence(rng, n)
    Decode = ''.join(text[pos.index(n)] for n in rng)
    print('Rail Fence Decode with Rail of #' + str(n) + ' -----------------> ' + Decode)

#Decodes ROT13 straight as is
def ROT13_Decoder(text):
    x = codecs.encode(text, 'rot_13')
    print('ROT13 Decoded ---------------------> ' + x)

dict1 = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5,
        'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10,
        'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15,
        'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20,
        'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}

dict2 = {0 : 'Z', 1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D', 5 : 'E',
        6 : 'F', 7 : 'G', 8 : 'H', 9 : 'I', 10 : 'J',
        11 : 'K', 12 : 'L', 13 : 'M', 14 : 'N', 15 : 'O',
        16 : 'P', 17 : 'Q', 18 : 'R', 19 : 'S', 20 : 'T',
        21 : 'U', 22 : 'V', 23 : 'W', 24 : 'X', 25 : 'Y'}

#Function used for the rot13_changeable function later
def ROT13_decrypt(message, shift):
    decipher = ''
    for letter in message:
        if(letter != ' '):
            num = ( dict1[letter] - shift + 26) % 26
            decipher += dict2[num]
        else:
            decipher += ' '
    return decipher

#Decodes ROT13, but is editable to other shifts as well
def rot13_changeable(n):
    message = n
    shift = 13
    result = ROT13_decrypt(message.upper(), shift)
    print ('ROT'+ str(shift) + ' Decoded ----------------------> ' + result)

lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
		'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
		'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
		'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
		'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}

#Atbash function which is used later
def atbash(message):
	cipher = ''
	for letter in message:
		if(letter != ' '):
			cipher += lookup_table[letter]
		else:
			cipher += ' '
	return cipher

#Actual Atbash usage
def atbash_decode(text):
    x = atbash(text.upper())
    print('Atbash decode ---------------------------> ' + x)
#--------------------------------------------------------------------#
title = """
TITLE: ALL-IN-ONE CONVERTER / DECODER

CREATOR: HARIS "5w464l1c10u5"
"""

note = """____________________________________________________
NOTE:

Ascii2Decimal: seperates each letter then converts it

Rail-Fence decode: Enter number for decode in the try/except for it (line 282) (default = 3)
_____________________________________________________

"""
print(title)
print(note)
#User Input
input = input('Enter input here: ')

try:
    base64_decode(input)
except:
    print("This is not Base64")

try:
    base32_decode(input)
except:
    print("This is not Base32")

try:
    Hex2Decimal(input)
except:
    print("This is not Hex")

try:
    Hex2Binary(input)
except:
    print("This is not Hex")

try:
    Binary2Hex(input)
except:
    print("This is not Binary")

try:
    Binary2Decimal(input)
except:
    print("This is not Binary")

try:
    Decimal2Binary(input)
except:
    print("This is not Decimal")

try:
    Decimal2Hex(input)
except:
    print("This is not Decimal")

try:
    Decimal2Ascii(input)
except:
    print("This is not Decimal")

try:
    Ascii2Decimal(input)
except:
    print("This is not Ascii")

try:
    Octal2Decimal(input)
except:
    print("This is not Octal")

try:
    MorseCode2Ascii(input)
except:
    print("This is not Morse Code")

try:
    Rail_Fence_Decode(input, 3)
except:
    print("This is not Rail Fence Encoded")

try:
    ROT13_Decoder(input)
except:
    print("This is not Rot13 Encoded")

try:
    rot13_changeable(input)
except:
    print("This is not Rot(n) Encoded")

try:
    atbash_decode(input)
except:
    print("This is not atbash Encoded")
