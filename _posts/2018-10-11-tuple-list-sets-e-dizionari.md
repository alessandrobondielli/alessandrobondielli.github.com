---
layout: post
title: "Tuple, Liste, Sets e Dizionari"
description: ""
category: Tutorial
tags: []
---
{% include JB/setup %}

#### Liste
Le **liste** rappresentano il tipo composto più versatile tra quelli disponibili in Python.
Una lista viene rappresentata come un insieme di valori separati da virgola
, _non necessariamente del medesimo tipo_, incapsulati tra parantesi quadre.

```python
>>> primes = [1, 2, 3, 5, 7, 11]
>>> primes
[1, 2, 3, 5, 7, 11]
```

Le liste possono essere indicizzate (gli indici iniziano da zero, **zero-based indexing**) e scorse:

```python
>>> primes[3]
5
```

```python
>>> primes[1:3]
[2, 3]
```

Le liste sono tipi **mutabili**, i.e. il loro contenuto può essere variato, sia singolarmente che tramite _slicing_:

```python
>>> primes = [1, 2, 3, 5, 9, 11]
>>> primes[4] = 7
>>> primes
[1, 2, 3, 5, 7, 11]
```

#### Tuple
Una **tupla** viene rappresentata come una lista di elementi, separati da virgola, eventualmente incapsulati
in parentesi tonde. Vengono usualmente utilizzate per rappresentare insiemi eterogenei di valori
e sono **immutabili**.

```python
>>> t =  (12345, 'ciao', 3452)
>>> t[0]
12345
# IMMUTABLE
>>> t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

#### Sets
Python implementa nativamente un tipo *Set*. I sets sono collezioni di elementi, non ordinate, e prive
di duplicati. Il tipo set implementa una serie di operazioni matematiche tipiche dell'insiemistica,
come unione, intersezione, differenza e differenza simmetrica. Un set viene creato attraverso il
costruttore `set()` od attraverso l'utilizzo di parentesi graffe `{,}`.

```python
>>> primes = set([1, 2, 3, 5, 7, 11])
>>> even = set([1, 3, 5, 7, 9, 11])
>>> even - primes
set([9])
>>> even | primes   # OR
set([1, 2, 3, 5, 7, 9, 11])
>>> even & primes   # AND
set([1, 3, 5, 7, 11])
```

#### Dizionari
Un *dizionario* è un array associativo. Rappresenta un insieme di elementi, indicizzati da chiavi(*keys*),
le quali possono essere di qualsiasi tipo immutabile. Una tupla può essere usata come chiave se non contiene,
direttamente od indirettamente, alcun elemento di tipo mutabile. Il metodo `keys()` di un oggetto dizionario
restituisce una lista di chiavi, in ordine aribitrario.
I dizionari sono di tipo mutabile.

```python
>>> name_year = {'The Doors': 1967, 'Fun House': 1970}
>>> name_year['In The Court Of The Crimson King'] = 1969
>>> name_year
{'Fun House': 1970, 'In The Court Of The Crimson King': 1969, 'The Doors': 1967}
>>> name_year['The Doors']
1967
>>> name_year.keys()
['Fun House', 'In The Court Of The Crimson King', 'The Doors']
>>> 'Fun House' in name_year
True
```

Una coppia <i>key:value</i> può essere eliminata attraverso la funzione `del`.

```python
del name_year['Fun House']
```
