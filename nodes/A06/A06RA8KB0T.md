---
tag: A06RA8KB0T
kind: concept
name: Coalgebra
msc: [16T15]
sources:
  - url: https://en.wikipedia.org/wiki/Coalgebra
same_as:
  wikidata: Q1777803
  wikipedia: Coalgebra
---

## Summary

A coalgebra is a vector space $C$ over a field $K$ with a comultiplication $\Delta \colon C \to C \otimes C$ and a counit $\varepsilon \colon C \to K$.
Its axioms come from reversing the arrows in the definition of an [[associative algebra|3CTW1P4HBP]].
The dual space of a coalgebra is an algebra, and the dual of a finite-dimensional algebra is a coalgebra.
Coalgebras are the other half of [[bialgebras|Q9HHVN606G]] and [[Hopf algebras|7XFYP0N84H]], and they model ways of splitting an object into two pieces.

## Explanations

### L1 human

Multiplication takes two elements and returns one; comultiplication takes one element and returns a sum of pairs.
It lists the ways to split an element into two parts.
For the polynomial ring $K[x]$, one can split $x^n$ as $\Delta(x^n) = \sum_{k} \binom{n}{k} x^k \otimes x^{n-k}$, like choosing which of $n$ objects go to the left.
The counit picks out the part where nothing is split off.
Coassociativity says that splitting into three parts gives the same result whichever way one splits first.
