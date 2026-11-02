---
tag: Q5JHEPRYQ6
kind: concept
name: Galois connection
msc: [06A15]
sources:
  - url: https://en.wikipedia.org/wiki/Galois_connection
same_as:
  wikidata: Q1491747
  wikipedia: Galois connection
---

## Summary

A Galois connection is a pair of maps $f \colon P \to Q$ and $g \colon Q \to P$ between [[partially ordered sets|011C29Q1S1]] with $f(x) \le y$ exactly when $x \le g(y)$.
It is a weak form of an order isomorphism, and it is the order-theoretic case of an adjunction between functors.
The [[correspondence between subgroups and subfields|R3625YKQC0]] in Galois theory is the classical example, which gives the notion its name.
Every Galois connection produces a [[closure operator|17FVAN6HXX]] $g \circ f$ on $P$.

## Explanations

### L1 human

A Galois connection pairs two ordered sets so that each map is the best approximation to an inverse of the other.
The map from integers to reals and the floor function form an example.
For an integer $n$ and a real $x$, the statement "$n \le x$" is the same as "$n \le \lfloor x \rfloor$".
So the floor of $x$ is the best integer approximation of $x$ from below.
