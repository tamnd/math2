---
tag: QWSD2JDRP0
kind: definition
name: Normal family
msc: [30D45]
defines: JTVWRXXAKM
uses: [0DG0Z72CQD, 08HJRTG5N7, 0QPHW703PV, 0R8J3ZQMJS]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_family
---

## Definition

Let $U \subseteq \C$ be an open set and let $\mathcal{F}$ be a family of [[holomorphic|0DG0Z72CQD]] functions $U \to \C$.
The family $\mathcal{F}$ is *normal* if every sequence $(f_n)$ in $\mathcal{F}$ has a [[subsequence|0R8J3ZQMJS]] that converges [[uniformly|08HJRTG5N7]] on each [[compact|0QPHW703PV]] subset of $U$.

## Remarks

Example: $\mathcal{F} = \set{z^n : n \ge 1}$ on the unit disc $\mathbb{D}$ is normal.
On a compact set $K \subset \mathbb{D}$ there is $r < 1$ with $\abs{z} \le r$ on $K$, so $\abs{z^n} \le r^n \to 0$ uniformly on $K$.
Non-example: $\set{n z : n \ge 1}$ on $\mathbb{D}$ is not normal.
Each subsequence tends to $\infty$ at each $z \neq 0$ but stays $0$ at $z = 0$, so it does not converge on a disc around $0$.
The limit of a convergent subsequence is holomorphic, by Weierstrass's theorem that [[uniform limits of holomorphic functions are holomorphic|0431RN0R1N]].
Many authors also accept a subsequence that tends to $\infty$ uniformly on compact subsets.
With this convention, and with the chordal metric of the [[Riemann sphere|0CDMXGPSES]], the definition extends to families of meromorphic functions.
