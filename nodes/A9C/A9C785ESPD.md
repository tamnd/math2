---
tag: A9C785ESPD
kind: definition
name: Packing density
msc: [52C17, 05B40, 11H31]
defines: 4P5PSWADJD
uses: [2Z2QVWZ262, 0T3RZQXDYD, 0Q0H13G8ZB]
sources:
  - url: https://en.wikipedia.org/wiki/Packing_density
---

## Definition

Let $n \ge 1$ and let $\operatorname{vol}$ be the [[Lebesgue measure|2Z2QVWZ262]] on $\R^n$.
Let $B_R$ be the [[closed ball|0Q0H13G8ZB]] of radius $R$ centred at $0$.
A *packing* in $\R^n$ is a countable family $\mathcal P = (K_i)_{i \in I}$ of compact sets with pairwise disjoint interiors.
The *upper density* of $\mathcal P$ is
$$\delta(\mathcal P) = \limsup_{R \to \infty} \frac{\sum_{i \in I} \operatorname{vol}(K_i \cap B_R)}{\operatorname{vol}(B_R)},$$
with the [[limit superior|0T3RZQXDYD]]; when the limit exists it is the *density* of $\mathcal P$.
For a compact set $K$ with nonempty interior, the *packing density* of $K$ is $\delta(K) = \sup \delta(\mathcal P)$, over all packings $\mathcal P$ of congruent copies of $K$.

## Remarks

The value lies in $[0, 1]$.
Example: the packing of discs of radius $\tfrac12$ centred at the points of $\Z^2$.
Each disc lies in its unit square, the squares tile the plane, so the ratio tends to $\pi/4$, the share of each square covered by its disc.
Non-example: discs of radius $1$ centred at $\Z^2$ do not form a packing, since neighbouring discs overlap in a set of positive area.
For them the same ratio tends to $\pi > 1$.
For a lattice packing $K + \Lambda$ of a body $K$, the density exists and equals $\operatorname{vol}(K)/\det \Lambda$.
Restricting to lattice packings gives the lattice packing density $\delta_L(K) \le \delta(K)$.
