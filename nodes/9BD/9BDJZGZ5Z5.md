---
tag: 9BDJZGZ5Z5
kind: definition
name: Class number
msc: [11R29]
defines: KTKK9B1X41
uses: [MWBDFS2KJ5, WQ46BD3ARY, 0B85S2V2DR, F99RM1T02C, 0PN13BB7BT, 7NPY2CN5KB, KZTFH832H0]
sources:
  - url: https://en.wikipedia.org/wiki/Ideal_class_group
---

## Definition

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]] and $\operatorname{Cl}(K)$ its [[ideal class group|WQ46BD3ARY]].
The *class number* of $K$ is the [[order|0B85S2V2DR]] of this group:
$$h_K = \#\operatorname{Cl}(K).$$
It is a positive integer by the [[finiteness of the class number|F99RM1T02C]].

## Remarks

Example: for $K = \Q(i)$, the ring of integers $\Z[i]$ is a [[Euclidean domain|0PN13BB7BT]], hence a principal ideal domain, so $\operatorname{Cl}(K)$ is trivial and $h_K = 1$.
Example: for $K = \Q(\sqrt{-5})$, $\operatorname{Cl}(K) \cong \Z/2\Z$, so $h_K = 2$.
Non-example: for a general [[Dedekind domain|7NPY2CN5KB]] the class group can be infinite, and then there is no finite class number.
For instance, let $E$ be the elliptic curve $y^2 = x^3 - x$ over $\C$.
The class group of its affine coordinate ring $\C[x, y]/(y^2 - x^3 + x)$ is isomorphic to the infinite group $E(\C)$.
By the [[Stark–Heegner theorem|KZTFH832H0]], the imaginary quadratic fields $\Q(\sqrt{d})$ with $h = 1$ are those with $d = -1, -2, -3, -7, -11, -19, -43, -67, -163$.
