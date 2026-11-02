---
tag: VYQATJQNBH
kind: definition
name: Function field of a variety
msc: [14A10, 12F20]
defines: 2D5SS6WM14
uses: [HV6YBS0YDH, 4M94FZH9Y8, 02BH3MCBQB, 0F2PTGX1A2, G9WB27VWP7, JERVQT4C12, XKEXQDRTGH, 4V81611P9N]
sources:
  - url: https://en.wikipedia.org/wiki/Function_field_of_an_algebraic_variety
---

## Definition

Let $k$ be an algebraically closed field and let $X$ be an [[algebraic variety|HV6YBS0YDH]] over $k$.
Consider pairs $(U, f)$ where $U \subseteq X$ is a nonempty [[open subset|02BH3MCBQB]] and $f$ is a [[regular function|4M94FZH9Y8]] on $U$.
Two pairs $(U, f)$ and $(V, g)$ are equivalent if $f = g$ on $U \cap V$.
The *function field* $k(X)$ of $X$ is the set of equivalence classes, called *rational functions* on $X$, with the operations
$$[(U, f)] + [(V, g)] = [(U \cap V, f + g)], \qquad [(U, f)] \cdot [(V, g)] = [(U \cap V, fg)].$$

## Remarks

Since $X$ is irreducible, $U \cap V$ is nonempty and dense, and two regular functions that agree on a nonempty open subset of $U \cap V$ agree on all of $U \cap V$.
This makes the relation transitive and the operations well defined.
$k(X)$ is a field: if $f \ne 0$ on $U$, then $1/f$ is regular on the nonempty open set $U \setminus V(f)$.

If $X$ is an [[affine variety|JERVQT4C12]], then $k(X)$ is the [[field of fractions|0F2PTGX1A2]] of the [[coordinate ring|G9WB27VWP7]] $k[X]$.
If $U$ is a nonempty open subset of $X$, then $k(U) = k(X)$.
$k(X)$ is a [[function field|XKEXQDRTGH]] over $k$ in the algebraic sense: a finitely generated field extension of $k$.

Example: $k(\mathbb{A}^n) = k(x_1, \dots, x_n)$, the [[field of rational functions|4V81611P9N]], since $k[\mathbb{A}^n]$ is the polynomial ring.
Example: for the parabola $X = V(y - x^2)$, $k[X] \cong k[x]$, so $k(X) \cong k(x)$.

Non-example: the construction needs irreducibility.
In $X = V(xy) \subseteq k^2$, the open sets $\set{x \ne 0}$ and $\set{y \ne 0}$ of $X$ are nonempty and disjoint.
So the relation above is not transitive there, and the analogous ring built from $k[X] = k[x, y]/(xy)$, its total ring of fractions, is $k(x) \times k(y)$, which is not a field.
