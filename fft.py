import math

class FFT:
    @staticmethod
    def FFT(P):
        n = len(P)
        if n == 1:
            return P
        
        omega = complex(math.cos(2 * math.pi / n), math.sin(2 * math.pi / n))
        
        P_e = P[::2]
        P_o = P[1::2]
        
        y_e = FFT.FFT(P_e)
        y_o = FFT.FFT(P_o)
        
        y = [0] * n
        for j in range(n // 2):
            w = omega ** j
            y[j] = y_e[j] + w * y_o[j]
            y[j + n // 2] = y_e[j] - w * y_o[j]
        
        return y
        
    
    @staticmethod
    def IFFT(P):
        n = len(P)
        if n == 1:
            return P
        
        omega = complex(math.cos(2 * math.pi / n), -math.sin(2 * math.pi / n))
        
        P_e = P[::2]
        P_o = P[1::2]
        
        y_e = FFT.IFFT(P_e)
        y_o = FFT.IFFT(P_o)
        
        y = [0] * n
        for j in range(n // 2):
            w = omega ** j
            y[j] = y_e[j] + w * y_o[j]
            y[j + n // 2] = y_e[j] - w * y_o[j]
        
        return y