---
tag: JRTB9SHAFD
kind: definition
name: Reduced complex space
msc: [32C15]
defines: 831N2Q4GCB
uses: [HXSZA44J5J, JTAKAPTT8H, SZHY975FFX]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_analytic_variety
---

## Definition

Let $(X, \mathcal{O}_X)$ be a [[complex analytic space|HXSZA44J5J]].
It is *reduced* if, for every $x \in X$, the [[stalk|JTAKAPTT8H]] $\mathcal{O}_{X,x}$ is a [[reduced ring|SZHY975FFX]], that is, it has no nonzero nilpotent elements.

## Remarks

Example: the local model in $\C^2$ given by $f = z_1 z_2$ is reduced.
Its stalk at $0$ is $\C\{z_1, z_2\}/(z_1 z_2)$, and if $g^k \in (z_1 z_2)$ then $z_1 \mid g^k$ and $z_2 \mid g^k$ in the factorial ring $\C\{z_1, z_2\}$, so $z_1 \mid g$ and $z_2 \mid g$, hence $z_1 z_2 \mid g$.
At the other points the stalk is a ring of convergent power series, which is reduced.

Non-example: the local model in $\C$ given by $f = z^2$ is not reduced, since the class of $z$ in $\C\{z\}/(z^2)$ is nonzero and has square $0$.

Equivalently, $X$ is reduced if every section of $\mathcal{O}_X$ whose value vanishes at every point of its domain is zero.
For any complex space $X$, the quotient of $\mathcal{O}_X$ by its sheaf of nilpotent germs defines a reduced complex space $X_{\mathrm{red}}$ on the same topological space.
