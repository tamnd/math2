---
tag: MD1QFAEFF0
kind: definition
name: Torus knot
msc: [57K10]
defines: NS60VV786W
uses: [QYEAZTYGPT, 03NM7DZXXC]
sources:
  - url: https://en.wikipedia.org/wiki/Torus_knot
---

## Definition

Let $p$ and $q$ be coprime integers.
The *$(p, q)$-torus knot* $T(p, q)$ is the image of the map $f \colon \R / 2\pi\Z \to \R^3$,
$$f(t) = \big( (2 + \cos qt) \cos pt, \ (2 + \cos qt) \sin pt, \ -\sin qt \big).$$
A [[knot|QYEAZTYGPT]] is a *torus knot* if it is isotopic to $T(p, q)$ for some coprime $p, q$ with $\abs{p} \ge 2$ and $\abs{q} \ge 2$.

## Remarks

The image lies on the standard [[torus|03NM7DZXXC]] obtained by revolving the circle $(x - 2)^2 + z^2 = 1$ about the $z$-axis.
The map $f$ is injective because $p$ and $q$ are coprime.
Example: $T(2, 3)$ is the [[trefoil knot|VYTYSVHN4A]]; here $\abs{p}, \abs{q} \ge 2$, so it is a torus knot in the sense above.
Non-example: $T(1, q)$ is isotopic to the [[unknot|1TQ06R4Q66]], so the bound $\abs{p} \ge 2$ fails and it is not counted as a torus knot.
$T(p, q)$ is isotopic to $T(q, p)$, and $T(p, -q)$ is the mirror image of $T(p, q)$.
For $p, q \ge 2$ the Seifert genus of $T(p, q)$ is $(p-1)(q-1)/2$.
