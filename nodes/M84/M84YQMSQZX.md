---
tag: M84YQMSQZX
kind: definition
name: Image of J
msc: [55Q50, 55Q45]
defines: GX8K2SCWVQ
uses: [YYJPRD1HYW, HGZAYPQBXW, 0CGYNDCWRR]
sources:
  - url: https://en.wikipedia.org/wiki/J-homomorphism
---

## Definition

Let $SO = \operatorname{colim}_n SO(n)$ be the infinite [[special orthogonal group|0CGYNDCWRR]], and let $r \ge 0$.
Let $J \colon \pi_r(SO) \to \pi_r^s$ be the stable [[J-homomorphism|YYJPRD1HYW]] into the [[stable homotopy group of spheres|HGZAYPQBXW]] $\pi_r^s$.
The *image of J* in degree $r$ is the subgroup $\im J \subseteq \pi_r^s$.

## Remarks

By Bott periodicity, for $r \ge 1$ the group $\pi_r(SO)$ is $\Z/2$ if $r \equiv 0, 1 \pmod 8$, $\Z$ if $r \equiv 3, 7 \pmod 8$, and $0$ otherwise.
For $r = 4k - 1$, the image is cyclic of order the denominator of $B_{2k}/4k$, where $B_{2k}$ is the [[Bernoulli number|0KC00K7KY4]].
For $r \equiv 0, 1 \pmod 8$ with $r \ge 1$, $J$ is injective and the image is $\Z/2$.

Example: in degree $3$, $B_2 = 1/6$ gives $B_2 / 4 = 1/24$, and the image of J is all of $\pi_3^s \cong \Z/24$.

Non-example: in degree $2$, $\pi_2(SO) = 0$, so the image of J is $0$; the nonzero element $\eta^2$ of $\pi_2^s \cong \Z/2$ is not in the image of J.

J. F. Adams determined the image, with the upper bound depending on the Adams conjecture, which was later proved by Quillen and by Sullivan.
