---
layout: post
title: "Laboratorio 8"
description: ""
category: "Laboratorio"
tags: [classi]
---
{% include JB/setup %}
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

## ESERCIZIO XXV

Scrivere un programma che usando la libreria [*Biopython*](http://biopython.org/wiki/Documentation) effettua le seguenti operazioni:

1. Istanziare due oggetti Seq rappresentanti rispettivamente la sequenza `ACT` e la sua sequenza complementare.
2. Usare la libreria SeqIO per parsare il file [`ls_orchid.gbk`](../../../../python/ls_orchid.gbk) in formato `genbank`. Per ciascuna sequenza si stampino l'ID,
    la lunghezza della sequenza e il numero delle occorrenze delle sequenze istanziate al punto precedente rispettivamente nella
    sequenza letta e in quella complementare.
3. Si filtrino le sequenze lette al punto precedente in modo da selezionare solo quelle con una lunghezza inferiore a 700.
4. Si salvino le sequenza filtrate su un nuovo file usando il formato FASTA.

### Soluzione

```python
from Bio import SeqIO
from Bio.Seq import Seq

# Punto 1
seq = Seq('ACT')
seq2 = seq.complement()

# Punto 2
ls_orchid = SeqIO.parse('ls_orchid.gbk',format='genbank')

for seq_orch in ls_orchid:
    seq_o = seq_orch.seq
    seq_c = seq_orch.seq.complement()
    print seq_orch.id, len(seq_o)
    print '\tACT occ: ',str(seq_o).count(str(seq)), '-', str(seq_c).count(str(seq))
    print '\tTGA occ: ',str(seq_o).count(str(seq2)), '-', str(seq_c).count(str(seq2))

# Punto 3
filtered = filter(lambda l: len(l.seq) < 700, SeqIO.parse('ls_orchid.gbk',format='genbank'))

# Punto 4
SeqIO.write(filtered,'ls_orchid.fasta',format='fasta')
```

---
## ESERCIZIO XXVI

Si consideri un albero binario (di ricerca, o BST) costruito in Python utilizzando istanze della seguente classe:

```python
class TNode:
   def __init__(self, data=None, left=None, right=None):
      self.data=data
      self.left=left
      self.right=right
```
1. Si aggiunga un metodo a TNode che, data in input una lista ordinata di interi (ordinamento crescente), costruisca un albero di
    profondità  minima.

2. Si aggiunga un metodo a TNode che stampi a video i contenuti dei nodi in accordo a una visita in profondità
  con ordinamento simmetrico (ovvero depth-first, in-order).

3. Si aggiunga un metodo a TNode che restituisca una lista con i contenuti dei nodi ottenuti in accordo a una visita
    in profondità con ordinamento simmetrico (ovvero depth-first, in-order).


### Soluzione

```python
class TNode:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

# Punto 1    
    @staticmethod   
    def buildTree(intList):
        if not intList:
            return
        if len(intList) == 1:
            return TNode(data=intList[0])
        else:
            midPoint = len(intList)/2
            return TNode(data=intList[midPoint], left = TNode.buildTree(intList[:midPoint]),
                         right = TNode.buildTree(intList[midPoint+1:]))

```
<!---
```python
# Punto 2
    def printTree(self):
        if self.left:
            self.left.printTree()
        print self.data,
        if self.right:
            self.right.printTree()
# Punto 3
    def treeToList(self, outlist=None):
        if not outlist:
            outlist = []
        if self.left:
            self.left.treeToList(outlist)
        outlist.append(self.data)
        if self.right:
            self.right.treeToList(outlist)
        return outlist

lista_nodi = [4,10,12,15,18,22,24,25,31,35,44,50,66,70,90]
myTree = TNode.buildTree(lista_nodi)

myTree.printTree()
print myTree.treeToList()
```
--->