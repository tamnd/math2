---
tag: WCMAN2AJYR
kind: definition
name: Complex multiplication
msc: [11G15, 14H52, 14K22]
defines: D3HEJTVY7G
uses: [427N6S6QQW, 0J7H0YBFDJ, 7SV4WA92SM, 0X6AB5P3G1]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_multiplication
---

## Definition

Let $K$ be a field of characteristic $0$ with [[algebraic closure|0X6AB5P3G1]] $\overline{K}$, and let $E$ be an [[elliptic curve|427N6S6QQW]] over $K$.
Let $\End(E)$ be the ring of [[endomorphisms|0J7H0YBFDJ]] of $E$ defined over $\overline{K}$, that is, morphisms $E \to E$ over $\overline{K}$ that send the origin $O$ to $O$.
For $n \in \Z$ let $[n] \colon E \to E$ be multiplication by $n$; the map $n \mapsto [n]$ embeds $\Z$ in $\End(E)$.
The curve $E$ has *complex multiplication*, or is a *CM elliptic curve*, if $\End(E) \ne \Z$.
That is, $E$ has an endomorphism that is not of the form $[n]$.

## Remarks

In characteristic $0$, $\End(E)$ is either $\Z$ or an order $\mathcal{O}$ in an imaginary [[quadratic field|7SV4WA92SM]] $F$, and one then says that $E$ has CM by $\mathcal{O}$.
Over $\C$, write $E \cong \C/\Lambda$ for a lattice $\Lambda$; then $\End(E) \cong \set{\alpha \in \C : \alpha \Lambda \subseteq \Lambda}$, which explains the name.

Example: $E \colon y^2 = x^3 - x$ over $\Q$.
The map $[i](x, y) = (-x, iy)$ sends $E$ to itself, since $(iy)^2 = -(x^3 - x) = (-x)^3 - (-x)$.
It fixes $O$, and $[i] \circ [i] = [-1]$, so $[i] \ne [n]$ for every integer $n$; hence $E$ has CM, by $\Z[i]$.

Non-example: $y^2 = x^3 + x + 1$ over $\Q$ has $j$-invariant $1728 \cdot \frac{4}{31} = \frac{6912}{31}$, which is not an algebraic integer.
The $j$-invariant of a CM curve is always an algebraic integer, so this curve has endomorphism ring $\Z$.

Over a finite field the endomorphism ring of every elliptic curve is larger than $\Z$, so the notion is mainly used in characteristic $0$.
