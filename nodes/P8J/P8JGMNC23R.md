---
tag: P8JGMNC23R
kind: definition
name: Differential graded algebra
msc: ["16E45", 18G35]
defines: GQVAXW5X09
uses: [0GYGHKX834, 3CTW1P4HBP, CAPQBQDRA7]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_graded_algebra
---

## Definition

Let $K$ be a [[commutative ring|0GYGHKX834]].
Let $A = \bigoplus_{n \in \Z} A^n$ be a [[graded|CAPQBQDRA7]] [[associative algebra|3CTW1P4HBP]] over $K$, so that $A^m A^n \subseteq A^{m+n}$; for $a \in A^n$ write $\abs{a} = n$.
A *differential graded algebra* is such an $A$ with a $K$-linear map $d \colon A \to A$ such that:

1. $d(A^n) \subseteq A^{n+1}$ for all $n$.
2. $d \circ d = 0$.
3. $d(ab) = d(a)\, b + (-1)^{\abs{a}} a\, d(b)$ for all homogeneous $a \in A$ and all $b \in A$.

## Remarks

This is the cohomological convention; in the homological convention $d$ lowers the degree by one.
The cohomology $H(A) = \ker d / \operatorname{im} d$ is a graded algebra, because clause 3 makes $\ker d$ a subalgebra and $\operatorname{im} d$ a two-sided ideal of it.
Example: let $K$ be a field, $A^0 = K[x]$, $A^1 = K[x]\, dx$, and $A^n = 0$ otherwise, with $(dx)^2 = 0$.
Put $d(f) = f'\, dx$ on $A^0$ and $d = 0$ on $A^1$.
Clauses 1 and 2 are clear, and clause 3 reduces to the product rule $(fg)' = f'g + fg'$; for $a = f$, $b = g\,dx$ both sides are $0$ since $(dx)^2 = 0$.
Non-example: in the same algebra put $d(f) = f\, dx$ instead.
Clauses 1 and 2 hold, but clause 3 fails: $d(1 \cdot 1) = dx$ while $d(1)\cdot 1 + 1 \cdot d(1) = 2\, dx$.
Every graded algebra with $d = 0$ is a differential graded algebra.
