---
tag: FE1VTGF349
kind: definition
name: Kontsevich integral
msc: [57K16]
defines: 727ZEPVSTC
uses: [QYEAZTYGPT, TWH3WVKFF1]
sources:
  - url: https://en.wikipedia.org/wiki/Kontsevich_invariant
---

## Definition

Identify $\R^3$ with $\C \times \R$, with complex coordinate $z$ and height $t$.
Let $K$ be an oriented [[knot|QYEAZTYGPT]] in $\C \times \R$ such that the height $t$ restricted to $K$ is a Morse function.
Let $t_{\min}$ and $t_{\max}$ be the minimum and the maximum of $t$ on $K$.
Let $\mathcal{A}$ be the $\C$-vector space of chord diagrams on the circle modulo the four-term relation and the one-term relation.
The one-term relation kills every diagram with an isolated chord.
Let $\widehat{\mathcal{A}}$ be the completion of $\mathcal{A}$ by degree.
For $t_{\min} < t_1 < \cdots < t_m < t_{\max}$, let $P = \set{(z_j, z_j')}_{j=1}^{m}$ be a choice of two distinct points of $K$ at height $t_j$, for each $j$.
Let $D_P$ be the chord diagram with these $m$ chords, and $\downarrow_P$ the number of chosen points where $K$ is oriented downward.
The *Kontsevich integral* of $K$ is
$$Z(K) = \sum_{m \ge 0} \frac{1}{(2\pi i)^m} \int_{t_{\min} < t_1 < \cdots < t_m < t_{\max}} \sum_{P} (-1)^{\downarrow_P} D_P \bigwedge_{j=1}^{m} \frac{dz_j - dz_j'}{z_j - z_j'} \in \widehat{\mathcal{A}}.$$

## Remarks

Each integral converges, and $Z(K)$ is unchanged by isotopies that keep the number of critical points of the height fixed.
Let $c$ be the number of critical points and $H$ the unknot embedded with two maxima and two minima.
Then the normalized $\widehat{Z}(K) = Z(H)^{-c/2} Z(K)$, with the product in $\widehat{\mathcal{A}}$, is an isotopy invariant of $K$.
Example: the degree-$0$ part of $Z(K)$ is the empty chord diagram with coefficient $1$, since the term $m = 0$ is the constant $1$.
Non-example: the unnormalized $Z$ is not an invariant, because adding a pair of critical points multiplies it by $Z(H)$, which is not $1$.
Every rational-valued [[finite type invariant|TWH3WVKFF1]] of type $\le n$ factors through $\widehat{Z}$ followed by a linear map on the part of degree $\le n$.
