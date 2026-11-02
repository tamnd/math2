---
tag: FRTE50B74R
kind: statement
role: theorem
name: Splitting principle
msc: [55R40, 57R20]
uses: [BE9NJRVDR3, 6N7BC70CX0, 7HACJC0JE2]
about: [7HACJC0JE2]
sources:
  - url: https://en.wikipedia.org/wiki/Splitting_principle
same_as:
  wikidata: Q7578745
  wikipedia: Splitting principle
---

## Statement

Let $E \to B$ be a complex vector bundle of rank $n$ over a paracompact space $B$.
Then there are a space $F(E)$ and a continuous map $p \colon F(E) \to B$ such that:

1. The pullback $p^* E$ is isomorphic to a [[Whitney sum|BE9NJRVDR3]] $L_1 \oplus \cdots \oplus L_n$ of complex line bundles over $F(E)$.
2. The induced map $p^* \colon H^*(B; \Z) \to H^*(F(E); \Z)$ in [[singular cohomology|6N7BC70CX0]] is injective.

The same holds for a real vector bundle, with real line bundles and with $\Z/2\Z$ coefficients in place of $\Z$.

## Remarks

One can take for $F(E)$ the bundle of complete flags in the fibers of $E$.
It is built in steps.
Over the projective bundle $P(E)$, the pullback of $E$ contains the tautological line bundle and splits it off.
The Leray–Hirsch theorem shows that the pullback in cohomology is injective.
Then one repeats with the complement, of rank $n - 1$.

In use: to prove an identity between [[characteristic classes|7HACJC0JE2]] that is natural and holds in the injective image, it suffices to prove it for sums of line bundles.
For example, the Chern classes of a sum of line bundles are $c(L_1 \oplus \cdots \oplus L_n) = \prod_{i=1}^n (1 + c_1(L_i))$, so $c_k(E)$ pulls back to the $k$-th elementary symmetric polynomial in the classes $x_i = c_1(L_i)$.
The Chern character and the Todd class are defined by symmetric power series in these $x_i$ for this reason.

## Explanations

### L1 human

A vector bundle can be complicated, but a sum of line bundles is easy to handle.
The splitting principle says that any vector bundle becomes such a sum after pulling it back to a suitable bigger space.
The pullback loses no cohomological information, because the map on cohomology is injective.
So a formula about characteristic classes can be checked as if every bundle were a sum of lines.

### L2 human

The splitting principle reduces computations with Chern or Stiefel–Whitney classes of rank $n$ bundles to computations with $n$ first Chern or Stiefel–Whitney classes, the Chern roots.
The Whitney sum formula, the formula for the Chern classes of a tensor product, and the formula $w(T\R P^n) = (1+a)^{n+1}$ all become polynomial identities in these roots.
It is also behind the description of $H^*(BU(n); \Z)$ as the symmetric polynomials in $n$ variables of degree $2$, via the map $BU(1)^n \to BU(n)$.
