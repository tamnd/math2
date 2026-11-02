---
tag: WZQ12PPVA2
kind: definition
name: Cut locus
msc: [53C22]
defines: X5WKGC5Q6T
uses: [7CBT4SM83Y, B4QR306D8G, Y7Z0AGY1A7, NSYMQMHPDN]
sources:
  - url: https://en.wikipedia.org/wiki/Cut_locus
---

## Definition

Let $(M, g)$ be a complete connected [[Riemannian manifold|7CBT4SM83Y]] with [[Riemannian distance|B4QR306D8G]] $d$, and let $p \in M$.
For a unit vector $v \in T_pM$, let $\gamma_v(t) = \exp_p(tv)$ be the unit-speed [[geodesic|NSYMQMHPDN]] from $p$ in direction $v$, using the [[exponential map|Y7Z0AGY1A7]], and let
$$t_c(v) = \sup \set{ t > 0 : d(p, \gamma_v(t)) = t } \in (0, \infty].$$
If $t_c(v) < \infty$, the point $\gamma_v(t_c(v))$ is the *cut point* of $p$ along $\gamma_v$.
The *cut locus* of $p$ is the set of all cut points of $p$, over all unit vectors $v \in T_pM$.

## Remarks

Example: on the unit sphere $S^n$, every unit-speed geodesic from $p$ is a great circle with $d(p, \gamma_v(t)) = t$ for $t \le \pi$ and $d(p, \gamma_v(t)) < t$ just after $t = \pi$.
So $t_c(v) = \pi$ for every $v$, and the cut locus of $p$ is the single point $-p$.

Non-example: in $\R^n$ with the Euclidean metric, $d(p, p + tv) = t$ for all $t > 0$, so $t_c(v) = \infty$ for all $v$, there are no cut points, and the cut locus is empty.

Let $q = \gamma_v(t_c(v))$ be the cut point of $p$ along $\gamma_v$.
Then $q$ is the first point [[conjugate|ZPXE5VSZ35]] to $p$ along $\gamma_v$, or there are two distinct minimizing geodesics from $p$ to $q$, or both.
The cut locus is a closed set of measure zero, and $\exp_p$ maps the open star-shaped set $\set{tv : \abs{v} = 1, \ 0 \le t < t_c(v)}$ diffeomorphically onto $M$ minus the cut locus of $p$.
