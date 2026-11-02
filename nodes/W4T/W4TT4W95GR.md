---
tag: W4TT4W95GR
kind: definition
name: Normal complex space
msc: [32C20, 32C15]
defines: PN55VEF0J7
uses: [HXSZA44J5J, 831N2Q4GCB, JTAKAPTT8H, H20P600HQS]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_analytic_variety
---

## Definition

Let $(X, \mathcal{O}_X)$ be a [[complex analytic space|HXSZA44J5J]].
A point $x \in X$ is *normal* if the [[stalk|JTAKAPTT8H]] $\mathcal{O}_{X,x}$ is an [[integrally closed domain|H20P600HQS]].
The space $X$ is *normal* if every point of $X$ is normal.

## Remarks

A normal space is [[reduced|831N2Q4GCB]], since an integral domain has no nonzero nilpotents.

Example: the cusp $A = \set{z_1^2 = z_2^3} \subseteq \C^2$ is not normal at $0$.
Its local ring is isomorphic to $\C\{t^2, t^3\}$ by $z_1 \mapsto t^3$, $z_2 \mapsto t^2$.
The element $t = z_1 / z_2$ of the field of fractions satisfies $t^2 - z_2 = 0$, so it is integral, but it does not lie in $\C\{t^2, t^3\}$.

Non-example of another kind: the cross $\set{z_1 z_2 = 0}$ is not normal at $0$, because its local ring has the zero divisors $z_1$ and $z_2$, so it is not a domain.

Example: $\C^n$ is normal, since the ring $\C\{z_1, \dots, z_n\}$ of convergent power series is factorial, and factorial domains are integrally closed.

For a reduced space $X$, there is an equivalent form.
The space $X$ is normal if and only if the following holds for every open $U \subseteq X$.
Every function on $U$ that is holomorphic on the regular points and locally bounded is holomorphic on $U$.
