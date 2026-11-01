---
tag: C1PFAQBCB8
kind: definition
name: Complete intersection ring
msc: [13H10, 14M10, 13C40]
defines: EPM2HKGMZS
uses: [0670T59HGE, MZ02BKPHJA, KBN13NPYJQ, 63XXTF6B5M, G9Q61B8A7C, 69R5R2FCS5, T6HCX959PJ, N3XH42KVV3]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_intersection_ring
---

## Definition

Let $(R, \mathfrak{m})$ be a commutative [[Noetherian|0670T59HGE]] [[local ring|MZ02BKPHJA]] and let $\hat{R}$ be its $\mathfrak{m}$-adic [[completion|KBN13NPYJQ]].
Then $R$ is a *complete intersection ring* if the following holds.
There are a [[complete|G9Q61B8A7C]] [[regular local ring|63XXTF6B5M]] $S$ and an [[$S$-regular sequence|69R5R2FCS5]] $f_1, \ldots, f_r$ such that
$$\hat{R} \cong S/(f_1, \ldots, f_r).$$

## Remarks

The completion is used because a Noetherian local ring need not be a quotient of a regular local ring, while its completion always is, by the [[Cohen structure theorem|N3XH42KVV3]].
If $R = S/(f_1, \ldots, f_r)$ with $S$ a regular local ring and $f_1, \ldots, f_r$ an $S$-regular sequence, then $R$ is a complete intersection.
Example: $K[x,y]$ localized at $(x, y)$ and divided by $(xy)$ is a complete intersection, since $xy \ne 0$ is a non-zero-divisor in the domain $K[x,y]_{(x,y)}$.
Example: $K[x]/(x^n)$ is a complete intersection, with $S = K[\![x]\!]$ and $f_1 = x^n$.
Non-example: $K[x,y]/(x^2, xy, y^2)$ is not a complete intersection, because it is not [[Gorenstein|T6HCX959PJ]], while every complete intersection is Gorenstein.
