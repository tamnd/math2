---
tag: NF8QD0N35D
kind: definition
name: Bernstein algebra
msc: [17D92, 92D10]
defines: S8GFADSZ7M
uses: [A6HRHW6CBY, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Genetic_algebra
---

## Definition

Let $K$ be a [[field|04C5ZBG1WT]].
A *Bernstein algebra* over $K$ is a commutative [[baric algebra|A6HRHW6CBY]] $(A, w)$ over $K$, with weight $w \colon A \to K$, such that
$$(x^2)^2 = w(x)^2\, x^2 \quad \text{for all } x \in A.$$

## Remarks

Example: the gametic algebra with basis $A_1, A_2$ over $\Q$, $A_1^2 = A_1$, $A_2^2 = A_2$, $A_1 A_2 = A_2 A_1 = \tfrac12(A_1 + A_2)$, with $w(A_1) = w(A_2) = 1$.
For $x = pA_1 + qA_2$ one gets $x^2 = p^2 A_1 + q^2 A_2 + pq(A_1 + A_2) = (p + q)x = w(x)\,x$.
Hence $(x^2)^2 = (w(x)\,x)^2 = w(x)^2 x^2$.

Non-example: $A = \Q^2$ with componentwise product and weight $w(s, t) = s$.
For $x = (1, 2)$ one gets $x^2 = (1, 4)$ and $(x^2)^2 = (1, 16)$, while $w(x)^2 x^2 = (1, 4)$.
So the identity fails, although $(A, w)$ is a baric algebra.

Every Bernstein algebra has idempotents: if $w(a) = 1$, then $e = a^2$ satisfies $e^2 = e$ by the identity.
