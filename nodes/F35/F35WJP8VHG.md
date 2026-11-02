---
tag: F35WJP8VHG
kind: definition
name: Center manifold
msc: [34C45, 37D10]
defines: X45STCVFZR
uses: [07BNRFQ0PJ, 0G4X36AE0X, 047NDTEPCV, WWZTW11664]
sources:
  - url: https://en.wikipedia.org/wiki/Center_manifold
---

## Definition

Let $U$ be an open subset of $\R^n$ and let $f \colon U \to \R^n$ be of class $C^k$ with $k \ge 1$.
Let $\varphi$ be the flow of the [[autonomous system|07BNRFQ0PJ]] $x' = f(x)$.
Let $x_0 \in U$ be an [[equilibrium point|0G4X36AE0X]].
Let $E^c$ be the sum of the generalised eigenspaces of the [[Jacobian matrix|047NDTEPCV]] $Df(x_0)$ for eigenvalues with real part $0$.
A local center manifold of $x_0$ is a set $W^c$ with these properties:

1. $W^c$ is an embedded $C^1$ submanifold of an open neighbourhood $V \subseteq U$ of $x_0$, it contains $x_0$, and its tangent space at $x_0$ is $E^c$.
2. $W^c$ is locally [[invariant|WWZTW11664]]: if $x \in W^c$ and $\varphi_s(x) \in V$ for all $s$ between $0$ and $t$, then $\varphi_t(x) \in W^c$.

## Remarks

The center manifold theorem states that a local center manifold exists and can be chosen of class $C^k$, but it is not unique in general.
Example: for $x' = x^2$, $y' = -y$ at the origin, $E^c$ is the $x$-axis, and the $x$-axis is a center manifold.
For each $c \in \R$, the curve $y = c e^{1/x}$ for $x < 0$ together with $y = 0$ for $x \ge 0$ is also a center manifold.
On it $y' = (-c e^{1/x} / x^2) \cdot x^2 = -y$, and the curve is smooth and tangent to the $x$-axis at $0$.
Non-example: the $y$-axis is invariant and passes through the origin, but its tangent space is the stable direction, not $E^c$, so clause 1 fails.
When $Df(x_0)$ has no eigenvalue with positive real part, the stability of $x_0$ is decided by the reduced equation on a center manifold.

## Explanations

### L1 human

A center manifold is an invariant curved surface through the equilibrium that is tangent to the neutral directions of the linearisation.
On it the motion is slow and decided by nonlinear terms, while off it solutions are attracted or repelled exponentially.
