import numpy as np
import pylab as plb
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp
from numpy.random import normal
#x = ar(range(10))
#y = ar([0,1,2,3,4,5,4,3,2,1])

x = ar([15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])

y = normal(range(15,120))  #y = ar([12.55765195,  15.42448838,  17.60238472,  17.77149525, 17.5869718 ,  19.25143399,  21.1891268 ,  25.02668415, 24.21922946,  23.10215553,  22.99254442,  23.3306961 , 31.06135822,  30.02534135,  32.14659856,  27.26999177, 32.46607407,  32.28540668,  32.1152903 ,  39.19816915, 35.8216122 ,  35.61063219,  35.16722011,  37.89010265, 36.37530399,  41.64665283,  43.80971948,  43.10783247, 42.63421608,  42.34609761,  43.40487632,  44.86366347, 49.02171085,  48.56617233,  49.14776781,  49.35426613, 51.83082986,  54.23208068,  52.52850186,  55.30975876, 55.62861122,  55.51957839,  58.60538186,  59.18199243, 57.06817628,  62.74493714,  61.48450258,  59.11690968, 62.08191928,  66.28639904,  65.99050398,  64.99772861, 67.97596372,  67.37187263,  69.18503462,  69.31192402, 69.82072897,  72.93000021,  74.19026178,  78.60357122, 77.82544065,  76.20919069,  77.61077278,  78.40203571, 80.09608423,  78.813157  ,  81.62072559,  81.4621605 , 80.68154153,  81.9867835 ,  85.54615116,  83.88260234, 86.96526725,  91.38158271,  87.77131768,  88.61839433, 92.87406287,  93.27895396,  94.0503961 ,  92.78925051, 92.18058856,  96.10834158,  96.85841747, 103.48453111, 100.97013721,  98.82546079,  99.61030249, 100.36451561, 103.26409733, 106.39141209, 105.37148622, 107.27322674, 109.60608996, 106.32678394, 109.10292624, 113.4610832 , 109.39585594, 113.91583675, 108.71820324, 113.55007181, 115.49579354, 117.48117207, 117.13502716, 121.04867476, 120.19924954])

n = len(x)                          #the number of data
mean = sum(x*y)/n                   #note this correction
#sigma = sum(y*(x-mean)**2)/n        #note this correction 

def pdf(x,mu,s):
    return (exp(-(x-mu)/s))/(s*(1+exp(-(x-mu)/s))**2)

popt,pcov = curve_fit(pdf,x,y,p0=[mean,10],maxfev=5000)
print(*popt)
#print(pcov)
plt.plot(x,y,label='dados') #plt.plot(x,y,'b+:',label='data')
plt.plot(x,pdf(x,*popt), 'g--', label=r'fit: $\mu$=%5.3f, s=%5.3f,' % tuple(popt))#plt.plot(x,pdf(x,*popt),'ro:',label='fit')
plt.legend()
plt.title('Adequação a Distribuição Logística')
plt.xlabel('Horizontal (x)')
plt.ylabel('Vertical (y)')
plt.show()
