SBOX = [
    # Box-1
[
[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
],

    # Box-2
[
[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
],

    # Box-3
[
[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]

],

    # Box-4
[
[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
],

    # Box-5
[
[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
],

    # Box-6
[
[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]

],

    # Box-7
[
[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
],

    # Box-8
[
[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
]]

# ========================================== S-BOX_LOOKUP ==========================================
def sbox_lookup(input6bitstr, sboxindex):
    
    DECtoBIN4 = {0: '0000', 1: '0001',
            2: '0010', 3: '0011',
            4: '0100', 5: '0101',
            6: '0110', 7: '0111',
            8: '1000', 9: '1001',
            10: '1010', 11: '1011',
            12: '1100', 13: '1101',
            14: '1110', 15: '1111'}
    row = 0
    col = 0
    
    col = int(input6bitstr[1:5],base=2)
    row = int(input6bitstr[0]+input6bitstr[5],base=2)
    sbox_value = SBOX[sboxindex][row][col]
    
    return DECtoBIN4[sbox_value]

# =========================================== BYTE-2-BITS ==========================================
def byteseq2binstr(byteseq):
    
    bitslist2 = [bin(int(b))[2:].zfill(8) for b in byteseq]
    allbitsstr = ''.join(bitslist2)
    
    return allbitsstr

# =========================================== PERMUTATION ==========================================
def Permutation(inputbitstr, perm_list):
    
    perm_str = ''.join([inputbitstr[b] for b in perm_list])
    return perm_str

# ============================================= XOR-BITS ===========================================
def XORbits(bitstr1,bitstr2):
    
    xor_result = ""
    for i in range(len(bitstr1)):
        if(bitstr1[i] == bitstr2[i]):
            xor_result = xor_result + '0'
        else:
            xor_result = xor_result + '1'    
    
    return xor_result

# ============================================= FUNCTION ===========================================
def functionF(bitstr32, keybitstr48):
    
    BOOK_E_TABLE = [32,1,2,3,4,5,
                    4,5,6,7,8,9,
                    8,9,10,11,12,13,
                    12,13,14,15,16,17,
                    16,17,18,19,20,21,
                    20,21,22,23,24,25,
                    24,25,26,27,28,29,
                    28,29,30,31,32,1]
    e_table = [x-1 for x in BOOK_E_TABLE]
    bitstr48 = Permutation(bitstr32, e_table)                              ## E-TABLE APPLIED
    
    bitstr_key = XORbits(bitstr48, keybitstr48)                            ## XORED 
    
    b6list = [bitstr_key[i:i+6] for i in range(0,len(bitstr_key), 6)]      # SPILT IN 8 ITEMS OF LENGTH 6 BITS
    post_sbox = ''
    for index in range(8):
        post_sbox = post_sbox + sbox_lookup(b6list[index], index)       ## CALLING SBOX LOOKUP
 
    P = [16, 7, 20, 21, 29, 12, 28, 17,
         1, 15, 23, 26, 5, 18, 31, 10,
         2, 8, 24, 14, 32, 27, 3, 9,
         19, 13, 30, 6, 22, 11, 4, 25]
    p = [x-1 for x in P]
    outbitstr32 = Permutation(post_sbox, p)                 ## FUNCTION'S SEPERATE PERMUTATION APPLIED
    
    return outbitstr32

# ============================================= DES_ROUND ===========================================
def des_round(LE_inp32, RE_inp32, key48):
    
    LE_out32 = RE_inp32
    RE_out32 = XORbits(LE_inp32, (functionF(RE_inp32, key48)))      ## GOING TO THE FUNCTION FOR EACH ROUND

    return LE_out32, RE_out32

# ========================================== KEY_GENERATE ==========================================
def des_keygen(C_inp, D_inp, roundindex):
    
    SHIFT = {
        1: 1, 2: 1,
        3: 2, 4: 2,
        5: 2, 6: 2,
        7: 2, 8: 2,
        9: 1, 10: 2,
        11: 2, 12: 2,
        13: 2, 14: 2,
        15: 2, 16: 1}
    
    C_out = C_inp[SHIFT[roundindex]:] + C_inp[:SHIFT[roundindex]]
    D_out = D_inp[SHIFT[roundindex]:] + D_inp[:SHIFT[roundindex]]

    PC2 = [14, 17, 11, 24, 1, 5, 3, 28,
           15, 6, 21, 10, 23, 19, 12, 4,
           26, 8, 16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55, 30, 40,
           51, 45, 33, 48, 44, 49, 39, 56,
           34, 53, 46, 42, 50, 36, 29, 32 ] 
    pc2 = [x-1 for x in PC2]
    key48 = Permutation((C_out+D_out), pc2)
    
    return key48, C_out, D_out

# ============================================ BYTE_ARRAY ==========================================
def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

# =========================================== DES_ENCYRPT ==========================================
def des_enc(inputblock, num_rounds, key64):
    

    if ((len(inputblock) % 8) != 0):
        diff = 8-(len(inputblock) % 8)
        for i in range(diff):        
            inputblock = inputblock + b'\x20'
            
    inp_bits = byteseq2binstr(inputblock)
    bin_inputkey64 = byteseq2binstr(key64)
    
    BookInitPermOrder = [58, 50, 42, 34, 26, 18, 10, 2, 
                         60, 52, 44, 36, 28, 20, 12, 4, 
                         62, 54, 46, 38, 30, 22, 14, 6, 
                         64, 56, 48, 40, 32, 24, 16, 8, 
                         57, 49, 41, 33, 25, 17, 9, 1, 
                         59, 51, 43, 35, 27, 19, 11, 3, 
                         61, 53, 45, 37, 29, 21, 13, 5, 
                         63, 55, 47, 39, 31, 23, 15, 7]
    
    InitPermOrder = [x-1 for x in BookInitPermOrder]               # APPLY INITIAL PERMUTATION
    inp_IP = Permutation(inp_bits, InitPermOrder)     # CREATED IP
    
    PC1 = [57, 49, 41, 33, 25, 17, 9,
           1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27,
           19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29,
           21, 13, 5, 28, 20, 12, 4 ]
    
    pc1 = [x-1 for x in PC1]
    key56 = Permutation(bin_inputkey64, pc1)          ## PC1 APPLIED    

    C = key56[:28]
    D = key56[28:]
    C_out = C
    D_out = D
    keys = []
    
    for i in range(num_rounds):
        key48, C_out, D_out = des_keygen(C_out, D_out, i+1)
        keys.append(key48)

    LE = inp_IP[:32]
    RE = inp_IP[32:]
    LE_OUT32 = LE
    RE_OUT32 = RE
    
    for i in range(num_rounds):
        LE_OUT32, RE_OUT32 = des_round(LE_OUT32, RE_OUT32, keys[i])      ## CALLING ROUND FUNCTION FOR EACH ROUND

    
    cipher = RE_OUT32 + LE_OUT32
    
    BookInvInitPermOrder = [40, 8, 48, 16, 56, 24, 64, 32, 
                            39, 7, 47, 15, 55, 23, 63, 31, 
                            38, 6, 46, 14, 54, 22, 62, 30, 
                            37, 5, 45, 13, 53, 21, 61, 29, 
                            36, 4, 44, 12, 52, 20, 60, 28, 
                            35, 3, 43, 11, 51, 19, 59, 27, 
                            34, 2, 42, 10, 50, 18, 58, 26, 
                            33, 1, 41, 9, 49, 17, 57, 25]
    
    InvInitPermOrder = [x-1 for x in BookInvInitPermOrder]
    cipher = Permutation(cipher, InvInitPermOrder)                        ## APPLIED INVERSE IP
    cipher = [cipher[i:i+8] for i in range(0,len(cipher), 8)]

    cipherblock = []
    for c in cipher:
        cipherblock.append(bitstring_to_bytes(c))
    
    cipherblock = b''.join(cipherblock)
    return cipherblock

# ========================================== DES_ENC_TEST ==========================================
def des_enc_test(input_fname, inputkey64, num_rounds, output_fname):
    
    finp = open(input_fname, 'rb')
    inpbyteseq = finp.read()
    finp.close()
    
    if ((len(inpbyteseq) % 8) != 0):
        diff = 8-(len(inpbyteseq) % 8)
        for i in range(diff):        
            inpbyteseq = inpbyteseq + b'\x20'

    block_list = [inpbyteseq[bl:bl+8] for bl in range(0, len(inpbyteseq), 8)]

    cipher = []
    for b in block_list:
        cipher.append(des_enc(b, num_rounds, bytes.fromhex(inputkey64)))    ### ENC_FUNC HARR ROUNDS KE LIYE

    cipherbyteseq = b''.join(cipher)
    fout = open(output_fname, 'wb')
    fout.write(cipherbyteseq)
    fout.close()
    
    
# ============================================ DES_DEC =============================================
def des_dec(inputblock, num_rounds, inputkey64):

    if ((len(inputblock) % 8) != 0):
        diff = 8-(len(inputblock) % 8)
        for i in range(diff):        
            inputblock = inputblock + b'\x20'
            
    inp_bits = byteseq2binstr(inputblock)
    bin_inputkey64 = byteseq2binstr(inputkey64)
    
    BookInitPermOrder = [58, 50, 42, 34, 26, 18, 10, 2,
                         60, 52, 44, 36, 28, 20, 12, 4,
                         62, 54, 46, 38, 30, 22, 14, 6, 
                         64, 56, 48, 40, 32, 24, 16, 8,
                         57, 49, 41, 33, 25, 17, 9, 1,
                         59, 51, 43, 35, 27, 19, 11, 3,
                         61, 53, 45, 37, 29, 21, 13, 5,
                         63, 55, 47, 39, 31, 23, 15, 7]
    
    InitPermOrder = [x-1 for x in BookInitPermOrder]
    cipher = Permutation(inp_bits, InitPermOrder)
    
    PC1 = [57, 49, 41, 33, 25, 17, 9,
           1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27,
           19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29,
           21, 13, 5, 28, 20, 12, 4]
    
    pc1 = [x-1 for x in PC1]
    key56 = Permutation(bin_inputkey64, pc1)          ## PC1 APPLIED    

    C = key56[:28]
    D = key56[28:]
    C_out = C
    D_out = D
    keys = []
    
    for i in range(num_rounds):
        key48, C_out, D_out = des_keygen(C_out, D_out, i+1)
        keys.append(key48)

    LE = cipher[:32]
    RE = cipher[32:]
    LE_OUT32 = LE
    RE_OUT32 = RE
    
    for i in range(num_rounds):
        LE_OUT32, RE_OUT32 = des_round(LE_OUT32, RE_OUT32, keys[15-i])

    plain = RE_OUT32 + LE_OUT32

    BookInvInitPermOrder = [40, 8, 48, 16, 56, 24, 64, 32, 
                        39, 7, 47, 15, 55, 23, 63, 31, 
                        38, 6, 46, 14, 54, 22, 62, 30, 
                        37, 5, 45, 13, 53, 21, 61, 29, 
                        36, 4, 44, 12, 52, 20, 60, 28, 
                        35, 3, 43, 11, 51, 19, 59, 27, 
                        34, 2, 42, 10, 50, 18, 58, 26, 
                        33, 1, 41, 9, 49, 17, 57, 25]
    InvInitPermOrder = [x-1 for x in BookInvInitPermOrder]
    plaintext = Permutation(plain, InvInitPermOrder)
    plaintext = [plaintext[i:i+8] for i in range(0,len(plaintext), 8)]
    
    plainblock = []
    for p in plaintext:
        plainblock.append(bitstring_to_bytes(p))
    
    plainblock = b''.join(plainblock)

    return plainblock
    
# ========================================== DES_DEC_TEST ==========================================
def des_dec_test(input_fname, inputkey64, num_rounds, output_fname):

    finp = open(input_fname, 'rb')
    cipherbyteseq = finp.read()
    finp.close()
    
    if ((len(cipherbyteseq) % 8) != 0):
        diff = 8-(len(cipherbyteseq) % 8)
        for i in range(diff):        
            cipherbyteseq = cipherbyteseq + b'\x20'
    
    block_list = [cipherbyteseq[bl:bl+8] for bl in range(0, len(cipherbyteseq), 8)]
  
    plain = []
    for b in block_list:
        plain.append(des_dec(b, num_rounds, bytes.fromhex(inputkey64))) 

    plainbyteseq = b''.join(plain)
    fout = open(output_fname, 'wb')
    fout.write(plainbyteseq)
    fout.close()
    
#des_enc_test("test_des.txt", "133457799BBCDFF1", 16, "test_enc_des.txt")
#des_dec_test("test_enc_des.txt", "133457799BBCDFF1", 16, "test_dec_des.txt")
