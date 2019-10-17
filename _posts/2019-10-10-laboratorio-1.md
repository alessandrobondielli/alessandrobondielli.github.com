---
layout: post
title: "Laboratorio 1"
description: ""
category: Laboratorio
tags: [liste, tuple, dizionari]
---
{% include JB/setup %}

## ESERCIZIO I

Utilizzando la console interattiva:

1. Creare due **tuple** che rappresentino i seguenti elenchi di amminoacidi e sigle:

    `amminoacidi: Alanina, Glicina, Lisina`\\
    `sigle: Ala, Gly, Lys`

2. Ottenere da esse una **lista** in cui ogni elemento è un **dizionario** che
    rappresenta un amminoacido e sigla (Alanina Ala, Glicina Gly etc.).
    Amminoacidi e sigle vanno accoppiati in base all’ordine con cui sono elencati.
    In ogni dizionario, gli amminoacidi devono essere rappresentati tramite la
    chiave "nome" e le sigle tramite la chiave "sigla".


### Soluzione:
```python
amminoacidi = ('Alanina', 'Glicina', 'Lisina')
sigle = ('Ala', 'Gly', 'Lys')

# alternativa I - Utilizzo di List comprehension:

l = [{'nome': amminoacido,'sigla': sigla} for amminoacido, sigla in
             zip(amminoacidi, sigle)]

# alternativa II:

l = []
for amminoacido, sigla in zip(amminoacidi, sigle):
        l.append({'nome':amminoacido, 'sigla': sigla})
```

---
## ESERCIZIO II

Utilizzando la console interattiva:
1. Creare un dizionario che contenga come chiavi nome e cognome, inserendo i
    propri dati come valori.
2. Aggiungere matricola.
3. Aggiungere esami, provando ad immaginare che tipi di dato usare per
    rappresentare sia nome che voto degli esami.


### Soluzione:
```python
d = {'nome':'Pinco', 'cognome': 'Pallino'}

d['matricola'] = 258115

# alternativa I:

d['esami'] = [{'nome':'Bioinformatica','voto': 30},
        {'nome':'Analisi','voto': 18}]

# alternativa II:

d['esami'] = {'Bioinformatica': 30, 'Analisi': 18}
```

---
## ESERCIZIO III

Scrivere un programma che:
1. Crei una lista di coppie (stringa, intero), utilizzando tuple. Ad esempio:
    `('hello', 3), ('world', 2), ('!', 1).`

2. Per ogni elemento della lista, stampi la stringa ripetuta un numero di volte
    pari al valore dell'intero.

3. Ripetere l'esercizio utilizzando dizionari al posto di tuple
    (usare le seguenti chiavi: parola, volte).

### Soluzione:
```python
l = [('hello', 3), ('world', 2), ('!', 1)]


for t in l:
    for i in range(t[1]):
        print t[0]

l = [{'parola': 'hello', 'volte': 3}, {'parola': 'world', 'volte':2}, {'parola': '!', 'volte': 1}]

for d in l:
    for i in range(d['volte']):
        print d['parola']
```

---

## ESERCIZIO IV

Calcolare la somma dei primi 500 numeri naturali (da 0 incluso a 500 escluso).

### Soluzione:
```python
# alternativa I:
n = 0
for k in xrange(0,500):
    n += k

#alternativa II:
n = sum(xrange(0,500))

#alternativa III:
n =  (499*500)/2

#alternativa IV
n = reduce(lambda x,y: x+y, xrange(500))
```

---
<!---
## ESERCIZIO V

1. Scrivere un programma che, data la stringa 'abcdefghi', la analizzi e
    stampi a video:

    `Lettera 1: a`\\
    `Lettera 2: b`\\
    `...`

2. Modificare poi il programma in modo da leggere la stringa da tastiera.


### Soluzione:
```python
stringa = 'abcdefghi'
for i,c in enumerate(stringa):
    print 'Lettera %d: %s' %(i+1, c)

stringa = raw_input('Inserisci una stringa: ')
for i,c in enumerate(stringa):
    print 'Lettera %d: %s' %(i+1, c)
```

---

## ESERCIZIO VI

Scrivere un programma che stampi la lunghezza di una stringa fornita dall'utente,
e ripeta questo processo finchè l'utente non inserisce la stringa 'exit'.

### Soluzione:
```python
while True:
    stringa = raw_input('Inserisci una stringa: \n')
    if stringa == 'exit':
        break
    print len(stringa)
```

---
## ESERCIZIO VII

Scrivere un programma che prenda in ingresso un intero e stampi tutti i numeri
primi fino al numero fornito dall’utente.

### Soluzione:

```python
num = raw_input('Inserire un numero: \n')

n = 2
while n < int(num):
    cond = True
    for k in range(2,n):
        if n%k == 0:
            cond = False
    if cond:
        print n
    n += 1
```

---
## ESERCIZIO VIII
Scrivere un programma che:

1. Prenda una stringa in input da tastiera, rappresentante un singolo nucleotide \\
    `(A, C, G oppure T)`.

2. Stampi a video una stringa rappresentante il nucleotide complementare.

Assicurarsi che il programma funzioni correttamente sia con input maiuscolo 
    che minuscolo.
    
### Soluzione:
```python
nuc = raw_input('Inserire un singolo nucleotide (A, C, G, T): \n')

nuc =  nuc.upper()

# Alternativa I:

if nuc == 'A':
    print 'T'
elif nuc == 'C':
    print 'G'
elif nuc == 'G':
    print 'C'
elif nuc == 'T':
    print 'A'
else:
    print "Nucleotide %s sconosciuto" %s


# Alternativa II:

nuc_dict = {'A':'T','C':'G','G':'C','T':'A'}

print nuc_dict[nuc]


```

---
## ESERCIZIO IX
1. Riprendere l'esercizio 8, e risolverlo definendo una funzione complementare(), 
    che ritorni il nucleotide complementare a quello passato come argomento:

```python
>>> complementare ('C')
'G'
```
        
2. Modificare l'esercizio in modo da gestire il caso in cui sia inserito un 
    nucleotide non valido tramite l'uso delle eccezioni. In particolare si 
    modifichi la funzione complementare in modo da lanciare un eccezione 
    generica Exception in caso di nucleotide non valido. Tale eccezione deve 
    essere catturata e gestita dal programma principale tramite la stampa a 
    video di un messaggio di errore.
    
-->
