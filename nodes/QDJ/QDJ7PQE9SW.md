---
tag: QDJ7PQE9SW
kind: statement
role: theorem
name: Frobenius theorem on real division algebras
msc: [16K20, "12E15"]
uses: [0WZXK05ME7, 08J2M1JYAG, 09FTAET5Z4, 0GE4DVQKR8]
about: [0EA5BTA0CX]
sources:
  - url: https://en.wikipedia.org/wiki/Frobenius_theorem_(real_division_algebras)
same_as:
  wikidata: Q1361031
  wikipedia: Frobenius theorem (real division algebras)
---

## Statement

Let $D$ be a finite-dimensional associative algebra over the field $\R$ of [[real numbers|08J2M1JYAG]].
Suppose $D$ is a [[division ring|0WZXK05ME7]]: it has a unit $1 \ne 0$ and every nonzero element has a two-sided inverse.
Then $D$ is isomorphic, as an $\R$-algebra, to exactly one of $\R$, the [[complex numbers|09FTAET5Z4]] $\C$, and the [[quaternions|0GE4DVQKR8]] $\mathbb{H}$.

## Remarks

Proof idea: each $a \in D$ lies in the commutative subalgebra $\R[a]$, which is a finite field extension of $\R$, hence $\R$ or $\C$.
Using this, one shows that the set $V$ of elements $u$ with $u^2 \in \R$ and $u^2 \le 0$ is a real subspace with $D = \R \oplus V$.
The rule $\ip{u}{w} = -(uw + wu)/2$ is a positive definite inner product on $V$.
An orthonormal basis of $V$ satisfies the multiplication rules of $\C$ or $\mathbb{H}$, and a fourth basis vector would lead to a contradiction.
The dimensions are $1$, $2$ and $4$.
Associativity is needed: the octonions form an $8$-dimensional real algebra, not associative, in which every nonzero element has an inverse.
Finite dimension is needed: the field $\R(t)$ of rational functions is a commutative division algebra over $\R$ of infinite dimension.

## Explanations

### L1 human

Consider number systems of finite dimension over the reals, where one can divide by every nonzero number.
If the order of brackets in a product does not matter, there are only three of them.
They are the real numbers, the complex numbers and Hamilton's quaternions.
The quaternions are the only one of the three in which $ab$ and $ba$ can differ.

### L2 human

In the language of the [[Brauer group|BEW48TA9WZ]], the only central division algebras over $\R$ are $\R$ and $\mathbb{H}$.
So the Brauer group of $\R$ has order $2$.
This agrees with [[Galois cohomology|9MPCZ3EAJM]]: $\C$ is the [[algebraic closure|0X6AB5P3G1]] of $\R$, and $H^2(\Gal(\C/\R), \C^\times) \cong \Z/2\Z$.
Without associativity, a finite-dimensional real division algebra has dimension $1$, $2$, $4$ or $8$, by work of Kervaire and of Bott and Milnor.
Hurwitz's theorem shows that the normed ones are $\R$, $\C$, $\mathbb{H}$ and the octonions.
