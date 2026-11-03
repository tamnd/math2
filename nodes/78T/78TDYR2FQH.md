---
tag: 78TDYR2FQH
kind: definition
name: Algebra over a field
msc: [17A01]
defines: 1SENAHZW5A
uses: [04C5ZBG1WT, 000AYPA9AJ, 60W3THKGA7]
sources:
  - url: https://en.wikipedia.org/wiki/Algebra_over_a_field
---

## Definition

Let $K$ be a [[field|04C5ZBG1WT]].
An *algebra over $K$* is a [[vector space|000AYPA9AJ]] $A$ over $K$ with a map $A \times A \to A$, $(x, y) \mapsto xy$, such that for all $x, y, z \in A$ and $a, b \in K$:

1. $(x + y)z = xz + yz$.
2. $z(x + y) = zx + zy$.
3. $(ax)(by) = (ab)(xy)$.

## Remarks

The three conditions say that the product is $K$-bilinear.
So an algebra over $K$ is a [[nonassociative algebra|60W3THKGA7]] over the ring $K$.
The algebra is *associative* if $(xy)z = x(yz)$ for all $x, y, z$, *commutative* if $xy = yx$ for all $x, y$, and *unital* if it has an element $1$ with $1x = x1 = x$ for all $x$.
Example: $\C$ is an algebra over $\R$; complex multiplication distributes over addition and $(ax)(by) = ab\,xy$ for real $a, b$.
Non-example: on $\R^2$, the product $(x_1, x_2) * (y_1, y_2) = (x_1 y_1, 1)$ fails clause 3, since $(0 \cdot x) * (0 \cdot y) = (0, 1) \neq (0, 0)$.
