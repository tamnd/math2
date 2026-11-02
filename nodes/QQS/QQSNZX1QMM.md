---
tag: QQSNZX1QMM
kind: concept
name: Dunford–Pettis property
msc: [46B10, 46B20]
sources:
  - url: https://en.wikipedia.org/wiki/Dunford%E2%80%93Pettis_property
same_as:
  wikidata: Q1265637
  wikipedia: Dunford–Pettis property
---

## Summary

A [[Banach space|06GZ956657]] has the Dunford–Pettis property when the following holds.
Pairing a weakly null sequence of vectors with a weakly null sequence of functionals always gives a null sequence of numbers.
The spaces $L^1(\mu)$ and $C(K)$ have it, by results of Dunford and Pettis and of Grothendieck.
No infinite-dimensional [[reflexive space|NN8RWPC8WG]] has it.
The property is a tool to show that some operators on these classical spaces are compact.

## Explanations

### L1 human

In infinite dimensions a sequence can tend to zero in a weak sense while its points stay far from zero.
The same happens to sequences of functionals.
In many spaces, two such sequences can still meet: the values $f_n(x_n)$ need not go to zero.
In $\ell^2$, the unit vectors $e_n$ and the functionals "take the $n$-th coordinate" are both weakly null, yet each value is $1$.
Spaces with the Dunford–Pettis property forbid this.
