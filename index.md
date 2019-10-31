---
layout: page
title: Esercitazioni Bioinformatica
tagline: Supporting tagline
---
{% include JB/setup %}
Benvenuti alla pagina relativa alle esercitazioni di Bioinformatica, A.A. 2018/2019. \\
Di seguito potrete trovare una lista delle **esercitazioni** presentate a lezione, con le relative soluzioni.

---


#### Laboratori

<ul>
  {% for post in site.posts %}
	{% if post.categories contains 'Laboratorio' %}
    	<li>
      		<a href="{{ post.url }}">{{ post.title }}</a>
    	</li>
    {% endif %}
  {% endfor %}
</ul>

---

#### Chiarificazioni e tutorial sugli elementi presentati a lezione
<ul>
  {% for post in site.posts %}
	{% if post.categories contains 'Tutorial' %}
    	<li>
      		<a href="{{ post.url }}">{{ post.title }}</a>
    	</li>
    {% endif %}
  {% endfor %}
</ul>
---

#### Codice
<ul>
<li>
	<a href="/python/esercizio_tartaglia.py">Esercizio Tartaglia</a>
</li>
</ul>
---

### Problemi con Biopython

Per installare Biopython sono disponibili diverse opzioni:

- Se si utilizza [Anaconda](https://www.continuum.io/downloads) (**scelta consigliata**) aprire il terminale, e digitare
	`conda install biopython` \\
	Alternativamente è possibile installare la libreria utilizzando la GUI Anaconda Navigator.

- Su Windows è possibile utilizzare [l'installer](http://biopython.org/wiki/Download)
	avendo cura di selezionare la versione di python opportuna.

- Installazione dai sorgenti; scaricare l'archivio [biopython-1.xy.tar.gz](http://biopython.org/wiki/Download)). \\
	Da terminale: \\
	Scompattare l'archivio e muoversi nella directory. \\
	Dunque eseguire: \\
	`python setup.py build`\\
	`python setup.py test`\\
	e, se non ci sono errori: \\
	`sudo python setup.py install`

- ...

---

### Alcuni link utili:

#### Python

- [Python Tutor](http://pythontutor.com) un tool attraverso cui scrivere script Python direttamente
	sul web e visualizzarne l'esecuzione step-by-step.
- [Anaconda Distribution](https://www.continuum.io/downloads) la distribuzione consigliata
	di Python.
- [Python Website](http://www.python.org) per documentazione e tutorial.
- [Is Python pass-by-reference or pass-by-value?](http://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/)
interessante post per chiarire come gli argomenti sono passati alle funzioni in Python.
#### Tutorial Online
- [Testare le Regex](https://regex101.com/) in python od altri linguaggi.
- Tutorial su [List Slicing](https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/) in python.
- **Ricorsione**: 
	- [Introduzione alla ricorsione](https://realpython.com/python-thinking-recursively/) su RealPython.com 
	- [Recursion 'Super Power' (in Python) - Computerphile](https://www.youtube.com/watch?v=8lhxIOAfDss) (Torri di Hanoi) YouTube.


#### Bioinformatica

- [Biopython](http://biopython.org/wiki/Biopython) libreria di tool per computational biology in python.
	Per l'installazione si invita ad utilizzare il package manager fornito assieme alla distribuzione di python.
