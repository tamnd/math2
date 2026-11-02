---
tag: PNWQZD5GRQ
kind: definition
name: Slice knot
msc: [57K10, 57K40]
defines: P68G28E4AD
uses: [QYEAZTYGPT]
sources:
  - url: https://en.wikipedia.org/wiki/Slice_knot
---

## Definition

Let $B^4$ be the closed unit ball in $\R^4$, with boundary the $3$-sphere $S^3$.
A tame [[knot|QYEAZTYGPT]] $K \subset S^3$ is *smoothly slice* if there is a smoothly embedded $2$-disk $D \subset B^4$ with $\partial D = D \cap S^3 = K$.
It is *topologically slice* if there is such a disk $D$ that is only locally flat.
Without qualification, *slice* means smoothly slice.

## Remarks

The disk $D$ must be properly embedded, meeting $S^3$ only in its boundary.
Example: let $K^*$ be the mirror image of $K$ with reversed orientation.
Then $K \# K^*$ bounds a ribbon disk, made by spinning a half of $K$ in $B^4$, so it is slice; the square knot is an instance.
Non-example: the [[trefoil knot|VYTYSVHN4A]] is not slice, because its signature is $\pm 2$ and the signature of a slice knot is $0$.
By Fox and Milnor, if $K$ is slice then $\Delta_K(t) = f(t) f(t^{-1})$ for some $f \in \Z[t, t^{-1}]$, where $\Delta_K$ is the [[Alexander polynomial|JKA25KDPQP]].
Freedman proved that every knot with $\Delta_K = 1$ is topologically slice.
Some of these knots are not smoothly slice, which shows that the two notions differ.
