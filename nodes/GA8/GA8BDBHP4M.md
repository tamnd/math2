---
tag: GA8BDBHP4M
kind: statement
role: theorem
name: Posner's theorem
msc: [16R20, 16N60, 16S85]
uses: [Z9TJSZZYG1, C0EDT81EGH, MVT64B3B6H, C5971PGKPH, 5HRKJBAY2V, 0F2PTGX1A2, MDS8655N0Z, 8NE9Q44FEG, QFDC3NYHJE, 667YZTHE96, GJGEVMZ828]
about: [C0EDT81EGH, Z9TJSZZYG1]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_identity_ring
---

## Statement

Let $R$ be a [[prime ring|Z9TJSZZYG1]] that satisfies a monic [[polynomial identity|C0EDT81EGH]].
Let $Z$ be the [[center|MVT64B3B6H]] of $R$, and let $S = Z \setminus \set{0}$.

1. $Z$ is a commutative domain, and each element of $S$ is a regular element of $R$.
2. The ring $Q = R S^{-1}$, obtained by inverting the nonzero central elements, is a finite-dimensional [[central simple algebra|5HRKJBAY2V]] over the [[field of fractions|0F2PTGX1A2]] $F$ of $Z$.
3. $Q$ is the [[classical ring of quotients|C5971PGKPH]] of $R$ on both sides.

## Remarks

Posner proved that a prime PI ring has a classical ring of quotients that is a simple Artinian ring finite-dimensional over its centre.
The sharper statement that one only has to invert the nonzero central elements, given in parts 1 and 2, is a later refinement based on [[central polynomials|667YZTHE96]].
One way to see the original statement: a prime PI ring satisfies the conditions of a [[Goldie ring|QFDC3NYHJE]], so [[Goldie's theorem|MDS8655N0Z]] gives a simple Artinian quotient ring $Q \cong M_s(D)$.
The ring $Q$ satisfies the same multilinear identities as $R$, and then [[Kaplansky's theorem|8NE9Q44FEG]] shows that $Q$ is finite-dimensional over its centre.

Example: $R = M_n(\Z)$ is prime and satisfies $s_{2n}$, its centre is $\Z$, and $Q = M_n(\Q)$, a central simple algebra over $\Q$.

The primeness hypothesis is needed for the conclusion that $Q$ is simple.
The ring $\Z \times \Z$ is commutative, hence PI, but it is not prime, and its classical ring of quotients $\Q \times \Q$ is not simple.

## Explanations

### L1 human

A commutative domain sits inside its field of fractions.
Posner's theorem says that a prime ring satisfying a polynomial identity sits, in the same way, inside a matrix-like algebra over a field: a central simple algebra of finite dimension.
One gets there just by dividing by central elements, as for fractions of integers.

### L2 human

Posner's theorem reduces the study of prime PI rings to orders in central simple algebras.
The dimension of $Q$ over $F$ is a square $n^2$, and $n$ is called the PI degree of $R$.
Combined with the theory of [[generic matrix algebras|GJGEVMZ828]], it is the main tool for questions about prime PI rings, such as their dimension theory and their centres.
