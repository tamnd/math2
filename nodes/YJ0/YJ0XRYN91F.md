---
tag: YJ0XRYN91F
kind: definition
name: Lie superalgebra
msc: [17B70, 17B60]
defines: 7CZ4Q5H78N
uses: [6JZW4JC68Z, 5JJYBJ6A8K, 000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_superalgebra
---

## Definition

Let $k$ be a field of characteristic $0$.
Let $\mathfrak{g} = \mathfrak{g}_{\bar 0} \oplus \mathfrak{g}_{\bar 1}$ be a [[vector space|000AYPA9AJ]] over $k$ graded by $\Z/2\Z = \set{\bar 0, \bar 1}$.
For a homogeneous element $x \in \mathfrak{g}_{a}$ write $\abs{x} = a$, the parity of $x$.
A *Lie superalgebra* structure on $\mathfrak{g}$ is a bilinear map $[\cdot, \cdot] \colon \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$ such that for all homogeneous $x, y, z$:

1. $[\mathfrak{g}_a, \mathfrak{g}_b] \subseteq \mathfrak{g}_{a + b}$ for all $a, b \in \Z/2\Z$;
2. $[x, y] = -(-1)^{\abs{x}\abs{y}} [y, x]$;
3. $(-1)^{\abs{x}\abs{z}} [x, [y, z]] + (-1)^{\abs{y}\abs{x}} [y, [z, x]] + (-1)^{\abs{z}\abs{y}} [z, [x, y]] = 0$.

## Remarks

Example: let $V = V_{\bar 0} \oplus V_{\bar 1}$ with $V_{\bar 0} = k^m$ and $V_{\bar 1} = k^n$.
The space $\mathfrak{gl}(m|n) = \End_k(V)$, graded by the maps that preserve or swap the two parts, with $[x, y] = xy - (-1)^{\abs{x}\abs{y}} yx$ on homogeneous elements, is a Lie superalgebra.
Clause 1 holds because parities add under composition, and clauses 2 and 3 follow from the associativity of composition by expanding the signed products.

Non-example: take the same graded space $\mathfrak{gl}(1|1)$ but the ordinary commutator $[x, y] = xy - yx$.
For the odd elements $x = E_{12}$ and $y = E_{21}$, clause 2 requires $[x, y] = [y, x]$, but $xy - yx = E_{11} - E_{22}$ while $yx - xy = E_{22} - E_{11}$.
So clause 2 fails.

The even part $\mathfrak{g}_{\bar 0}$ is an ordinary [[Lie algebra|5JJYBJ6A8K]], and the bracket makes $\mathfrak{g}_{\bar 1}$ a $\mathfrak{g}_{\bar 0}$-module.
A Lie superalgebra with $\mathfrak{g}_{\bar 1} = 0$ is just a Lie algebra.
Over fields of characteristic $3$ one adds the axiom $[y, [y, y]] = 0$ for odd $y$, and characteristic $2$ needs a separate treatment.
