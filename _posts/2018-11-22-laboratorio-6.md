---
layout: post
title: "Laboratorio 6"
description: ""
category: "Laboratorio"
tags: [classi]
---
{% include JB/setup %}
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>


## ESERCIZIO XIX

Scrivere un programma che:

1. Definisca una classe `Punto2D`, che rappresenti un punto del piano.
2. Definisca il metodo `distanza_origine()` della classe `Punto2D`. Il metodo deve restituire la distanza del punto dall’origine degli assi.


### Soluzione

```python
import math

class Punto2D(object):
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def distanza_origine(self):
        return math.sqrt(self.x**2 + self.y**2)

            
p = Punto2D(2.5,3.1)
print p.distanza_origine()
print p

```
---
## ESERCIZIO XX

Scrivere un programma che:


1. Definisca una classe `Dado`, che rappresenti un dado. La classe deve avere un metodo `lancia()`, che stampi un numero da 1 a 6 con probabilità uniforme. Utilizare il metodo `random.choice()`.
2. Definsca una classe `DadoTruccato` derivata da `Dado`. Ridefinisca il metodo `lancia()`, che simuli il lancio di un dado in cui la probabilità che esca 6 sia doppia rispetto agli altri numeri. Si usi la funzione `random.random()` .


### Soluzione

```python
import random

# Parte I

class Dado(object):
    dado = [1,2,3,4,5,6]

    def lancia(self):
        print random.choice(self.dado)

d = Dado()
d.lancia()

# Parte II

class DadoTruccato(Dado):
    
    def lancia(self):    
        base_prob = 1.0/7
        prob = random.random();
        if prob < base_prob:
            return 1
        elif base_prob <= prob < 2 * base_prob:
            return 2
        elif 2* base_prob <= prob < 3 * base_prob:
            return 3
        elif 3* base_prob <= prob < 4 * base_prob:
            return 4
        elif 4* base_prob <= prob < 5 * base_prob:
            return 5
        else:
            return 6
            
d_t = DadoTruccato()
print d_t.lancia()
```


---
## ESERCIZIO XXI

Scrivere un programma che:
1. Definisca una classe DNA che rappresenti una sequenza di DNA tramite una stringa di caratteri scelti tra `{C, G, A, T}`.
2. Definisca il metodo `stampa()` della classe `DNA`, che stampi a video la sequenza di `DNA`.
3. Definisca il metodo `complementare()` della classe `DNA`, che restituisca la sequenza complementare come un nuovo oggetto `DNA`.


### Soluzione

```python
class DNA(object):
    BASE_COMPL = {'C': 'G', 'G': 'C', 'A': 'T', 'T': 'A'}

    def __init__(self , s):
        self.s = s.upper()
    #Punto II
    def stampa(self):
        print self.s
    #Punto III
    def complementare(self):        
        return DNA(''. join (DNA.BASE_COMPL[b] for b in self.s))
        
    
        
d = DNA("ACG")
c = d.complementare()

d.stampa()
c.stampa()
```

