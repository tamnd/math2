---
tag: 6VK9RSG13Q
kind: statement
role: theorem
name: Feit–Thompson theorem
msc: [20D10, 20D05]
uses: [0FXJ7YFMMX, 0B85S2V2DR, 0YMYMNQ0QZ]
about: [0FXJ7YFMMX]
sources:
  - url: https://en.wikipedia.org/wiki/Feit%E2%80%93Thompson_theorem
same_as:
  wikidata: Q909517
  wikipedia: Feit–Thompson theorem
---

## Statement

Let $G$ be a finite [[group|G5S1M9]] whose [[order|0B85S2V2DR]] is odd.
Then $G$ is [[solvable|0FXJ7YFMMX]].

## Remarks

An equivalent form: every finite non-abelian [[simple group|0YMYMNQ0QZ]] has even order.
Indeed, a finite group is solvable exactly when all its [[composition factors|0PHTC93M58]] are cyclic of prime order, and every composition factor of a group of odd order has odd order.
The proof, published by Walter Feit and John Thompson in 1963, fills a whole issue of a journal and combines local analysis of subgroups with character theory.
A formal proof was completed in the Coq proof assistant in 2012.
The hypothesis of odd order is necessary: the alternating group $A_5$ has order $60$ and is not solvable.
For example, every group of order $3 \cdot 5 \cdot 7 \cdot 11 = 1155$ is solvable, although [[Burnside's theorem|0FMAQSB1SC]] on groups of order $p^a q^b$ does not apply to it.

## Explanations

### L1 human

The theorem says that a finite group with an odd number of elements can always be broken down into abelian pieces.
So every interesting simple group must have an even number of elements, and hence contain an element of order $2$.

### L2 human

By [[Cauchy's theorem|0JM7PA288B]], a non-abelian finite simple group therefore contains involutions, that is, elements of order $2$.
This opened the way to studying simple groups through the [[centralisers|02YYV36BFM]] of their involutions, the main strategy of the [[classification of finite simple groups|06J6P03MG7]].
The [[Brauer–Fowler theorem|K5CQM8MYYG]] shows that the centraliser of an involution limits the size of the simple group.
