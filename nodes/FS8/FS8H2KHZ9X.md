---
tag: FS8H2KHZ9X
kind: definition
name: Regular scheme
msc: [14A15, 13H05]
defines: ESPG0BJERZ
uses: [ND6XEY68P4, JTAKAPTT8H, 63XXTF6B5M, MVGBS3J1P7]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_scheme
---

## Definition

A scheme $X$ is *regular* if it is [[locally Noetherian|ND6XEY68P4]] and for every point $x \in X$ the [[stalk|JTAKAPTT8H]] $\mathcal{O}_{X,x}$ is a [[regular local ring|63XXTF6B5M]].
Here a Noetherian local ring $R$ with maximal ideal $\mathfrak{m}$ and residue field $\kappa$ is regular if $\dim_\kappa \mathfrak{m}/\mathfrak{m}^2 = \dim R$, the [[Krull dimension|MVGBS3J1P7]] of $R$.

## Remarks

A regular local ring is an integrally closed domain, so a regular scheme is normal.
Example: $\operatorname{Spec} \Z$ is regular.
Its local rings are $\Q$, of dimension $0$ with $\mathfrak{m} = 0$, and $\Z_{(p)}$, of dimension $1$ with $\mathfrak{m}/\mathfrak{m}^2$ spanned by $p$.
Non-example: the cusp $\operatorname{Spec} k[x, y]/(y^2 - x^3)$ over a field $k$ is not regular at the origin.
There the local ring has dimension $1$, but $\mathfrak{m}/\mathfrak{m}^2$ has basis $x, y$, since $y^2 - x^3 \in \mathfrak{m}^2$; so its dimension is $2 \ne 1$.
