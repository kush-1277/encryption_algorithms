#!/usr/bin/env python
# coding: utf-8

# kacharya | 116694803 | Kush Dilip Acharya
##############################################################################################
##############################################################################################
##############################################################################################
import random
import hmac
import hashlib

def xor(byteseq1, byteseq2):
    # First we convert each byte to its int value
    l1 = [b for b in byteseq1]
    l2 = [b for b in byteseq2]

    l1xorl2 = [bytes([elem1^elem2]) for elem1,elem2 in zip(l1,l2)]
    
    result = b''.join(l1xorl2) # used b coz we need btye values
    return result


########################################## FUNCTION #########################################
def F(byteseq, k):    # create a hmac sha1 
    h = hmac.new(k, byteseq, hashlib.sha1)
    return h.digest()[:8]


################################# MAIN BLOCK PROCESSING #####################################
def feistel_block(LE_inp, RE_inp, k):
    LE_out = RE_inp
    RE_out = xor(LE_inp, (F(RE_inp, k)))
    return LE_out, RE_out


####################################### KEY GENERATOR #######################################
keylist = []
def gen_keylist(keylenbytes, numkeys, seed):
    random.seed(seed) #sets starting point to start random no.
    for i in range(numkeys):
        l = [random.randint(0,255) for i in range(keylenbytes)]
        keylist.append(bytes(l))
    return keylist

###################################### MAIN DECRYPTION #######################################
def feistel_dec(inputblock, num_rounds, seed):
    keylist = gen_keylist(8, num_rounds, seed)
    LE = inputblock[:4]
    RE = inputblock[4:8]
    LE_out = LE
    RE_out = RE
    
    for i in range(num_rounds):
        LE_out, RE_out = feistel_block(LE_out, RE_out, keylist[num_rounds - 1 - i])
        
    plainblock = RE_out + LE_out
    return plainblock


#################################### TEST MAIN DECRYPTION #####################################
def feistel_dec_test(input_fname, seed, num_rounds, output_fname):
    finp = open(input_fname, 'rb')
    inpbyteseq = finp.read()
    finp.close()
    
    if ((len(inpbyteseq)%8) != 0):
        diff = 8-(len(inpbyteseq) % 8)
        for i in range(diff):        
            inpbyteseq = inpbyteseq + b'\x20'      
    
    block_list = [inpbyteseq[bl:bl+8] for bl in range(0, len(inpbyteseq), 8)]
    cipher = []
    for b in block_list:
        cipher.append(feistel_dec(b, num_rounds, seed))

    cipherbyteseq = b''.join(cipher)
    fout = open(output_fname, 'wb')
    fout.write(cipherbyteseq)
    fout.close()
