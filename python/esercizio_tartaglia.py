#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

Scrivere un programma in grado di generare un triangolo di Tartaglia
di altezza `n`, dove `n` è  un intero inserito da tastiera.
Ad esempio, per `n = 5` si avrà:
```
1
1   1
1   2   1
1   3   3   1
1   4   6   4   1
```
Per la stampa a video del triangolo si faccia riferimento alla
 funzione fornita.
"""

def stampa_tartaglia(triangolo):
    """ Funzione per stampare a video un triangolo di tartaglia.

    Parametri
    ----------
    triangolo: list of lists [[],[],[],...]
        Lista di liste, corrispondenti alle righe del triangolo di tartaglia.

    Esempio
    -------
    >>> triangolo = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    >>> stampa_tartaglia(triangolo)
                 1
              1     1
           1     2     1
        1     3     3     1

    """
    n_len = len(triangolo)

    # Iterazione sulle righe del triangolo
    for indr, _ in enumerate(triangolo):
        print " "*(n_len-indr)*3,

        #Iterazione sulle colonne
        for col in range(0, indr+1):
            print "%5d" %triangolo[indr][col],
        print


def tartaglia(n):
    """ Funzione per generare un triangolo di tartaglia.

    Parametri
    ---------
    n: int
        Altezza del triangolo da generare

    Output
    ------
    triangolo: list of lists [[],[],[],...]
        Lista di liste, corrispondenti alle righe del triangolo di tartaglia.

    Esempio
    -------
    >>> triangolo = tartaglia(4)
    >>> triangolo
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    """
    triangolo = []

    # Scrivere il proprio codice quì

    return triangolo
