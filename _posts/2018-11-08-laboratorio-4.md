---
layout: post
title: "Laboratorio 4"
description: ""
category: "Laboratorio"
tags: [cicli, funzioni, distanza di Hamming]
---
{% include JB/setup %}
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
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

## ESERCIZIO XVI
Funzioni ricorsive

1. Scrivere un programma che calcoli il fattoriale di un numero dato in input dall’utente.
    Il programma dovra fare uso di **funzioni ricorsive**.
2. Scrivere una funzione ricorsiva che calcoli la somma degli elementi di un vettore dato in ingresso.

### Soluzione

```python
# Punto 1
def fattoriale(n):
    if n == 1 or n == 0:
        return 1
    return n * fattoriale(n-1)

num = int(raw_input("scegli un numero di cui calcolare il fattoriale:"))

print fattoriale(num)

# Punto 2
def somma(vect):
    if len(vect) == 1:
        return vect[0]
    return vect[0] + somma(vect[1:])
```

## ESERCIZIO XVII

Si consideri un modello di evoluzione della sequenza del DNA basato su catene di Markov. Si faccia riferimento al modello definito da Jukes e Cantor, come mostrato in figura (si ricordi che per JK $$\alpha=\beta$$). [Wikipedia](https://en.wikipedia.org/wiki/Models_of_DNA_evolution#JC69_model_.28Jukes_and_Cantor.2C_1969.29.5B2.5D), [Libro](https://books.google.it/books?hl=it&lr=&id=FDHLBAAAQBAJ&oi=fnd&pg=PA21&dq=+Evolution+of+Protein+Molecules+jukes&ots=blcjZGR_lA&sig=nN-B81QAXDARET-ht5TrTM2qDlo#v=onepage&q=Evolution%20of%20Protein%20Molecules%20jukes&f=false).
<img src="../../../../python/kimura.jpg" alt="Kimura model" height="300" width="300">

 Codice fornito [MarkovChain.py](../../../../python/MarkovChain.py).

 Alcuni esempi:

```python
>>> nuc_mc = JC69('A')
<__main__.MarkovChain instance at 0x1a22066638>
...                         
>>> nuc_mc.get_state()
'A'
>>> nuc_mc.move()
'True'
>>> nuc_mc.get_state()
'C'
```

Utilizzado il codice fornito si:

1. Generi una sequenza casuale di lunghezza 100 nucleotidi; si generi un modello di Jukes e Cantor per ogni nucleotide, e si faccia evolvere la sequenza per 100 **passi**. Si stampi a video la distanza di hamming tra la sequenza originale e la sequenza evoluta.

2. Generi una sequenza casuale di lunghezza 100 nucleotidi; si generi un modello di Jukes e Cantor per ogni nucleotide, e si faccia evolvere la sequenza per 100 **mutazioni**. Si stampi a video la distanza di hamming tra la sequenza originale e la sequenza evoluta.


### Soluzione

```python
# Punto I
length = 100
sequence = ''.join(random.choice(list('ACGT')) for k in range(length))
print sequence
models = [JC69(nuc) for nuc in sequence]

num_it = 100
for it in range(num_it):
    for i in range(length):
        models[i].move()
seq2 = ''.join(model.get_state() for model in models)
print sum(ch1!=ch2 for ch1,ch2 in zip(sequence,seq2))
```
<!--
#%%
# Punto II
models = [JC69(nuc) for nuc in sequence]

counter = 0
num_mutations = 100

while counter <num_mutations:
    for i in range(length):
        counter += models[i].move()
        if counter == num_mutations:
            break

seq2 = ''.join(model.get_state() for model in models)
print sum(ch1!=ch2 for ch1,ch2 in zip(sequence,seq2))
-->

