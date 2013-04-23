shift = 3

def encode_char(x):
    if x == '_':
        return 'b'
    elif x == '.':
        return 'c'
    elif x == 'x':
        return '_'
    elif x == 'y':
        return '.'
    elif x == 'z':
        return 'a'
    else:
        return chr(ord(x) + shift)
    
def caesar_encrypt(plain):
    if len(plain) == 0:
        return ''
    else:
        return encode_char(plain[0]) + caesar_encrypt(plain[1: ])
    
def decode_char(x):
    if x == 'b':
        return '_'
    elif x == 'c':
        return '.'
    elif x == '_':
        return 'x'
    elif x == '.':
        return 'y'
    elif x == 'a':
        return 'z'
    else:
        return chr(ord(x) - shift)
    
def caesar_decrypt(cipher):
    if len(cipher) == 0:
        return ''
    else:
        return decode_char(cipher[0]) + caesar_decrypt(cipher[1: ])