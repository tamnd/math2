---
tag: J29JWVDSEJ
kind: definition
name: Skew polynomial ring
msc: [16S36, 16W20]
defines: S6C8KDBS04
uses: [VF3PV13BA1, 0B1261B5ED, 0VTH8KPCG2]
sources:
  - url: https://en.wikipedia.org/wiki/Ore_extension
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity and let $\sigma \colon R \to R$ be a [[ring endomorphism|0VTH8KPCG2]] with $\sigma(1) = 1$.
The *skew polynomial ring* $R[x; \sigma]$ is the [[Ore extension|VF3PV13BA1]] $R[x; \sigma, 0]$.
So it is a free left $R$-module with basis $1, x, x^2, \dots$, it contains $R$ as a subring, and $x a = \sigma(a) x$ for all $a \in R$.

## Remarks

The product of monomials is $(a x^i)(b x^j) = a \sigma^i(b) x^{i+j}$.
Example: let $R = \C$ and let $\sigma$ be complex conjugation.
Then $x z = \bar z x$ for $z \in \C$, and $x^2 z = x \bar z x = z x^2$, so $x^2$ commutes with all of $\C$ and with $x$; it lies in the center.
Example: for a field $k$, $q \in k$ nonzero, $R = k[y]$ and $\sigma(y) = q y$, the ring $R[x; \sigma]$ has $x y = q y x$; it is the quantum plane.
Non-example: the first Weyl algebra, with $x y = y x + 1$, is an Ore extension $k[y][x; \id, d/dy]$ with a nonzero derivation, so it is not of the form $R[x; \sigma]$ with this $R$ and this $x$.
When $\sigma = \id$ the ring $R[x; \sigma]$ is the ordinary polynomial ring $R[x]$.
Some books call every Ore extension $R[x; \sigma, \delta]$ a skew polynomial ring.
