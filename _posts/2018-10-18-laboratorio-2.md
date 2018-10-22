---
layout: post
title: "Laboratorio 2"
description: ""
category: "Laboratorio"
tags: [funzioni, operatori condizionali]
---
{% include JB/setup %}


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

# Punto I:

def complementare(nuc):
    if nuc == 'A':
        return 'T'
    elif nuc == 'C':
        return 'G'
    elif nuc == 'G':
        return 'C'
    elif nuc == 'T':
        return 'A'

nuc = raw_input('Inserire un singolo nucleotide (A, C, G, T): \n')

compl = complementare(nuc)

print compl

# Punto II:

def complementare_con_eccezione(nuc):
    
    if nuc == 'A':
        return 'T'
    elif nuc == 'C':
        return 'G'
    elif nuc == 'G':
        return 'C'
    elif nuc == 'T':
        return 'A'
    else:
        raise Exception('Wrong nucletide!')

nuc = raw_input('Inserire un singolo nucleotide (A, C, G, T): \n')

try:
    compl = complementare_con_eccezione(nuc)
    print compl
except Exception:
    print "Errore, nucleotide inserito non valido"
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

3. Aggiungere una funzione reverse_complement(), che restituisca il reverse 
  complement del filamento passato come argomento alla funzione:
        
    `>>> reverse_complement('CTAATGT')`\\
    `'ACATTAG'`
    

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

... 

```