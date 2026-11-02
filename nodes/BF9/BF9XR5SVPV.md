---
tag: BF9XR5SVPV
kind: concept
name: Type and cotype
msc: [46B07, 46B09]
sources:
  - url: https://en.wikipedia.org/wiki/Type_and_cotype_of_a_Banach_space
same_as:
  wikidata: Q117615954
  wikipedia: Type and cotype of a Banach space
---

## Summary

Type and cotype measure how far a [[Banach space|06GZ956657]] is from a Hilbert space.
They compare random sign sums $\sum_i \pm x_i$ with the sizes of the $x_i$.
A space of type $p$ makes such sums small, and a space of cotype $q$ makes them large.
A theorem of Kwapień says that a Banach space has type $2$ and cotype $2$ exactly when it is isomorphic to a [[Hilbert space|HM2HHE3J51]].
These notions organise much of the local theory of Banach spaces, around results such as [[Dvoretzky's theorem|NRPQP49N9F]].

## Explanations

### L1 human

Take some vectors and add them with random signs.
In the plane with the usual length, the average squared length of the result is the sum of the squared lengths, by the theorem of Pythagoras.
In other spaces the random sum can be longer or shorter than this.
Type and cotype record the best inequalities between the two sides.
For example, in $\ell^1$ the unit vectors $e_1, \dots, e_n$ give a random sum of norm exactly $n$, much larger than the Pythagorean value $\sqrt{n}$.
