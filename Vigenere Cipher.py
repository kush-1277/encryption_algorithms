import numpy as np
from pprint import pprint

######################################################################################################
########################################### VIGENERE CIPHER ##########################################
######################################################################################################

#################################### Substitution Function ###########################################
def ch_enc(ch, K):
    if ch.isalpha():
        encch = chr((((ord(ch) - 97) + K) % 26) + 97)
        return encch
    else:
        return ch
    
################################## Vigenere encryption function ######################################
def vigenere_enc(keyword, plaintext):
    
    plaintext = plaintext.replace(' ','')
    plaintext = plaintext.lower()
    # keyword is a string of arbitrary length
    # creates a list of indices of the keyword
    key_list = [ord(c)-97 for c in keyword]
    k_len = len(key_list)
    c = ""
    n = 0
    for p in plaintext:
        k = n%k_len
        encch = ch_enc(p, key_list[k])
        c = c + encch
        n = n + 1
    return c

######################################### Substitution Function ######################################
def ch_dec (ch, K):
    if ch.isalpha():
        decch = chr((((ord(ch) - 97) - K) % 26) + 97)
        return decch
    else:
        return ch

#################################### Vionegere decryption function ###################################
def vigenere_dec(keyword, ciphertext):
    key_list = [ord(c)-97 for c in keyword]
    k_len = len(key_list)
    p = ""
    n = 0
    for c in ciphertext:
        k = n%k_len
        dec = ch_dec(c, key_list[k])
        p = p + dec
        n = n + 1
    return p
