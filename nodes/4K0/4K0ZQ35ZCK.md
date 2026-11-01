---
tag: 4K0ZQ35ZCK
kind: definition
name: Kolmogorov quotient
msc: [54D10, 54B15]
defines: MKFKFTPMXZ
uses: [0CQHFPGJ45, 02BH3MCBQB, 0G8VEZ3WTK, 0NQ1H2X495, 07SG12TQH3]
sources:
  - url: https://en.wikipedia.org/wiki/Kolmogorov_space
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
Two points $x, y \in X$ are topologically indistinguishable when every [[open set|02BH3MCBQB]] of $X$ that contains one of them also contains the other.
This is an [[equivalence relation|0G8VEZ3WTK]] $\equiv$ on $X$.
The *Kolmogorov quotient* of $X$ is the quotient set $\mathrm{KQ}(X) = X / {\equiv}$ with the [[quotient topology|0NQ1H2X495]].

## Remarks

Equivalently, $x \equiv y$ if and only if $\overline{\set{x}} = \overline{\set{y}}$.
The space $\mathrm{KQ}(X)$ is a [[T0 space|07SG12TQH3]].
The quotient map $q \colon X \to \mathrm{KQ}(X)$ is open and closed, and $U \mapsto q(U)$ is a bijection from the open sets of $X$ to the open sets of $\mathrm{KQ}(X)$.
If $X$ is already $T_0$, then $q$ is a homeomorphism.

Example: let $(X, d)$ be a [[pseudometric space|0A3HJX3KTF]] with its topology.
Here $x \equiv y$ if and only if $d(x, y) = 0$, because a point with $d(x, y) > 0$ has a ball around $x$ that misses $y$.
So $\mathrm{KQ}(X)$ is the metric space obtained by identifying points at distance $0$.

Non-example: the identity map of a two-point set $\set{a, b}$ with the trivial topology is not a Kolmogorov quotient map.
Its target is not $T_0$, since $a$ and $b$ have the same neighbourhoods; the Kolmogorov quotient of this space is a single point.
