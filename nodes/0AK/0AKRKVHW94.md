---
tag: 0AKRKVHW94
kind: statement
role: theorem
name: Stokes' theorem
aliases: [kelvin-stokes-theorem]
msc: [26B20]
uses: [0GDNHS9J2X, 0YS8RX87F4, 0YPRY7T4PK, 0EKZW08FQ5, 05788J51WZ, 0HR3N02317, 0HPHKCGEQ0]
sources:
  - url: https://en.wikipedia.org/wiki/Stokes%27_theorem
    locator: Theorem
  - url: https://en.wikipedia.org/wiki/Stokes%27_theorem
    locator: History
same_as:
  wikidata: Q467756
  wikipedia: Stokes' theorem
---

## Statement

Let $D \subseteq \mathbb{R}^2$ be the compact region bounded by a piecewise smooth simple closed curve $\gamma$, oriented counterclockwise.
Let $r$ be an injective regular [[parametrised surface|05788J51WZ]] of class $C^2$ on an open set that contains $D$. Let $S = r(D)$ have the unit normal $n = (r_u \times r_v) / \| r_u \times r_v \|$, and let $\partial S$ be the closed curve $r \circ \gamma$.
If $F$ is a vector field of class $C^1$ on an open set that contains $S$, then
$$\oint_{\partial S} F \cdot d\mathbf{r} = \iint_S (\nabla \times F) \cdot n \, dS.$$

## Remarks

The left side is the circulation of $F$ around the boundary. The right side is the [[flux|0YPRY7T4PK]] of the [[curl|0GDNHS9J2X]] of $F$ through $S$.
The orientations match by the right-hand rule: with the thumb along $n$, the fingers curl in the direction of $\partial S$.
Example: for the upper unit hemisphere and $F = (-y, x, 0)$, $\nabla \times F = (0, 0, 2)$, and both sides equal $2\pi$.
For a flat surface in the $xy$-plane, the theorem reduces to [[Green's theorem|0HR3N02317]]. The proof pulls the integrals back to $D$ and applies Green's theorem there.

## History

The theorem first appears in a letter from William Thomson to George Stokes in 1850.
Stokes set it as a question on the Smith's Prize examination at Cambridge in 1854, and the result then got his name.

## Explanations

### L1 human

The total swirl of a field over a surface equals the circulation of the field around the edge of the surface.
The surface can be any shape: only its boundary curve matters.
