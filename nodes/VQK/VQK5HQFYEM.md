---
tag: VQK5HQFYEM
kind: statement
role: theorem
name: Twenty-seven lines on a cubic surface
msc: [14J26, 14N10]
uses: [AV2ZAAZXN9, ZT9A6JK8QF, C4KGYAFPN7, 0PF6TM8TWT]
about: [AV2ZAAZXN9]
sources:
  - url: https://en.wikipedia.org/wiki/Cubic_surface
---

## Statement

Let $k$ be an [[algebraically closed field|0PF6TM8TWT]].
Let $X \subset \mathbb{P}^3$ be a smooth cubic surface over $k$.
This means that $X$ is the zero set in [[projective space|ZT9A6JK8QF]] of a homogeneous polynomial $F$ of degree $3$.
Moreover, the partial derivatives of $F$ have no common zero on $X$.
Then $X$ contains exactly $27$ lines of $\mathbb{P}^3$.

## Remarks

One proof identifies $X$ with the [[blow-up|C4KGYAFPN7]] of $\mathbb{P}^2$ at six points $p_1, \ldots, p_6$ in general position, so that $X$ is a [[del Pezzo surface|AV2ZAAZXN9]] of degree $3$.
The lines on $X$ are exactly the curves $E$ with $E^2 = -1$ and $-K_X \cdot E = 1$.
They are the $6$ exceptional curves over the $p_i$ and the strict transforms of the $15$ lines through two of the points.
The other $6$ are the strict transforms of the conics through five of the points, and $6 + 15 + 6 = 27$.
Each of the $27$ lines meets exactly $10$ of the others, and the symmetry group of the incidence configuration is the Weyl group of type $E_6$, of order $51840$.
Smoothness is needed: the cone over a smooth plane cubic is a singular cubic surface.
It contains infinitely many lines, one through the vertex and each point of the base curve.
The result goes back to Cayley and Salmon in 1849.

## Explanations

### L1 human

One might expect a curved surface given by a cubic equation to contain no straight lines at all.
But every smooth cubic surface contains exactly $27$ straight lines, no more and no fewer.
For the Fermat cubic $x^3 + y^3 + z^3 + w^3 = 0$ they can be listed: $x = -\zeta y$, $z = -\zeta' w$ with cube roots of unity $\zeta, \zeta'$, and the analogous lines for the other pairings of the variables.

### L2 human

The theorem is one of the first results of enumerative geometry and a model for counting curves on varieties.
The lines are the $(-1)$-curves of the del Pezzo surface of degree $3$.
Similar counts hold for the other degrees, for instance $16$ such curves on a del Pezzo surface of degree $4$ and $240$ on one of degree $1$.
Over the real numbers a smooth cubic surface has $3$, $7$, $15$ or $27$ real lines.
