---
tag: S5H153HFWC
kind: concept
name: Hochschild homology
msc: ["16E40"]
sources:
  - url: https://en.wikipedia.org/wiki/Hochschild_homology
same_as:
  wikidata: Q1622047
  wikipedia: Hochschild homology
---

## Summary

Hochschild homology is a homology theory for [[associative algebras|3CTW1P4HBP]], with coefficients in a [[bimodule|EM7FHAFD3N]].
It is computed from the Hochschild complex, whose $n$-th term is $M \otimes A^{\otimes n}$.
In degree $0$ it gives $A/[A, A]$, the quotient of the algebra by its commutators.
For smooth commutative algebras in characteristic $0$ it recovers [[Kähler differential forms|7HCFARHG7D]], so it is a noncommutative analogue of differential forms.

## Explanations

### L1 human

Hochschild homology measures how far an algebra is from being commutative, and in which ways.
In the lowest degree it keeps an element $a$ only up to adding commutators $bc - cb$.
For the matrix algebra $M_n(k)$ this quotient is a single copy of $k$, detected by the trace.
In higher degrees it records relations among such commutators, built from tensor products of elements of the algebra.
For the polynomial ring $k[x]$ it is $k[x]$ in degree $0$, the forms $f(x)\,dx$ in degree $1$, and zero above.
