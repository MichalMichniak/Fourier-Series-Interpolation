import cmath
import numpy as np
from typing import List
import matplotlib.pyplot as plt
def FFT(x: List[float])->List[complex]:
    """
    FFT for n = 2^k
    args:
        x - input array List[float]
    return:
        FFT(x) List[complex]
    """
    lst = [0+0j for i in x]
    bin_len = len(bin(len(x)-1)[2:])
    N = len(lst)
    for n,i in enumerate(x):
        binary_repr = bin(n)[2:]
        n_zero = bin_len - len(binary_repr)
        binary_repr = "0"*n_zero + binary_repr
        int_repr = int(binary_repr[::-1],2)
        lst[int_repr] = i
    
    ###W_{N}^{k} = exp(-j2pik/N)
    
    M_group = 1
    lst_temp = lst.copy()
    while M_group != len(lst):
        M_group *=2
        lst_W = [0+0j for i in range(len(lst))]
        for n,i in enumerate(lst):
            k = (n*(N//M_group))%N
            lst_W[n] = cmath.rect(1,-(np.pi*2*k)/N)
        l = 0
        for n,i in enumerate(lst):
            ### Butterfly
            m = M_group//2
            if n%M_group < m%M_group:
                lst_temp[n] = lst[n] + lst[n+m]*lst_W[n]
                pass
            else:
                lst_temp[n] = lst[n]*lst_W[n] + lst[n-m]
                pass
        lst = lst_temp.copy()
    return lst

def IFFT(x: List[float])->List[complex]:
    """
    FFT for n = 2^k
    args:
        x - input array List[float]
    return:
        FFT(x) List[complex]
    """
    lst = [0+0j for i in x]
    bin_len = len(bin(len(x)-1)[2:])
    N = len(lst)
    for n,i in enumerate(x):
        binary_repr = bin(n)[2:]
        n_zero = bin_len - len(binary_repr)
        binary_repr = "0"*n_zero + binary_repr
        int_repr = int(binary_repr[::-1],2)
        lst[int_repr] = i
    ###W_{N}^{-k} = exp(j2pik/N)
    M_group = 1
    lst_temp = lst.copy()
    while M_group != len(lst):
        M_group *=2
        lst_W = [0+0j for i in range(len(lst))]
        for n,i in enumerate(lst):
            k = (n*(N//M_group))%N
            lst_W[n] = cmath.rect(1,(np.pi*2*k)/N)
        l = 0
        for n,i in enumerate(lst):
            ### Butterfly
            m = M_group//2
            if n%M_group < m%M_group:
                lst_temp[n] = lst[n] + lst[n+m]*lst_W[n]
                pass
            else:
                lst_temp[n] = lst[n]*lst_W[n] + lst[n-m]
                pass
        lst = lst_temp.copy()
    for n,i in enumerate(lst):
        lst[n] = np.real(i/N)
    return lst


# k = 10
# FS = 100.0
# x = [1 if i*(1/FS)%10 > 10 else 0 for i in range(2**k)]
# x = [np.sin(2*np.pi*2*i*(1/FS)) for i in range(2**k)]
# #plt.plot(x)
# #plt.show()
# y = FFT(x)
# y1 = IFFT(y)
# plt.title("IFFT(FFT)")
# plt.plot(np.array(y1)-np.array(x))
# plt.show()
# df = np.array([i*FS/len(x) for i in range(len(x)//2)])
# fig,ax = plt.subplots(3,1)
# fig.set_size_inches([10,10])
# ax[1].set_title("FFT")
# ax[0].set_title("signal")
# ax[0].plot([i/FS for i in range(len(x))],x)
# ax[2].set_title("FFT numpy")
# ax[1].plot(df,abs(np.array(y)[:len(y)//2]))
# ax[2].plot(df,abs(np.fft.fft(x)[:len(x)//2]))
# #plt.plot(np.real(y),np.imag(y))
# plt.show()
# fig,ax = plt.subplots(2,1)
# fig.set_size_inches([10,10])
# ax[0].set_title("FFT")
# ax[1].set_title("FFT numpy")
# ax[0].plot(np.real(np.array(y)),np.imag(np.array(y)))
# ax[1].plot(np.real(np.fft.fft(x)),np.imag(np.fft.fft(x)))
# #plt.plot(np.real(y),np.imag(y))
# plt.show()