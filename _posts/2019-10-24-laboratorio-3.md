---
layout: post
title: "Laboratorio 3"
description: ""
category: "Laboratorio"
tags: [cicli, funzioni, distanza di Hamming]
---
{% include JB/setup %}
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

## ESERCIZIO X

1. Modificare ulteriormente il programma dell'esercizio 9 (punto I) in modo da 
    aggiungere una funzione filamento_opposto(), che utilizzi la funzione 
    complementare() per restituire il filamento opposto a quello 
    passato come argomento:

    `>>> filamento_opposto('CTAATGT ')`\\
    `'GATTACA '`

2. Modificare la soluzione in modo da usare la funzione map al posto della 
    funzione filamento_opposto() definita al punto precedente. 
    La funzione complementare potra' essere sfruttata dalla funzione map.

3. Aggiungere una funzione reverse_complement(), che restituisca il reverse 
  complement del filamento passato come argomento alla funzione:
        
    `>>> reverse_complement('CTAATGT')`\\
    `'ACATTAG'`

4. Modificare il programma in maniera tale da importare il modulo random e 
    usarlo per generare un filamento casuale da dare in pasto alla funzione 
    reverse_complement. Si consiglia di usare la funzione choice() del modulo 
    random che ritorna un elemento casuale tra gli elementi di una 
    sequenza data in ingresso.


### Soluzione:

```python

# Punto I:

def filamento_opposto(filamento):
    sequenza_opposta = [complementare(c) for c in filamento]
    return ''.join(sequenza_opposta)

# Punto II:
filamento_opposto_list = map(complementare, filamento)

filamento_opposto = ''.join(filamento_opposto_list)


# Punto III:

def reverse_complement(filamento):
    # Ottenere il reverse del filamento
    rev_f = filamento[::-1] 
    return filamento_opposto(rev_f)
    
print reverse_complement('CTAATGT')

# Punto IV:

import random

filamento = ''
#genero un filamento di lunghezza 10

#opzione I : ciclo for
for i in range(10):
    filamento = filamento + random.choice('CGAT')
print filamento

# opzione II: list comprehension
filamento = ''.join([random.choice('CGAT') for i in xrange(10)])
print filamento

print filamento_opposto(filamento)
print reverse_complement(filamento)


... 

```

---
## ESERCIZIO XI
Scrivere un programma che legga un intero `righe` e un intero
`colonne` da tastiera e stampi a schermo:

`X X X X X`\\
`X X X X X`\\
`X X X X X`

L’esempio riporta l’output richiesto per `righe = 3` e `colonne = 5`. 
Per andare a capo, dare l’istruzione print senza argomenti: `print`. \\
Per stampare senza andare a capo, aggiungere una virgola in fondo alla 
riga con l’istruzione `print`. 
Es: `print "ciao",`

### Soluzione
```python
# Leggo due interi da tastiera
righe = int(raw_input("righe:"))
colonne = int(raw_input("colonne:"))

# Soluzione I:
for i in range(0, righe):     
    for j in range(0, colonne):
        print 'X ',
    print 

# Soluzione II, con complessità inferiore:

stringa = ''
# Alternativa con ciclo for:
for j in range(0, colonne):
    stringa += 'X  '

# Alternativa usando list comprehension:
stringa = " ".join(["X " for x in xrange(colonne)])

for i in range(0, righe):     
    print stringa


```

