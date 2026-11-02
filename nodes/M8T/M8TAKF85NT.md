---
tag: M8TAKF85NT
kind: definition
name: Wandering set
msc: [37B20, 37A40]
defines: VNW5FHCQ2M
uses: [0CQHFPGJ45, 0VGFHTM75Y, 02BH3MCBQB, 0QT00PB5G2, P15VQS5DJ9]
sources:
  - url: https://en.wikipedia.org/wiki/Wandering_set
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]] and let $f \colon X \to X$ be a [[continuous map|0VGFHTM75Y]].
A set $W \subseteq X$ is a *wandering set* for $f$ if $f^n(W) \cap W = \emptyset$ for every integer $n \ge 1$.
A point $x \in X$ is a *wandering point* if it has an [[open|02BH3MCBQB]] neighbourhood $U$ that is a wandering set.

## Remarks

If $f$ is a [[homeomorphism|0QT00PB5G2]], the images $f^n(W)$, $n \in \Z$, of a wandering set are pairwise disjoint.
The set of wandering points is open.
In measurable dynamics, let $T$ be a measurable map of a [[measure space|P15VQS5DJ9]] $(X, \mathcal{A}, \mu)$.
A measurable set $W$ of positive measure is called wandering when the sets $T^{-n}(W)$, $n \ge 0$, are pairwise disjoint.
Example: for $f(x) = x + 1$ on $\R$, the set $W = (0, 1)$ has $f^n(W) = (n, n+1)$, which is disjoint from $W$ for $n \ge 1$; so every point of $\R$ is wandering.
Non-example: for $f(x) = x/2$ on $\R$, any open interval $U$ containing $0$ satisfies $0 \in f^n(U) \cap U$ for all $n$, so $U$ is not wandering and $0$ is not a wandering point.

## Explanations

### L1 human

A wandering set never overlaps with any of its later images.
A wandering point is a point with a small open neighbourhood that wanders away and never comes back to meet itself.
