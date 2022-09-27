
from cmath import phase
import numpy as np
import sampling
import matplotlib.pyplot as plt
import output
def DFT(samples,Td):
    """ 
    DFT 
    samples,Td => DFT,dF
    """
    Fs = 1/Td
    N = len(samples)
    result = []
    w0 = 2*np.pi*Fs
    samples = np.array(samples,dtype=complex)
    for k in range(-N//2,N//2):
        result.append(np.sum(samples[:]*np.exp(-k*np.array([i for i in range(N)])*1j*2*np.pi/N)))
    return np.array(result),Fs/N

def IDFT(F,dF):
    """ 
    IDFT 
    samples,Td => DFT,dF
    """
    Td = 1/dF
    N = len(F)
    result = []
    w0 = 2*np.pi*dF
    F = np.array(F,dtype=complex)
    for k in range(N):
        result.append(np.sum(F[:]*np.exp(k*np.array([i for i in range(-N//2,N//2)])*1j*2*np.pi/N)))
    return 1/N * np.array(result),Td

def four():
    ### get samples:
    res = sampling.start_window()

    dft,F = DFT(res,1)
    N = len(res)#
    w = [((i)*F)*2*np.pi for i in range(-N//2,N//2)]
    M = 1/(N)*np.abs(dft)
    phi = [phase(i) for i in dft]
    # plt.plot(w,np.abs(dft))
    # plt.show()
    idft = IDFT(dft,1)[0]
    # plt.plot(np.real(idft),np.imag(idft))
    # plt.show()
    # plt.plot(w,M)
    # plt.show()
    #print(w)
    lst = [(i,j,k) for i,j,k in zip(list(M),list(w),list(phi))]
    lst = sorted(lst,key= lambda x: x[0])[::-1]
    lst = list(zip(*lst))
    #output.start_window(M,w,phi,[(x,y)for x,y in zip(list(np.real(idft)+200),list(np.imag(idft)+250))])

    # visualisation:
    ## no need to pass idft better to pass just points directly but i wanted to check the correctness of idft (scale of sampling etc.)
    output.start_window(lst[0],lst[1],lst[2],[(x,y)for x,y in zip(list(np.real(idft)+200),list(np.imag(idft)+250))])
    
    pass
