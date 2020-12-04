import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import Methods as meth
import pickle

z = 4
p = 10


length = np.array([])
ALength = np.array([])
for p in range(10,13):
    print(p)
    n = 2**p
    m = 4*n
    prob = z/(n-1)
    G = meth.PRG(prob,z,n,m)
    for i in range(10):
        s = np.random.randint(100)
        O = meth.BFS(G,s,10)
        length = np.append(length,O.size)
    ALength = np.append(ALength, np.sum(length)/length.size)

pickle_out = open("dict.pickle","wb")
pickle.dump(ALength,pickle_out)
pickle_out.close()


x = np.arange(10,13)
x = 2**x
fig = plt.figure()
#fig.subplots_adjust(top=0.8)
ax = fig.add_subplot(111)
lab = 'Experimental'
plt.plot(x, ALength, label = lab) 
lab = 'Theoretical'
plt.plot(x, np.log(x)/np.log(z), label = lab) 
plt.show()