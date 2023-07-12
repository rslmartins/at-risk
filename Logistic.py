import numpy as np
import pylab as plb
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp
from numpy.linalg import norm

x = ar([15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119])

y = ar([0.019047619047619, 0.00952380952381, 0.019047619047619, 0.038095238095238, 0.047619047619048, 0.038095238095238, 0.028571428571429, 0.104761904761905, 0.057142857142857, 0.047619047619048, 0.095238095238095, 0.104761904761905, 0.085714285714286, 0.066666666666667, 0.152380952380952, 0.190476190476191, 0.152380952380952, 0.152380952380952, 0.123809523809524, 0.190476190476191, 0.20952380952381, 0.095238095238095, 0.219047619047619, 0.257142857142857, 0.2, 0.142857142857143, 0.219047619047619, 0.257142857142857, 0.276190476190476, 0.238095238095238, 0.247619047619048, 0.323809523809524, 0.314285714285714, 0.266666666666667, 0.2, 0.238095238095238, 0.304761904761905, 0.257142857142857, 0.257142857142857, 0.276190476190476, 0.352380952380952, 0.161904761904762, 0.2, 0.247619047619048, 0.228571428571429, 0.2, 0.219047619047619, 0.276190476190476, 0.257142857142857, 0.257142857142857, 0.257142857142857, 0.238095238095238, 0.333333333333333, 0.247619047619048, 0.266666666666667, 0.380952380952381, 0.247619047619048, 0.247619047619048, 0.276190476190476, 0.2, 0.190476190476191, 0.285714285714286, 0.247619047619048, 0.333333333333333, 0.219047619047619, 0.266666666666667, 0.266666666666667, 0.219047619047619, 0.20952380952381, 0.323809523809524, 0.266666666666667, 0.2, 0.228571428571429, 0.304761904761905, 0.238095238095238, 0.304761904761905, 0.180952380952381, 0.152380952380952, 0.095238095238095, 0.171428571428571, 0.2, 0.257142857142857, 0.123809523809524, 0.161904761904762, 0.247619047619048, 0.142857142857143, 0.171428571428571, 0.161904761904762, 0.104761904761905, 0.161904761904762, 0.104761904761905, 0.171428571428571, 0.114285714285714, 0.152380952380952, 0.076190476190476, 0.057142857142857, 0.047619047619048, 0.066666666666667, 0.038095238095238, 0.019047619047619, 0.038095238095238, 0.00952380952381, 0.028571428571429, 0.019047619047619, 0.038095238095238])

n = len(x)                          #the number of data
mean = sum(x*y)/n                   #note this correction
#sigma = sum(y*(x-mean)**2)/n        #note this correction 

def pdf(x, mean,  s):
    return exp((mean-x)/ s)/( s*(1+exp((mean-x)/ s))**2)

popt,pcov = curve_fit(pdf,x,y,p0=[mean,20],maxfev=5000)
y2=pdf(x,*popt)
print("Erro de: "+str(norm(y-y2)))
print(*popt)
#print(pcov)
plt.plot(x,y,label='dados') #plt.plot(x,y,'b+:',label='data')
plt.plot(x,pdf(x,*popt), 'g--', label=r'fit: $\mu$=%5.3f, s=%5.3f,' % tuple(popt))#plt.plot(x,pdf(x,*popt),'ro:',label='fit')
plt.legend()
plt.title('Adequação a Distribuição Logística')
plt.xlabel('Horizontal (x)')
plt.ylabel('Vertical (y)')
plt.show()
