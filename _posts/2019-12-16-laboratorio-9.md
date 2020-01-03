---
layout: post
title: "Laboratorio 9"
description: ""
category: "Laboratorio"
tags: [classi]
---
{% include JB/setup %}
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

## ESERCIZIO XXVI

Si consideri un albero binario (di ricerca, o BST) costruito in Python utilizzando istanze della seguente classe:

```python
class TNode:
   def __init__(self, data=None, left=None, right=None):
      self.data=data
      self.left=left
      self.right=right
```
1. Si aggiunga un metodo a TNode che, data in input una lista ordinata di interi (ordinamento crescente), costruisca un albero di
    profondità  minima.

2. Si aggiunga un metodo a TNode che stampi a video i contenuti dei nodi in accordo a una visita in profondità
  con ordinamento simmetrico (ovvero depth-first, in-order).

3. Si aggiunga un metodo a TNode che restituisca una lista con i contenuti dei nodi ottenuti in accordo a una visita
    in profondità con ordinamento simmetrico (ovvero depth-first, in-order).


### Soluzione

```python
class TNode:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

# Punto 1    
    @staticmethod   
    def buildTree(intList):
        if not intList:
            return
        if len(intList) == 1:
            return TNode(data=intList[0])
        else:
            midPoint = len(intList)/2
            return TNode(data=intList[midPoint], left = TNode.buildTree(intList[:midPoint]),
                         right = TNode.buildTree(intList[midPoint+1:]))

# Punto 2
    def printTree(self):
        if self.left:
            self.left.printTree()
        print self.data,
        if self.right:
            self.right.printTree()
# Punto 3
    def treeToList(self, outlist=None):
        if not outlist:
            outlist = []
        if self.left:
            self.left.treeToList(outlist)
        outlist.append(self.data)
        if self.right:
            self.right.treeToList(outlist)
        return outlist

lista_nodi = [4,10,12,15,18,22,24,25,31,35,44,50,66,70,90]
myTree = TNode.buildTree(lista_nodi)

myTree.printTree()
print myTree.treeToList()
```

---
## ESERCIZIO XXVII

1. Si scriva un programma che simuli un [random walk 2-D](http://mathworld.wolfram.com/RandomWalk2-Dimensional.html), per un numero di passi di lunghezza
    unitaria `n` dato in ingresso. Si rappresenti la traiettoria con `matplotlib`.
2. Si determini la distanza quadratica media dall'origine dopo `k` step, utilizzando `m = 2000` traiettorie.

Analiticamente è facile ricavare che, data la posizione nel piano dopo $$k$$ step, \\
$$ z = \sum_{j=1}^{k} e^{i\theta_j}$$ \\
la media della distanza $$ |z|^2$$ sia uguale a : \\
$$\langle |z|^2 \rangle = k $$


### Soluzione

```python
import numpy as np

def random_walk(path_len=100, num_path=2000):

    allpath = np.empty((num_path,path_len),dtype=complex)

    for i in xrange(num_path):
        for j in xrange(path_len):
            teta = random.uniform(0,2*np.pi)
            allpath[i,j] = complex(np.cos(teta), np.sin(teta))

    allpath = np.cumsum(allpath, axis=1)
    return allpath

# Punto 1
path = random_walk(path_len=200,num_path=1)
x = np.real(path[0])
y = np.imag(path[0])
plt.plot(x,y,linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Random Walk, 2D')

# Punto 2
path = random_walk(path_len=200,num_path=2000)
abspath = np.abs(path)**2
plt.figure()
plt.plot(xrange(path.shape[1]),np.mean(abspath,axis=0),linewidth=2)
plt.grid()
plt.xlabel('Step')
plt.ylabel('Mean square distance')
plt.title('Random Walk, 2D')
```

