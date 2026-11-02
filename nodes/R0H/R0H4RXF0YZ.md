---
tag: R0H4RXF0YZ
kind: concept
name: Pincherle derivative
msc: [47B47, 44A45]
sources:
  - url: https://en.wikipedia.org/wiki/Pincherle_derivative
same_as:
  wikidata: Q7194927
  wikipedia: Pincherle derivative
---

## Summary

The Pincherle derivative of a linear operator $T$ on polynomials is the commutator $T' = Tx - xT$ of $T$ with multiplication by $x$.
It behaves like a derivative: it is linear and satisfies the product rule $(ST)' = S'T + ST'$.
It turns the [[differentiation operator|BB15T3J891]] into the identity, and each shift operator $f(x) \mapsto f(x + h)$ into $h$ times itself.
It is a basic tool in umbral calculus.

## Explanations

### L1 human

Operators on polynomials can be "differentiated" too.
The Pincherle derivative measures how far an operator is from commuting with multiplication by $x$.
Operators that commute with multiplication by $x$, such as multiplication by a fixed polynomial, have derivative $0$, like constants.
Differentiation $d/dx$ has Pincherle derivative the identity, just as $x$ has derivative $1$.
