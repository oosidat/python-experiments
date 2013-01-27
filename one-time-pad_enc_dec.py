## One Time Pad
## Based on the Encryption / Decryption Functions from http://djao.math.uwaterloo.ca/cgi-bin/otp.cgi

import re
import string
import os

# Creating Alphabet to Numeric Representation, character for space given number 0
alphadict = dict( (key, ord(key)-64) for key in string.ascii_uppercase )
alphadict[' '] = 0
reverse_alphadict = dict([[v,k] for k,v in alphadict.items()])


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

cipher1 = file('C:/Users/Osama Sidat/Documents/Python Projects/a1q3_c1.txt', 'r')
cipher2 = file('C:/Users/Osama Sidat/Documents/Python Projects/a1q3_c2.txt', 'r')
cipherstring1 = cipher1.read()
cipherstring2 = cipher2.read()
#print cipherstring1
#print cipherstring2
c1_list = list(cipherstring1)
c2_list = list(cipherstring2)
c1_list = [alphadict[element] for element in c1_list]
c2_list = [alphadict[element] for element in c2_list]
c1c2_list = [(c1_list[i] - c2_list[i]) % 27 for i in range(0,len(c1_list))]
c1c2_list = [reverse_alphadict[element] for element in c1c2_list]
c1minusc2 = ''.join(c1c2_list)
print c1minusc2
starts = [match.start() for match in re.finditer(re.escape('MPRISES'), c1minusc2)]
print starts
