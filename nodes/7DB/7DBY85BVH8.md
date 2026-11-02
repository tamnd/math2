---
tag: 7DBY85BVH8
kind: definition
name: Integral scheme
msc: [14A15]
defines: 17NVR4XBHK
uses: [5A35TYZD02, 0QVD7WBFGN, ZXSN8D4MCB, 3A19C4YXGE, 0F2PTGX1A2]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_algebraic_geometry
---

## Definition

A [[scheme|5A35TYZD02]] $X$ is *integral* if $X$ is nonempty and for every nonempty open set $U \subseteq X$ the ring $\mathcal{O}_X(U)$ is an [[integral domain|0QVD7WBFGN]].

## Remarks

A scheme is integral if and only if it is [[reduced|ZXSN8D4MCB]] and its underlying space is irreducible.
An affine scheme $\operatorname{Spec} A$ is integral if and only if $A$ is an integral domain.
Then its [[generic point|3A19C4YXGE]] is $(0)$, and the local ring there is the [[field of fractions|0F2PTGX1A2]] of $A$, the function field.
Example: $\operatorname{Spec} \Z$ is integral, since $\Z$ is a domain and each $\mathcal{O}(D(n)) = \Z[1/n]$ is a domain.
Non-example: $\operatorname{Spec} k[x, y]/(xy)$ for a field $k$ is reduced but not integral, since $x y = 0$ with $x \ne 0$ and $y \ne 0$.
The open set $U = \emptyset$ is excluded because $\mathcal{O}_X(\emptyset)$ is the zero ring, which is not a domain.
