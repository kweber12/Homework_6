import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import Methods as meth

G = np.array([[0,1,1,0,1,0],[0,0,0,1,1,0],[0,0,0,1,0,1],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])


S = np.zeros(4)
s = np.zeros(4)#generating matricies to hold the values of S and average s for each graph
dummy = np.zeros(100)
dummy1 = np.zeros(100)
w = np.zeros(400)
for z in range(400):
    n = 100
    m = 100
    p = z/(n-1)
    for r in range(2):
        G = meth.PRG(p,z,n,m)
        t = 0
        O = meth.DFS(G,t)
        a = np.amax(O, axis = 0)
        dummy[r] = np.count_nonzero(a > 0) + 1
        (d,e) = O.shape
        for j in range(d):
            w[j] = np.sum(O[j,:])
        duf = np.amax(w)
        duf = np.where(w == duf)
        O = np.delete(O, duf, axis = 1)
        dummy1[r] = np.count_nonzero(O > 0) + 1
    s[z] = np.sum(dummy1)/n
    S[z] = np.sum(dummy)/(100*n)

x = np.arange(0,4)
fig1 = plt.figure()
#fig.subplots_adjust(top=0.8)
ax = fig1.add_subplot(111)
#lab = 'Experimental'
#plt.plot(x, ALength, label = lab) 
lab = 'Experimental'
plt.plot(x,S , label = lab) 
plt.show()