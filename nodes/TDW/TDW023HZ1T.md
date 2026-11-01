---
tag: TDW023HZ1T
kind: definition
name: Invertible ideal
msc: [13A15, 13F05, 13C20]
defines: E190TAV2S6
uses: [0QVD7WBFGN, 0F2PTGX1A2, 05WDSN597C, 096Z9MP2ME, BFFA03GE3V]
sources:
  - url: https://en.wikipedia.org/wiki/Fractional_ideal
---

## Definition

Let $R$ be an [[integral domain|0QVD7WBFGN]] with [[field of fractions|0F2PTGX1A2]] $K$.
A *fractional ideal* of $R$ is a nonzero $R$-[[submodule|05WDSN597C]] $I$ of $K$ such that $dI \subseteq R$ for some nonzero $d \in R$.
The product $IJ$ of two fractional ideals is the set of finite sums $\sum a_k b_k$ with $a_k \in I$ and $b_k \in J$.
A fractional ideal $I$ is *invertible* if there is a fractional ideal $J$ with $IJ = R$.
An [[ideal|096Z9MP2ME]] of $R$ is invertible if it is nonzero and invertible as a fractional ideal.

## Remarks

If $I$ is invertible, its inverse is unique and equals $I^{-1} = (R : I) = \set{x \in K : xI \subseteq R}$.
Equivalently, a fractional ideal is invertible exactly when it is a [[projective|BFFA03GE3V]] $R$-module.
For a Noetherian domain, a nonzero ideal is invertible exactly when its localization at every maximal ideal is principal.

Example: let $R = \Z[\sqrt{-5}]$ and $P = (2, 1 + \sqrt{-5})$.
Then $P^2 = (4, 2 + 2\sqrt{-5}, -4 + 2\sqrt{-5})$ contains $6$ and $4$, hence $2$, and all its generators are multiples of $2$, so $P^2 = (2)$.
Thus $J = \frac{1}{2} P$ is a fractional ideal with $PJ = \frac{1}{2}(2) = R$, and $P$ is invertible.

Non-example: let $R = k[x, y]$ for a field $k$ and $\mathfrak{m} = (x, y)$.
If $f \in K$ satisfies $fx \in R$ and $fy \in R$, write $f = a/x = b/y$ with $a, b \in R$; then $ay = bx$, so $x$ divides $a$ and $f \in R$.
Hence $(R : \mathfrak{m}) = R$ and $\mathfrak{m} (R : \mathfrak{m}) = \mathfrak{m} \ne R$, so $\mathfrak{m}$ is not invertible.
