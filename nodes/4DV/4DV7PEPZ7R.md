---
tag: 4DV7PEPZ7R
kind: definition
name: Jordan algebra
msc: [17C10, 17C50]
defines: 6C2MCVB8C7
uses: [0QA8CHH8MG, 05EGHEQZAW, YP5TQ6WFVN]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_algebra
---

## Definition

Let $F$ be a [[field|0QA8CHH8MG]] of characteristic different from $2$.
A *Jordan algebra* over $F$ is a [[vector space|05EGHEQZAW]] $J$ over $F$ with a bilinear product $J \times J \to J$, $(x, y) \mapsto xy$, such that for all $x, y \in J$:

1. $xy = yx$;
2. $(xy)(xx) = x(y(xx))$.

Clause 2 is the *Jordan identity*.
The product need not be associative, so $J$ is a [[nonassociative ring|YP5TQ6WFVN]] with an $F$-vector space structure.

## Remarks

Example: for an associative $F$-algebra $A$, put $x \circ y = \frac{1}{2}(xy + yx)$.
Clause 1 is clear, and clause 2 follows by expanding: with $x^2 = xx$ in $A$, one has $x \circ x = x^2$, and both $(x \circ y) \circ x^2$ and $x \circ (y \circ x^2)$ equal $\frac{1}{4}(xyx^2 + yx^3 + x^3y + x^2yx)$.
The resulting Jordan algebra is written $A^+$; the Hermitian $n \times n$ complex matrices form a real Jordan subalgebra of $M_n(\C)^+$.
Non-example: $\R^3$ with the cross product satisfies clause 2, since $x \times x = 0$ makes both sides $0$, but fails clause 1, because $x \times y = -y \times x$.
A Jordan algebra is power-associative: the powers of a single element do not depend on the bracketing.
