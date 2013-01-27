## One Time Pad
## Based on the Encryption / Decryption Functions from http://djao.math.uwaterloo.ca/cgi-bin/otp.cgi

# Creating Alphabet to Numeric Representation, character for space given number 27
alphadict = dict( (key, ord(key)-64) for key in string.ascii_uppercase )
alphadict[' '] = 0
reverse_alphadict = dict([[v,k] for k,v in alphadict.items()])

import re
import string

## Encryption Function
def encrypt(message,key):
    # Converting Inputs to Uppercase and removing extras
    message = re.sub('[^A-Z]', ' ',str.upper(message))
    key = re.sub('[^A-Z]', ' ',str.upper(key))
    # Truncation of string to the smaller of the two string lengths
    message = message[:min(len(message),len(key))]
    key = key[:min(len(message),len(key))]
    # Splitting strings to list
    m_list = list(message)
    k_list = list(key)
    # Converting list of characters to list of numbers based on alphadict
    m_list = [alphadict[element] for element in m_list]
    k_list = [alphadict[element] for element in k_list]
    # Generating the list for the ciphertext numbers
    c_list = [(m_list[i] + k_list[i]) % 27 for i in range(0,len(m_list))]
    # Mapping ciphertext numbers to alphabet string
    c_list = [reverse_alphadict[element] for element in c_list]
    cipher = ''.join(c_list)
    print message + '\n' + key + '\n' + cipher

## Decryption Function
def decrypt(cipher,key):
    # Converting Inputs to Uppercase and removing extras
    cipher = re.sub('[^A-Z]', ' ', str.upper(cipher))
    key = re.sub('[^A-Z]', ' ', str.upper(key))
    # Truncation of string to the smaller of the two string lengths
    cipher = cipher[:min(len(cipher),len(key))]
    key = key[:min(len(cipher),len(key))]
    # Splitting strings to list
    c_list = list(cipher)
    k_list = list(key)
    # Converting list of characters to list of numbers based on alphadict
    c_list = [alphadict[element] for element in c_list]
    k_list = [alphadict[element] for element in k_list]
    # Generating the list for the message numbers
    m_list = [(c_list[i] - k_list[i]) % 27 for i in range(0,len(c_list))]
    # Mapping message numbers to alphabet string
    m_list = [reverse_alphadict[element] for element in m_list]
    message = ''.join(m_list)
    print cipher + '\n' + key + '\n' + message
