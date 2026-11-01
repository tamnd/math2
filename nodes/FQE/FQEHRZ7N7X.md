---
tag: FQEHRZ7N7X
kind: definition
name: Gorenstein ring
msc: [13H10, 13D05]
defines: T6HCX959PJ
uses: [0670T59HGE, MZ02BKPHJA, 85H7PRHDPZ, QCJN05GN64, 00MHHZ9SNE, X6JD4AG973, N1QJQEGBFC]
sources:
  - url: https://en.wikipedia.org/wiki/Gorenstein_ring
---

## Definition

Let $R$ be a commutative ring and $M$ an $R$-module.
The *injective dimension* $\operatorname{id}_R M$ is the least $n \ge 0$ such that there is an exact sequence $0 \to M \to I^0 \to \cdots \to I^n \to 0$ of $R$-modules.
Here every $I^j$ must be an [[injective module|85H7PRHDPZ]], and $\operatorname{id}_R M = \infty$ if there is no such sequence.
A commutative [[Noetherian|0670T59HGE]] [[local ring|MZ02BKPHJA]] $R$ is a *Gorenstein local ring* if $\operatorname{id}_R R < \infty$.
A commutative Noetherian ring $R$ is a *Gorenstein ring* if the [[localization|X6JD4AG973]] $R_{\mathfrak{p}}$ is a Gorenstein local ring for every [[prime ideal|00MHHZ9SNE]] $\mathfrak{p}$.

## Remarks

A Gorenstein local ring is [[Cohen–Macaulay|N1QJQEGBFC]], and then $\operatorname{id}_R R = \dim R$.
Equivalently, a Noetherian local ring $(R, \mathfrak{m}, k)$ of dimension $d$ is Gorenstein if and only if $\operatorname{Ext}^i_R(k, R) = 0$ for $i \ne d$ and $\operatorname{Ext}^d_R(k, R) \cong k$.
For an Artinian local ring this says that the socle $(0 :_R \mathfrak{m})$ is a $k$-vector space of dimension $1$, or that $R$ is the [[injective hull|QCJN05GN64]] of $k$ as an $R$-module.
Example: $R = K[x]/(x^n)$ with $n \ge 1$ and $K$ a field is Gorenstein, since its socle is $K x^{n-1}$.
Non-example: $R = K[x,y]/(x^2, xy, y^2)$ is Artinian local with socle $Kx \oplus Ky$ of dimension $2$, so it is not Gorenstein, although it is Cohen–Macaulay.
