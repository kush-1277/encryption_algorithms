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
    return p
