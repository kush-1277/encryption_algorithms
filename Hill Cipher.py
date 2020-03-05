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


######################################################################################################
############################################# HILL CIPHER ############################################
######################################################################################################

############## 1 - clean up the inverting operations explained above to get a matrix inversion-mod-26 function ###############
def matrixinvmod26(M):
    Mod26invTable = {}
    for m in range(26):
        for n in range(26):
            if (m*n)%26==1:
                Mod26invTable[m] = n
    
    M_inverse = np.linalg.inv(M)    # inverse kiya
    M_det = np.linalg.det(M)    # determinent nikala
    M_det26 = M_det%26          # MOD 26 kiya determinent kiya
    
    if M_det26 in Mod26invTable:
        M_det_inv26 = Mod26invTable[M_det26]
    else:
        M_det_inv26 = None                  
        exit()
        
    M_adj = M_det * M_inverse
    M_adj26 = M_adj % 26
    M_inv26 = (M_det_inv26 * M_adj26) % 26
    Minv26 = np.matrix.round(M_inv26, 0) % 26
    return Minv26

################################## Hill encryption function ########################################
def hill_enc(M, plaintext):
    plaintext = plaintext.replace(' ','')
    plaintext = plaintext.lower()
    
    p_list = []
    p_mat = []
    mat = [c for c in plaintext]
    if ((len(mat)%3) != 0):
        diff = 3-(len(mat)%3)
        for i in range(diff):        
            mat.append('x')
    p_list = [ord(c)-97 for c in mat]

    for i in range(0,len(p_list), 3):
        sub = p_list[i:i+3]
        p_mat.append(sub)

    res = (np.matmul(p_mat, M)) % 26
    cipher = [chr(c+97) for c in [val for sublist in res for val in sublist]]
    c = ''.join(cipher)
    #print(c, "\n")
    return c

################################### Hill decryption function ######################################
def hill_dec(M, ciphertext):
    
    c_list = []
    c_mat = []
    mat = [p for p in ciphertext]
    c_list = [ord(c)-97 for c in mat]           # list of ascii values
    
    for i in range(0,len(c_list), 3):
        sublist = c_list[i:i+3]
        c_mat.append(sublist)
    #print(c_mat)
    
    key = matrixinvmod26(M)
    
    p_mat = (np.matmul(c_mat, key)) % 26
    p_int_mat = []
    for i in range(len(p_mat)):
        temp = []
        for j in range(len(p_mat[i])):
            temp.append(int(p_mat[i][j]))
        p_int_mat.append(temp)

    plain = [chr(c+97) for c in [val for sub in p_int_mat for val in sub]]
    p = ''.join(plain)
    #print(p)
    return p
