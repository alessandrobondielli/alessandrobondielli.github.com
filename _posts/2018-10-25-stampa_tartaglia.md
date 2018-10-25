---
layout: post
title: "Stampa Tartaglia"
description: ""
category: Tutorial
tags: []
---
{% include JB/setup %}

Funzione che stampa un triangolo di tartaglia.
L'argomento della funzione è una lista di liste. 
Ciascuna lista contiene gli elementi di una riga del triangolo.

```python
def stampa_tartaglia(triangolo):
    """
    argument triangolo: list of lists [[], [], [], ...]
    
    """

    n_len = len(triangolo)

    #iterazione sulle righe del tirangolo (i.e. le liste)
    for i, _ in enumerate(triangolo):
        print " "*(n_len-i)*3,

        #iterazione su ciascuna colonna
        for col in range(0, i+1):
            print "%5d" %triangolo[i][col],
        print 

```
