---
layout: post
title: "Laboratorio 5"
description: ""
category: "Laboratorio"
tags: [cicli, funzioni, distanza di Hamming]
---
{% include JB/setup %}
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

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

3. Ripetendo l'esperimento definito al punto 2 per un certo numero k (es: k=10) volte, si stimi distanza di hamming media tra la sequenza originale e la sequenze evolute. Questo rappresenta un punto sul grafico in figura, dove k rappresenta il numero di mutazioni e c la distanza misurata.
  <img src="../../../../python/relation.jpg" alt="Relationship mutation" height="300" width="300">

4. Ripetendo l'esperimento del punto 3 per diversi valori del numero di mutazioni, si stimi l'intero grafico.


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

#%%
# Punto III
num_tests = 10
num_mutations = 100
vect = []
for k in range(num_tests):
    models = [JC69(nuc) for nuc in sequence]
    counter = 0

    while counter <num_mutations:
        for i in range(length):
            evolved = models[i].move()
            counter += evolved
            if counter == num_mutations:
                break
    seq2 = ''.join(model.get_state() for model in models)
    vect.append(sum(ch1!=ch2 for ch1,ch2 in zip(sequence,seq2)))
print sum(vect)/num_tests

#%%

# Punto IV
import  numpy as np

num_tests = 30
total_arr = np.zeros((num_tests,length*5))

for k in range(num_tests):
    print "Evaluating for %d mutations, test n°: %d" %(length*5, k+1)
    models = [JC69(nuc) for nuc in sequence]
    counter = 0
    while counter < length*5:
        for i in range(length):
            evolved = models[i].move()
            counter += evolved
            if counter == length*5:
                break
            if evolved:
                seq2 = ''.join(model.get_state() for model in models)
                total_arr[k,counter] = sum(ch1!=ch2 for ch1,ch2 in zip(sequence,seq2))

import matplotlib.pyplot as plt
plot_gen(total_arr)
```



