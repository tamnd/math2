---
tag: NN77VYSGXR
kind: concept
name: Cyclotomic field
msc: [11R18]
specializes: [MWBDFS2KJ5]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclotomic_field
same_as:
  wikidata: Q1554628
  wikipedia: Cyclotomic field
---

## Summary

The $n$-th cyclotomic field is the field $\Q(\zeta_n)$ obtained by adjoining to $\Q$ a [[primitive $n$-th root of unity|0EHM5ZP5QH]] $\zeta_n$.
It is a [[Galois extension|0QMZAQ6QQ4]] of $\Q$ of degree $\varphi(n)$ whose Galois group is the [[group of units of $\Z/n\Z$|0F8X8ZRQ53]].
By the [[Kronecker–Weber theorem|AW00HPFB54]], every finite abelian extension of $\Q$ lies in some cyclotomic field.
Cyclotomic fields were studied by Kummer in his work on Fermat's Last Theorem, which led to the notion of a [[regular prime|B4VK33PCXZ]].

## Explanations

### L1 human

The $n$-th roots of unity are the $n$ corners of a regular $n$-gon inscribed in the unit circle, with one corner at $1$.
The cyclotomic field is what you get by adjoining these corners to the rational numbers.
For $n = 4$ the corners are $1, i, -1, -i$, and the field is $\Q(i)$.
For $n = 3$ the field is $\Q(\sqrt{-3})$, since $e^{2\pi i/3} = (-1 + \sqrt{-3})/2$.
The symmetries of the field are the maps $\zeta_n \mapsto \zeta_n^a$ with $a$ coprime to $n$.
