---
tag: YVQ9CKGA0T
kind: definition
name: Valuation ring
msc: [13F30, 12J20]
defines: QSX12D8RQM
uses: [09S3PFBEPM, 0VF11ZTTMD, B85T5VKR3M]
sources:
  - url: https://en.wikipedia.org/wiki/Valuation_ring
---

## Definition

Let $R$ be an [[integral domain|09S3PFBEPM]] with [[field of fractions|0VF11ZTTMD]] $K$.
The ring $R$ is a *valuation ring* if for every nonzero $x \in K$, at least one of $x$ and $x^{-1}$ lies in $R$.

## Remarks

Example: for a prime $p$, the ring $\Z_{(p)} = \set{a/b : a, b \in \Z,\ p \nmid b}$ is a valuation ring.
Each nonzero rational number is $x = p^n a/b$ with $n \in \Z$ and $a, b$ prime to $p$; if $n \ge 0$ then $x \in \Z_{(p)}$, and if $n < 0$ then $x^{-1} = p^{-n} b/a \in \Z_{(p)}$.
Non-example: $\Z$ is not a valuation ring, since neither $2/3$ nor $3/2$ is an integer.
Every field is a valuation ring of itself.
If $v$ is a [[valuation|B85T5VKR3M]] on a field $K$, then $\set{x \in K : v(x) \ge 0}$ is a valuation ring with fraction field $K$.
Conversely, let $R$ be a valuation ring with fraction field $K$.
Then $K^\times / R^\times$, ordered by $xR^\times \le yR^\times$ when $y/x \in R$, is a totally ordered group.
The quotient map $K^\times \to K^\times/R^\times$ extends to a valuation whose ring is $R$.
A valuation ring is a local ring, with maximal ideal the set of non-units, and any two of its ideals are comparable by inclusion.
