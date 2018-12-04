---
layout: post
title: "Laboratorio 7"
description: ""
category: "Laboratorio"
tags: [classi]
---
{% include JB/setup %}
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

## ESERCIZIO XXII

1. Scrivere un programma che definisca una classe MatriceSparsa, che rappresenti una matrice utilizzando un dizionario del tipo `(i,j): value`.

2. Definire il metodo `__init__()` in modo che la matrice sia inizializzata come una matrice 1x1 contenente il valore 1.

3. Definire un metodo `inserisci(i,j,value)` che inserisce il valore `value` alla riga `i`, colonna `j` della matrice. 

4. Definire un metodo `stampa()`, che stampi la matrice. N.B.: Per valori mancanti in posizione `(i,j)` il metodo stampa 0.

`>>> mat = MatriceSparsa()`\\
`>>> mat.stampa()`\\
`1`\\
`>>> mat.inserisci(2,2,5)`\\
`>>> mat.stampa()`\\
`0 0 0`\\
`0 0 0`\\
`0 0 9`\\
`>>> mat.inserisci(0,2,12)`\\
`>>> mat.stampa()`\\
`0 0 12`\\
`0 0 0`\\
`0 0 5`\\
`>>> mat.inserisci(0,6,99)`\\
`>>> mat.stampa()`\\
`0 0 12 0 0 0 99`\\
`0 0 0 0 0 0 0`\\
`0 0 5 0 0 0 0`


### Soluzione

```python
class MatriceSparsa(object):
    def __init__(self):
        self.rows = 1
        self.cols = 1
        self.values = {(0 ,0): 1}

    def inserisci(self, i ,j ,value ):
        self.rows = max(self.rows, i+1)
        self.cols = max(self.cols, j+1)
        self.values[(i,j)] = value
        
    def stampa(self):
        for i in xrange(self.rows):
            for j in xrange(self.cols):
                if (i,j) in self.values : # se la cella (i,j) e’ non nulla
                    print '%3i' % self.values[(i,j)],
                else:
                    print '%3i' % 0,
            print
            
mat = MatriceSparsa()
mat.stampa()

mat.inserisci(2 ,2 ,9)
mat.stampa()

mat.inserisci(2 ,0 ,45)
mat.stampa()

mat.inserisci(0 ,6 ,99)
mat.stampa()
```

---
## ESERCIZIO XXIII

Dato un file .html fornito, <a href="/python/baby1993.html" download>`"baby1993.html"`</a>, contenente i nomi più popolari per i bambini nati nel 1990 negli USA, si scriva una funzione
`estrai_nomi()` che prenda in ingresso il nome del file e ne faccia il parsing, restituendo una lista contenente l'anno come primo elemento
seguito dalle stringhe nome-rank in ordine alfabetico `['1990', 'Aaron 34', 'Abbey 482', 'Abbie 685', ... ]`.

Si faccia uso della particolare struttura di questo file html:

```html
...
<h3 align="center">Popularity in 1993</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
```

### Soluzione

```python
import re

def estrai_nomi(filename):
    """
    """
    pattern = r"<td>([\d]{1,})</td><td>([\w]{1,})</td><td>([\w]{1,})</td>"
    year_pattern = r"""<h3 align="center">Popularity in ([\d]{4})</h3>"""
    lista_nomi = []
    infile = open(filename)
    htmlPage = ''.join(line for line in infile)
    matches = re.finditer(pattern,htmlPage)
    for match in matches:
        lista_nomi.append(match.group(2)+' '+match.group(1))
        lista_nomi.append(match.group(3)+' '+match.group(1))
    lista_nomi.sort()
    match_year = re.search(year_pattern,htmlPage)
    year = match_year.group(1)
    return [year]+lista_nomi


print estrai_nomi("files/baby1993.html")[0:20]
```

---
## ESERCIZIO XXIV

1. Scrivere una funzione `conta_caratteri(s)` che ritorni un dizionario contenente il numero di occorrenze
    per ciascun carattere presente nella stringa s:\\
    `>>> conta_caratteri('peptide') {'i': 1, 'p': 2, 'e': 2, 't': 1, 'd': 1}`\\
    Facoltativo: risolvere l’esercizio utilizzando i costrutti per il controllo delle eccezioni.
2. Utilizzare la funzione `conta_caratteri` per contare il numero di occorrenze per amminoacidi
    nella proteina [P51787](http://www.uniprot.org/uniprot/P51787.fasta).

<!---
### Soluzione

```python
# Punto 1
def conta_caratteri(stringa):
    if type(stringa) != str:
        raise TypeError('Input type must be string')

    char_dict = {}
    for char in stringa:
        try:
            char_dict[char] += 1
        except KeyError:
            char_dict[char] = 1

    return char_dict

# Punto 2
sequenza = ""
with open("files/P51787.fasta") as fopen:
    for line in fopen:
        if not line.startswith('>'):
            sequenza += line.replace('\n','')

dict_ammino =  conta_caratteri(sequenza)
print dict_ammino

```
--->
