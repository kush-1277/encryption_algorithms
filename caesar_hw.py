# Simple Caesar's Cipher Demo Code
import sys

#Encoding Function
def caesar_str_enc(plaintext, K):
    ciphertext=""
    for ch in plaintext:
        encch = caesar_ch_enc(ch, K)
        ciphertext = ciphertext + encch
    return ciphertext

#Core Encoding Function
def caesar_ch_enc(ch, K):
    if ch.isalpha():
        encch = chr((((ord(ch) - 97) + K) % 26) + 97)
        return encch
    else:
        return ch
    
#Decoding Function
def caesar_str_dec(ciphertext, K):
    plaintext = ""
    for ch in ciphertext:
        decch = caesar_ch_dec(ch, K)
        plaintext = plaintext + decch
    return plaintext

#Core Decoding Function
def caesar_ch_dec (ch, K):
    if ch.isalpha():
        decch = chr((((ord(ch) - 97) - K) % 26) + 97)
        return decch
    else:
        return ch


def test_module():
    k_char = sys.argv[1]
    K = int(k_char)
    input_str = sys.argv[2]

    encstr = caesar_str_enc(input_str, K)
    print(encstr)
    decstr = caesar_str_dec(encstr, K)
    print(decstr)
    
if __name__=="__main__":
    test_module()

# In this case, if you call your file like this:
# >python caear_hw.py 3 "string to be encoded"
# it should first print the above string
# then the encrypted version of it
# and next the decrypted version of it i.e., the riginal one


# In[ ]:




