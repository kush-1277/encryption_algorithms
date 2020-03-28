import numpy as np
from pprint import pprint

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
