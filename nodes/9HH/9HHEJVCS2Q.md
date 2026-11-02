---
tag: 9HHEJVCS2Q
kind: definition
name: Strongly pseudoconvex domain
msc: [32T15, 32T05]
defines: Z7RVXBA2KB
uses: [80MTNXWW80, PETEQQCS0B]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudoconvexity
---

## Definition

Let $\Omega \subseteq \C^n$ be a domain with $C^2$ boundary, and let $\rho$ be a defining function of $\Omega$.
For $p \in \partial\Omega$, let $H_p$ be the complex tangent space of $\partial\Omega$ at $p$.
The domain $\Omega$ is *strongly pseudoconvex* if the [[Levi form|80MTNXWW80]] of $\partial\Omega$ is positive definite at every boundary point:
$$\sum_{j,k=1}^{n} \frac{\partial^2 \rho}{\partial z_j \partial \bar z_k}(p)\, w_j \bar w_k > 0 \quad \text{for all } p \in \partial\Omega \text{ and all } w \in H_p \setminus \set{0}.$$
A boundary point where this holds is a *strongly pseudoconvex point*.

## Remarks

A strongly pseudoconvex domain is [[Levi pseudoconvex|PETEQQCS0B]].
Many authors also ask $\Omega$ to be bounded.
Example: the unit ball, with $\rho(z) = \abs{z}^2 - 1$, has Levi form $\abs{w}^2$, which is positive for $w \ne 0$.
Non-example: the domain $\set{z \in \C^2 : \abs{z_1}^2 + \abs{z_2}^4 < 1}$ is Levi pseudoconvex but not strongly pseudoconvex.
At $p = (1, 0)$, with $\rho(z) = \abs{z_1}^2 + \abs{z_2}^4 - 1$, the space $H_p$ is $\set{w : w_1 = 0}$ and $L_\rho(p; (0, w_2)) = 4 \abs{p_2}^2 \abs{w_2}^2 = 0$.
A bounded domain $\Omega$ with $C^2$ boundary is strongly pseudoconvex if and only if it has a defining function that is strictly plurisubharmonic near $\partial\Omega$.
This means that $L_\rho(p; \cdot)$ is positive definite on all of $\C^n$, not only on $H_p$.
