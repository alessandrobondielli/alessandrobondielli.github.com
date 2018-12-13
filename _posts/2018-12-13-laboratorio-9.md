---
layout: post
title: "Laboratorio 9"
description: ""
category: "Laboratorio"
tags: [classi]
---
{% include JB/setup %}
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

## ESERCITAZIONE XXVII

1. Si scriva un programma che simuli un [random walk 2-D](http://mathworld.wolfram.com/RandomWalk2-Dimensional.html), per un numero di passi di lunghezza
    unitaria `n` dato in ingresso. Si rappresenti la traiettoria con `matplotlib`.
2. Si determini la distanza quadratica media dall'origine dopo `k` step, utilizzando `m = 2000` traiettorie.

Analiticamente è facile ricavare che, data la posizione nel piano dopo $$k$$ step, \\
$$ z = \sum_{j=1}^{k} e^{i\theta_j}$$ \\
la media della distanza $$ |z|^2$$ sia uguale a : \\
$$\langle |z|^2 \rangle = k $$

<!---
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
--->
