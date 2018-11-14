---
layout: post
title: "Laboratorio 3"
description: ""
category: "Laboratorio"
tags: [cicli, funzioni, distanza di Hamming]
---
{% include JB/setup %}
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

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

---
## ESERCIZIO XII
Scrivere un programma in grado di generare un triangolo di Tartaglia di altezza `n`, dove `n` è  un intero inserito da tastiera. 
Ad esempio, per `n = 5` si avrà:

```
1
1   1
1   2   1
1   3   3   1
1   4   6   4   1
```
### Soluzione
```python

# Alternativa con indici:
def tartaglia_indici(n):
    triangolo = []
    triangolo.append([0]*n)    
    triangolo[0][0] = 1
    

    for i in range(1,n):
        
        triangolo.append([0]*n)    
        triangolo[i][0] = 1
        
        for c in range(1,n):

            triangolo[i][c]= triangolo[i-1][c-1]+triangolo[i-1][c]
        
    return triangolo

# Alternativa con zip
def tartaglia_zip(n):
    triangolo = []
    #inserisco il vertice del triangolo
    triangolo.append([1])
    for k in range(1, n):
        
        riga = [sum(k) for k in zip([0]+triangolo[-1], triangolo[-1]+[0])]

        triangolo.append(riga)

    return triangolo


def stampa_tartaglia(triangolo):
    """
    Parametro triangolo: list of lists [[], [], [], ...]
    
    """

    n_len = len(triangolo)
    print n_len
    #iterazione sulle righe del tirangolo (i.e. le liste)
    for i, line in enumerate(triangolo):
        print " "*(n_len-i)*3,

        #iterazione su ciascuna colonna
        for col in range(0, i+1):
            print "%5d" %triangolo[i][col],
        print 



print tartaglia_zip(5)
stampa_tartaglia(tartaglia_zip(5))

```

---
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

# Punto III ???

```


# Punto III
```python
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

