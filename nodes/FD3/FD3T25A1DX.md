---
tag: FD3T25A1DX
kind: definition
name: Local property
msc: [13B30, 13C99]
defines: 3S58E70Z7Z
uses: [0310REJJY8, 0NZ8JA25WK, 00MHHZ9SNE, 68E0F8N94E, X6JD4AG973]
sources:
  - url: https://en.wikipedia.org/wiki/Local_property
---

## Definition

Let $P$ be a property of modules over commutative rings.
The property $P$ is *local* if, for every [[commutative ring|0310REJJY8]] $R$ and every $R$-[[module|0NZ8JA25WK]] $M$, the following are equivalent:

1. $M$ has $P$ as an $R$-module;
2. for every [[prime ideal|00MHHZ9SNE]] $\mathfrak p$ of $R$, the [[localized module|68E0F8N94E]] $M_{\mathfrak p}$ has $P$ as an $R_{\mathfrak p}$-module.

A property of commutative rings is *local* in the same way, with $R$ in place of $M$ and the [[localizations|X6JD4AG973]] $R_{\mathfrak p}$ in place of $M_{\mathfrak p}$.
A property of module homomorphisms $\varphi \colon M \to N$ is local in the same way, with the localized maps $\varphi_{\mathfrak p} \colon M_{\mathfrak p} \to N_{\mathfrak p}$.

## Remarks

Example: the property "$M = 0$" is local.
If $M \ne 0$, pick $m \ne 0$ in $M$; its [[annihilator|HB4XDKJTW8]] is a proper ideal, so it lies in a [[maximal ideal|0PV74TR5FP]] $\mathfrak m$.
Then $m/1 \ne 0$ in $M_{\mathfrak m}$, since $um \ne 0$ for all $u \notin \mathfrak m$.
The converse direction is clear.
It follows that injectivity and surjectivity of a module map, exactness of a sequence, and [[flatness|73RYYEVDKA]] are local.

In each case it is enough to check the maximal ideals instead of all prime ideals.

Non-example: being an [[integral domain|0QVD7WBFGN]] is not a local property of rings.
For a field $k$, the ring $R = k \times k$ has the two prime ideals $k \times 0$ and $0 \times k$, and both localizations are isomorphic to $k$, a domain.
But $(1, 0) \cdot (0, 1) = 0$ in $R$, so $R$ is not a domain.
Being [[Noetherian|0670T59HGE]] is also not local; see [[localization of a Noetherian ring is Noetherian|C618HAK3X6]].
