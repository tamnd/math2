---
tag: RSBGYTQ1WG
kind: definition
name: Division algebra
msc: [17A35]
defines: 8H3JKHAAHE
uses: [1SENAHZW5A]
sources:
  - url: https://en.wikipedia.org/wiki/Division_algebra
---

## Definition

Let $K$ be a field and let $A$ be an [[algebra|1SENAHZW5A]] over $K$ with $A \neq 0$.
$A$ is a *division algebra* if for all $a, b \in A$ with $a \neq 0$:

1. there is exactly one $x \in A$ with $ax = b$, and
2. there is exactly one $y \in A$ with $ya = b$.

## Remarks

Equivalently, for each nonzero $a$ the $K$-linear maps $x \mapsto ax$ and $x \mapsto xa$ are bijections of $A$.
If $A$ has finite dimension, this holds if and only if $A$ has no zero divisors: $ab = 0$ implies $a = 0$ or $b = 0$.
This follows from the rank-nullity theorem applied to the two maps.
Example: the [[quaternions|0GE4DVQKR8]] form a division algebra over $\R$, since a nonzero $q$ has the inverse $\bar{q}/(q\bar{q})$ and then $x = q^{-1}b$ and $y = bq^{-1}$.
Non-example: the algebra of $2 \times 2$ real matrices is not a division algebra; for $a = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $b$ the identity matrix, $ax = b$ has no solution.
For associative algebras with a unit, the definition says that $A$ is a [[division ring|0EA5BTA0CX]].
