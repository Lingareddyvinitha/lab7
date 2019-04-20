import numpy as np
import cmath as c
import math
import matplotlib.pyplot as plt
Dp=0.7
Ds=0.01
Op=2*np.pi*500
Os=2*np.pi*1000
def butterworth(Dp,Ds,Op,Os):
	a=(1.0/Dp**2.0)-1
	b=(1.0/Ds**2.0)-1
	N=int(np.ceil(0.5*math.log10(a/b)/math.log10(Op/Os)))
	Oc=Op/(a**(1.0/(2.0*N)))
	return N,Oc
def chebyshev(Dp,Ds,Op,Os):
	c=((1.0/Dp**2.0)-1)
	b=((1.0/Ds**2.0)-1)
	N=int(np.ceil(np.arccosh(np.sqrt((b)/(c)))/(np.arccosh(Os/Op))))
	E=np.sqrt((1.0/Dp**2.0)-1)
	return N,E
O=2*np.pi*np.asarray(range(10000),'float32')
N,Oc=butterworth(Dp,Ds,Op,Os)
print N,Op,Oc,Os
hb=[]
for W in range(10000):
	H=(1/(np.sqrt(1+(W/Oc)**(2*N))))
	hb=np.append(hb,H)
print hb.shape
plt.subplot(211)
plt.plot(np.log10(O),20*np.log10(hb))
H=[]
H1=[]
N,E=chebyshev(Dp,Ds,Op,Os)
for i in range(10000):
	if((2*np.pi*i)<Op):
		#print i
		#print (i/Op)
		h1=(1.0/(1+(((E**2.0))*(np.cos(N*np.arccos((2*np.pi*i)/Op)))**2.0))**0.5)
		H.append(h1)
	else:
		#print i
		#print (i/Op)
		h1=(1.0/(1+(((E**2.0))*(np.cosh(N*np.arccosh((2*np.pi*i)/Op)))**2.0))**0.5)
		H.append(h1)
plt.subplot(212)
plt.plot(np.log10(O),20*np.log10(H))
plt.show()
