def K_d(a,b):   #Kronecker delta
    if a==b:
        return(1)
    if a!=b:
        return(0)
    
def Generate_Pauli_matrix(i):
    mtx=np.array([[K_d(i,3),K_d(i,1)-1j*K_d(i,2)],
                  [K_d(i,1)+1j*K_d(i,2),-K_d(i,3)]])
    return(mtx)

print('Pauli X:',Generate_Pauli_matrix(1))