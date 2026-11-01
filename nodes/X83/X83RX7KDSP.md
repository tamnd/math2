---
tag: X83RX7KDSP
kind: definition
name: Integral element
msc: [13B21]
defines: 1EHN4KPSFS
uses: [0310REJJY8, 0GNCRPYXYV, 0C3QBCR46M, 0SDC934R52]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_element
---

## Definition

Let $B$ be a [[commutative ring|0310REJJY8]] and let $A$ be a [[subring|0GNCRPYXYV]] of $B$.
An element $b \in B$ is *integral over $A$* if there are an integer $n \ge 1$ and elements $a_0, \ldots, a_{n-1} \in A$ such that
$$b^n + a_{n-1} b^{n-1} + \cdots + a_1 b + a_0 = 0.$$
Equivalently, $b$ is a root of a [[monic polynomial|0C3QBCR46M]] in $A[x]$.
More generally, for a ring homomorphism $f \colon A \to B$, an element $b$ is integral over $A$ if it is integral over the subring $f(A)$.

## Remarks

Example: $i \in \C$ is integral over $\Z$, because $i^2 + 1 = 0$ and $x^2 + 1$ is monic with integer coefficients.

Non-example: $1/2 \in \Q$ is not integral over $\Z$.
By the [[rational root theorem|0819CQ1V8H]], a rational root of a monic polynomial with integer coefficients is an integer.

The following are equivalent for $b \in B$:

1. $b$ is integral over $A$.
2. The subring $A[b]$ is a [[finitely generated|05QY1VEBYD]] $A$-module.
3. $A[b]$ is contained in a subring $C$ of $B$ that is a finitely generated $A$-module.

The proof of 3 implies 1 uses the [[determinant trick|A8HRT9H3XA]].
When $A$ and $B$ are fields, an element is integral exactly when it is [[algebraic|0H628RSGWX]], since a nonzero polynomial over a field can be divided by its leading coefficient.
