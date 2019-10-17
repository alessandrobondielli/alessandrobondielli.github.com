---
layout: post
title: "Laboratorio 1"
description: ""
category: Laboratorio
tags: [liste, tuple, dizionari]
---
{% include JB/setup %}

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
    
#alternativa: formattazione di stringhe
for i,c in enumerate(stringa):
    print 'Lettera {index}: {character}'.format(index=i+1, character=c)

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
    non_divisibile = True
    for k in range(2,n):
        if n%k == 0:
            non_divisibile = False
    if non_divisibile:
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
    print "Nucleotide {nuc}  sconosciuto".format(nuc=nuc)


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
    
### Soluzione:
```python
# Parte I
def complementare(nuc):
    nuc =  nuc.upper()
    nuc_dict = {'A':'T','C':'G','G':'C','T':'A'}
    return nuc_dict[nuc]



# Parte II:
def complementare_eccezione(nuc):
    nuc =  nuc.upper()
    nuc_dict = {'A':'T','C':'G','G':'C','T':'A'}
    
    if nuc not in nuc_dict.keys():
        raise Exception()
    return nuc_dict[nuc]
        

# Programma principale     
nuc = raw_input('Inserire un singolo nucleotide (A, C, G, T): \n')

print complementare(nuc)

try:
    print complementare_eccezione(nuc)
except Exception:
    print "Errore! Qualcosa è andato storto"
```

---
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
    
3. Definire una funzione generatore gen_filamento_opposto(). Il generatore deve produrre il filamento opposto a quello passato come argomento, un nucleotide alla volta.

4. Aggiungere una funzione reverse_complement(), che restituisca il reverse 
  complement del filamento passato come argomento alla funzione:
        
    `>>> reverse_complement('CTAATGT')`\\
    `'ACATTAG'`

5. Modificare il programma in maniera tale da importare il modulo random e 
    usarlo per generare un filamento casuale da dare in pasto alla funzione 
    reverse_complement. Suggerimento: usare la funzione choice() del modulo 
    random che ritorna un elemento casuale tra gli elementi di una 
    sequenza data in ingresso.