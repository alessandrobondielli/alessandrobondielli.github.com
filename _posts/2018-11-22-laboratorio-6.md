---
layout: post
title: "Laboratorio 6"
description: ""
category: "Laboratorio"
tags: [classi]
---
{% include JB/setup %}
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

## ESERCIZIO XVIII
Scrivere un programma che:

1. Dati due vettori, crei la matrice del prodotto $$V_1 * V_2^T$$. 
    Ideare una struttura dati appropriata per implementare la matrice.

    $$V_1 = \begin{pmatrix}1\\ 2\\ 3\\ 4\\ 5 \end{pmatrix} \quad V_2 = \begin{pmatrix} 6\\ 7\\ 8\\ 9\\ 10 \end{pmatrix}$$

2. Completare il programma con una stampa della matrice riga per riga: \\
    `[6, 7, 8 ... ]`\\
    `[12 , 14, 16 ... ]`\\
    `...`
2. Aggiungere una funzione stampa_matrice(mat), che migliori la stampa:\\
    `stampa_matrice(mat)`\\
    `6 7 8 9 10`\\
    `12 14 16 18 20`\\
    `18 21 24 27 30`\\
    `...`\\
Per fare in modo che i numeri siano stampati allineati, usare per ogni numero il costrutto di string formatting come riportato:\\
`print '%3i' % num`

<!---
### Soluzione

```python
v1 = [1,2,3,4,5]
v2 = [6,7,8,9,10]

mat = []
for x1 in v1:
    row = []
    for x2 in v2:
        row.append(x1*x2)
    mat.append(row)
    
#Alternativa con list comprension
mat = [[x1*x2 for x2 in v2] for x1 in v1]

#Punto 2
for row in mat:
    print row
    
#Punto 3
def stampa_matrice(mat):
    for row in mat:
        for el in row:
            print '%3i' %el,
        print

stampa_matrice(mat)
```
-->

---
## ESERCIZIO XIX

Scrivere un programma che:

1. Definisca una classe `Punto2D`, che rappresenti un punto del piano.
2. Definisca il metodo `distanza_origine()` della classe `Punto2D`. Il metodo deve restituire la distanza del punto dall’origine degli assi.

<!--
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
-->
---
## ESERCIZIO XX

Scrivere un programma che:


1. Definisca una classe `Dado`, che rappresenti un dado. La classe deve avere un metodo `lancia()`, che stampi un numero da 1 a 6 con probabilità uniforme. Utilizare il metodo `random.choice()`.
2. Definsca una classe `DadoTruccato` derivata da `Dado`. Ridefinisca il metodo `lancia()`, che simuli il lancio di un dado in cui la probabilità che esca 6 sia doppia rispetto agli altri numeri. Si usi la funzione `random.random()` .

<!--
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
-->

---
## ESERCIZIO XXI

Scrivere un programma che:
1. Definisca una classe DNA che rappresenti una sequenza di DNA tramite una stringa di caratteri scelti tra `{C, G, A, T}`.
2. Definisca il metodo `stampa()` della classe `DNA`, che stampi a video la sequenza di `DNA`.
3. Definisca il metodo `complementare()` della classe `DNA`, che restituisca la sequenza complementare come un nuovo oggetto `DNA`.

<!---
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
-->

---
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

<!---
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
--->
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
<!---
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
-->

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
