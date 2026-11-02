---
tag: VWNSHKJT92
kind: concept
name: Gelfand transform
msc: [46J05, 46J25]
sources:
  - url: https://en.wikipedia.org/wiki/Gelfand_representation
same_as:
  wikidata: Q1499675
  wikipedia: Gelfand representation
---

## Summary

The Gelfand transform turns each element $a$ of a commutative complex [[Banach algebra|9KYWN94QDN]] into a continuous function $\hat a$ on the [[character space|M7JVFJ3MMX]], by $\hat a(\varphi) = \varphi(a)$.
It is an algebra homomorphism into the functions vanishing at infinity, and it does not increase norms.
For a unital algebra, the range of $\hat a$ is the spectrum of $a$.
For commutative C*-algebras it is an isometric isomorphism onto all such functions, by the [[commutative Gelfand–Naimark theorem|NT564Y315M]].

## Explanations

### L1 human

The idea is to view the elements of an abstract commutative algebra as functions.
The points are the characters, and the value of $a$ at a character $\varphi$ is the number $\varphi(a)$.
For sequences $(a_n)_{n \in \Z}$ with $\sum \abs{a_n} < \infty$ and convolution as product, the characters are the points $z$ of the unit circle.
There the Gelfand transform is the Fourier series $\sum_n a_n z^n$, which turns convolution into ordinary multiplication.
