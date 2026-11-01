---
tag: JEMH9P1NVX
kind: definition
name: Normal ring
msc: [13B22]
defines: KR7SWBYHRQ
uses: [0310REJJY8, 00MHHZ9SNE, X6JD4AG973, H20P600HQS]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_scheme
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]].
The ring $R$ is *normal* if for every [[prime ideal|00MHHZ9SNE]] $\mathfrak{p}$ of $R$, the [[localization|X6JD4AG973]] $R_{\mathfrak{p}}$ is an [[integrally closed domain|H20P600HQS]].

## Remarks

Example: $\Z \times \Z$ is normal.
Its prime ideals are $\mathfrak{q} \times \Z$ and $\Z \times \mathfrak{q}$ for a prime ideal $\mathfrak{q}$ of $\Z$, and the localizations are $\Z_{\mathfrak{q}}$, which are integrally closed domains.
It is not a domain, since $(1, 0) \cdot (0, 1) = 0$.

Non-example: $R = k[x, y]/(y^2 - x^3)$ over a field $k$ is not normal.
At the prime $\mathfrak{p} = (x, y)$, the element $y/x$ of the fraction field of $R_{\mathfrak{p}}$ is a root of $z^2 - x$, but it is not in $R_{\mathfrak{p}}$.

An integral domain is normal if and only if it is integrally closed.
A Noetherian ring is normal if and only if it is a finite product of integrally closed domains.
Some authors use the word "normal ring" only for integrally closed domains.
