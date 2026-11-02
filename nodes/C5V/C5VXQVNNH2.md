---
tag: C5VXQVNNH2
kind: definition
name: Covering density
msc: [52C17, 52C15, 11H31]
defines: BWSN2JAMTK
uses: [2Z2QVWZ262, 0H4R3RESGV, 0Q0H13G8ZB, 4P5PSWADJD]
sources:
  - url: https://en.wikipedia.org/wiki/Covering_problems
---

## Definition

Let $n \ge 1$, let $\operatorname{vol}$ be the [[Lebesgue measure|2Z2QVWZ262]] on $\R^n$, and let $B_R$ be the [[closed ball|0Q0H13G8ZB]] of radius $R$ centred at $0$.
A *covering* of $\R^n$ is a countable family $\mathcal C = (K_i)_{i \in I}$ of compact sets whose union is $\R^n$.
It is required that each bounded set meets only finitely many $K_i$.
The *lower density* of $\mathcal C$ is
$$\underline{d}(\mathcal C) = \liminf_{R \to \infty} \frac{\sum_{i \in I} \operatorname{vol}(K_i \cap B_R)}{\operatorname{vol}(B_R)},$$
with the [[limit inferior|0H4R3RESGV]]; when the limit exists it is the *density* of $\mathcal C$.
Let $K$ be a compact set with nonempty interior.
The *covering density* of $K$ is $\vartheta(K) = \inf \underline{d}(\mathcal C)$, over all coverings $\mathcal C$ of $\R^n$ by congruent copies of $K$.

## Remarks

The ratio is the same as for the [[packing density|4P5PSWADJD]]; packings forbid overlaps, coverings forbid gaps.
Since the sets cover $B_R$, the ratio is at least $1$, so $\vartheta(K) \ge 1$, with equality when $K$ tiles space, as a cube does.
Example: unit discs centred at the points of the triangular lattice spanned by $(\sqrt 3, 0)$ and $(\sqrt 3/2, 3/2)$.
Each disc contains the regular hexagon of circumradius $1$ around its centre, and these hexagons tile the plane, so the discs cover.
The density is $\pi$ divided by the hexagon area $3\sqrt 3/2$, that is $2\pi/\sqrt{27}$.
Non-example: unit discs centred at $2\Z^2$ do not form a covering, since the point $(1, 1)$ is at distance $\sqrt 2 > 1$ from every centre.
For a lattice covering $K + \Lambda$, the density exists and equals $\operatorname{vol}(K)/\det \Lambda$.
