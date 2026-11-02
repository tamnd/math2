---
tag: WRYP2XCKJB
kind: definition
name: Bridge number
msc: [57K10]
defines: G44YY10VC4
uses: [QYEAZTYGPT]
sources:
  - url: https://en.wikipedia.org/wiki/Bridge_number
---

## Definition

Let $K$ be a tame [[knot|QYEAZTYGPT]] in $\R^3$, and let $h \colon \R^3 \to \R$ be the height function $h(x, y, z) = z$.
Call a knot $K'$ in $\R^3$ *generic* if the restriction of $h$ to $K'$ is a Morse function.
The *bridge number* $b(K)$ is the least number of local maxima of $h$ on $K'$, over all generic knots $K'$ ambient isotopic to $K$.

## Remarks

A function on a circle has at least one maximum, so $b(K) \ge 1$.
Example: a round circle in a vertical plane has exactly one maximum, so the [[unknot|1TQ06R4Q66]] has bridge number $1$.
Conversely $b(K) = 1$ only for the unknot, since a knot with one maximum and one minimum bounds an embedded disk.
The [[trefoil knot|VYTYSVHN4A]] has a position with two maxima and is knotted, so its bridge number is $2$.
Non-example: a position of the trefoil with three maxima is generic but does not realize the minimum, so the count $3$ is only an upper bound.
Equivalently, $b(K)$ is the least number of overpasses (bridges) in a diagram of $K$ whose over-strands are disjoint arcs carrying all overcrossings.
Schubert proved $b(K_1 \# K_2) = b(K_1) + b(K_2) - 1$ for the [[knot sum|AGZSZW7GYE]].
