---
tag: FMWGQ0W2X0
kind: definition
name: Finite type invariant
msc: [57K16, 57K10]
defines: TWH3WVKFF1
uses: [QYEAZTYGPT, GZQ5ZE3X6G]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_type_invariant
---

## Definition

Let $G$ be an abelian group and $v$ a [[knot invariant|GZQ5ZE3X6G]] of oriented [[knots|QYEAZTYGPT]] with values in $G$.
A *singular knot* is an immersion of the oriented circle in $\R^3$ whose only singularities are finitely many transverse double points.
At a double point, let $K_+$ and $K_-$ be its positive and negative resolutions into crossings.
Extend $v$ to singular knots by the rule $v(K_\times) = v(K_+) - v(K_-)$, applied at each double point.
The invariant $v$ is of *type* $\le n$ if its extension vanishes on every singular knot with more than $n$ double points.
It is a *finite type invariant*, or *Vassiliev invariant*, if it is of type $\le n$ for some $n$.

## Remarks

The extension is well defined: resolving the double points in different orders gives the same alternating sum over all $2^k$ resolutions.
The invariants of type $\le 0$ are the constants, and for knots so are those of type $\le 1$.
Example: the coefficient $c_2$ of $z^2$ in the Conway polynomial is of type $\le 2$.
Non-example: $c_2$ is not of type $\le 1$, since it takes the value $1$ on a singular knot with two double points whose chords cross.
After the substitution $t = e^h$, the coefficient of $h^n$ in the [[Jones polynomial|4SPC17FPXE]] is of type $\le n$.
