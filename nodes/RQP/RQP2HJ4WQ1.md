---
tag: RQP2HJ4WQ1
kind: definition
name: Ring of invariants
msc: [13A50, 14L24]
defines: 6VTR5EBNYC
uses: [0310REJJY8, 0WCY42EV9V, 0GNCRPYXYV, 0SDC934R52, 0VHSHB9B6J, 0GW1ZZH0R4]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_theory
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $G$ be a group that [[acts|0WCY42EV9V]] on $R$ by ring automorphisms, written $r \mapsto g \cdot r$.
The *ring of invariants* of the action is
$$R^G = \set{ r \in R : g \cdot r = r \text{ for all } g \in G }.$$

## Remarks

$R^G$ is a [[subring|0GNCRPYXYV]] of $R$, because each $g$ acts by a ring homomorphism and so fixes $0$, $1$, sums and products of fixed elements.
The main case is a group $G$ acting linearly on a finite-dimensional vector space $V$ over a field $k$.
Then $G$ acts on the [[polynomial ring|0SDC934R52]] $k[V]$ of polynomial functions by $(g \cdot f)(v) = f(g^{-1} v)$.
Emmy Noether proved that for a finite group $G$ acting by $k$-algebra automorphisms on a finitely generated commutative $k$-algebra $R$, the ring $R^G$ is finitely generated.

Example: the symmetric group $S_n$ acts on $k[x_1, \ldots, x_n]$ by permuting the variables.
Its ring of invariants is the ring of [[symmetric polynomials|0VHSHB9B6J]], which is a polynomial ring in the elementary symmetric polynomials by the [[fundamental theorem of symmetric polynomials|0GW1ZZH0R4]].

Example: let $G = \set{1, g}$ act on $k[x, y]$ by $g \cdot x = -x$ and $g \cdot y = -y$, where the characteristic of $k$ is not $2$.
A monomial $x^a y^b$ is fixed exactly when $a + b$ is even, so $k[x, y]^G = k[x^2, xy, y^2]$.

Non-example: in the last example, $x \notin k[x, y]^G$, because $g \cdot x = -x \ne x$.
