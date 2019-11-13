---
layout: post
title: "Laboratorio 5"
description: ""
category: "Laboratorio"
tags: [cicli, funzioni, distanza di Hamming]
---
{% include JB/setup %}
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

## ESERCIZIO XIII
1. Scrivere un programma che definisca la funzione `dh(s,t)`, 
    che implementi il calcolo della [distanza di Hamming](https://en.wikipedia.org/wiki/Hamming_distance) tra due stringhe s e t.

2. Aggiungere la funzione `dhplus(s,t)`, che generalizzi `dh(s,t)` al caso di stringhe di 
    diversa lunghezza. Visto che molte generalizzazioni della distanza di Hamming sono 
    possibili e’ richiesta l’implementazione di questo primo modo: estendere la stringa 
    di lunghezza minore con una serie di caratteri non validi (ad esempio ’-’) in modo 
    da ottenere stringhe di lunghezza uguale.

    
3. Aggiungere una funzione `dhplus2(s,t)` che implementa un modo diverso per generalizzare 
    la distanza di Hamming: prolungare le due stringhe con caratteri non validi fino ad 
    una lunghezza pari alla somma delle due, iterare sulla lunghezza delle stringhe prolungate 
    ogni volta ruotando una stringa spostando un carattere dal fondo alla testa e calcolare 
    la distanza di Hamming, ritornare come valore della distanza di Hamming il minimo valore 
    tra quelli calcolati.

    `prova.......`\\
    `.....provola`\\
    `prova.......`\\
    `a.....provol`\\
    `prova.......`\\
    `la.....provo`\\
    `prova.......`\\
    `ola.....prov`

### Soluzione

```python
# Punto I:
def dh(s,t):
    if len(s) != len(t):
        return -1        
    ones = [ es != et for es, et in zip(s,t) ]
    return sum(ones)    
    
s1 = 'prova'
s2 = 'privo'
print dh(s1,s2)

# Punto II

def dhplus(s,t):
    max_len = max(len(s), len(t))
    s_prime = s + '-'*(max_len - len(s))
    t_prime = t + '-'*(max_len - len(t))
    
    return dh(s_prime, t_prime)
    
s3 = 'prova'
s4 = 'provola'

print dhplus(s3,s4)

# Punto III 

def dhplus1(s,t):
    lun =len(s) + len(t)
    sprime = s + '-'*(lun - len(s))
    tprime = '-'*(lun - len(t)) + t
    
    dist = lun
    for x in xrange(lun):
        sprime = sprime[-1] + sprime[:-1]
        tmp = dh(sprime, tprime)
        dist = min(dist, tmp)
    
    return dist
    
print dhplus1(s3,s4)
```


## ESERCIZIO XIV

Scrivere un programma che:

1. Utilizza la list comprehension per creare la lista dei primi dieci cubi:\\
    `[0,1,8,27 ... ]`
2. Utilizza la funzione `filter` per ottenere una nuova lista con solo
numeri pari.
3. Utilizza la funzione `map` per ottenere una nuova lista che
contenga gli elementi della precedente moltiplicati per 3.
4. Utilizza lo _slice_ operator per ottenere una nuova lista senza il
primo elemento.
5. Utilizza la funzione `reduce` per ottenere il prodotto degli elementi.

### Soluzione

```python
# Punto 1
lista = [ x**3 for x in xrange(10) ]

# Punto 2
lista2 = filter( lambda el: not el%2, lista )

# Punto 3
lista3 = map(lambda x: x*3, lista2)

# Punto 4
lista4 = lista3[1:]

# Punto 5
prodotto = reduce(lambda x,y: x*y, lista4)
```

## ESERCIZIO XV

Scrivere un programma che:

1. Crei una stringa ripetendo 10,000 volte la stringa "CGAT".

2. Crei una stringa di 40,000 caratteri scelti a caso dall'alfabeto $$\mathcal{A} = \{`A',`C',`G',`T'\}$$

3. Utilizzi la funzione `compress()` del modulo `zlib` ([documentazione](https://docs.python.org/2/library/zlib.html)) per comprimere ciascuna delle due stringhe.
    Infine si calcoli le lunghezze delle nuove stringhe così ottenute ed i relativi rapporti di compressione.

### Soluzione

```python
import random
import zlib

s1 = 'CGAT' * 10000
s2 = ''.join([random.choice('CGAT') for i in xrange(40000)])

zs1 = zlib.compress(s1)
zs2 = zlib.compress(s2)

print len(zs1)/float(len(s1))
print len(zs2)/float(len(s2))
```

