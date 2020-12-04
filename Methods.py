import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

def PRG(p,z,n,m):
    G = np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            x = np.random.randint(100)
            w = 100*p
            if x <= w:
                G[i,j] = 1
            if np.count_nonzero(G == 1) == m:
                break
        if np.count_nonzero(G == 1) == m:
            break
    return G

def BFS(G,s,e):
    q = np.array([s])
    (n,d) = G.shape
    visited = np.array([s])
    prev = []
    while q.size != 0:
        c = np.where(G[q[0],:] == 1)
        k = visited.size
        for i in range(k):
            w = np.where(c == visited[i])
            c = np.delete(c,w)
        q = np.append(q,c)
        
        prev = np.append(prev,q[0])  
        q = np.delete(q,0)
        visited = np.append(visited, c).astype(int)
     
    a = prev.size
    prev = np.flip(prev)
    prev = prev.astype(int)
    print(prev)
  
    g = 0
    while g < a-1:
        b = g + 1
        if G[prev[b], prev[g]] == 1: #If there is an edge between the current vertex in prev and the previous vertex in prev
            prev = prev 
        else:
            prev = np.delete(prev,b)
            g = b - 2
        a = prev.size
        g = g+1
    
    prev = np.flip(prev)
    
    
    
    return prev

    
def DFS(G,t):
    (n,d) = G.shape
    visited = np.array([0])
    out = np.empty((0,n),int)
    for s in range(n):
        st = np.array([s])
        comp = np.array([s])
        while st.size != 0: 
            a = np.where(G[st[-1],:] == 1) 
            a = a[0] 
            q = a.size 
            for i in range(q):
                if i >= a.size:
                    break
                v = np.where(visited == a[i])
                v = v[0]
                if v.size != 0:
                    a = np.delete(a,i)
            q = a.size 
            if q == 0: 
                st = np.delete(st,-1)
                
            else:
                G[st[-1],a[0]] = 0
                st = np.append(st,a[0])
                t = t+1
                visited = np.append(visited,a[0])
                h = np.where(comp == a[0])
                h = h[0]
                if h.size != 0:
                    a = np.delete(a,h)
                comp = np.append(comp,a[0]) 
            if st.size == 0:
                if comp.size == 1:
                    break
                f = comp.size
                w = n - comp.size 
                e = np.zeros(w) 
                comp = np.append(comp,e).astype(int)
                comp = np.array([comp])#comp does not have correct dimestions if I do not do this
                out = np.append(out, comp, axis = 0)
                comp = np.delete(comp,slice(f-1,n))
                
                
    return out
        
