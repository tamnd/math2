---
tag: 1JPGWFMAGK
kind: definition
name: Hopf bifurcation
msc: [34C23, 37G15]
defines: F5H8GW1XYS
uses: [0G4X36AE0X, 0BQAA2BK3Q, 047NDTEPCV, 0V33BNKZ9S, 0AA97XA70K]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_bifurcation
---

## Definition

Let $n \ge 2$, let $f \colon \R^n \times \R \to \R^n$ be [[smooth|0V33BNKZ9S]], and consider the family of systems $x' = f(x, \mu)$ with parameter $\mu$.
Assume $f(0, \mu) = 0$ for all $\mu$ near $0$, so that $0$ is an [[equilibrium point|0G4X36AE0X]] for each such $\mu$.
Let $A(\mu)$ be the [[Jacobian matrix|047NDTEPCV]] of $x \mapsto f(x, \mu)$ at $0$.
The family has a *Hopf bifurcation* at $\mu = 0$ if:

1. $A(\mu)$ has a pair of simple complex conjugate [[eigenvalues|0BQAA2BK3Q]] $\alpha(\mu) \pm i \beta(\mu)$ for $\mu$ near $0$, with $\alpha(0) = 0$ and $\beta(0) > 0$;
2. no other eigenvalue of $A(0)$ has zero real part;
3. $\alpha'(0) \ne 0$.

## Remarks

Under these conditions, a family of [[periodic orbits|0AA97XA70K]] branches off the equilibrium at $\mu = 0$, with periods close to $2\pi / \beta(0)$.
If moreover a certain coefficient $\ell_1$, the first Lyapunov coefficient, is nonzero, the orbits exist for $\mu$ on one side of $0$ only and have amplitude of order $\sqrt{\abs{\mu}}$.
The bifurcation is supercritical when $\ell_1 < 0$; in the plane the orbits are then stable limit cycles.
It is subcritical when $\ell_1 > 0$; the orbits are then unstable.

Example: $x' = \mu x - y - x(x^2 + y^2)$, $y' = x + \mu y - y(x^2 + y^2)$.
The Jacobian at $0$ is $\begin{pmatrix} \mu & -1 \\ 1 & \mu \end{pmatrix}$, with eigenvalues $\mu \pm i$.
So $\alpha(\mu) = \mu$, $\beta(\mu) = 1$, and all three clauses hold.
In polar coordinates the system is $r' = \mu r - r^3$, $\theta' = 1$, and the circle $r = \sqrt{\mu}$ is a stable limit cycle for $\mu > 0$.

Non-example: $x' = \mu^2 x - y$, $y' = x + \mu^2 y$.
The eigenvalues are $\mu^2 \pm i$, so $\alpha(\mu) = \mu^2$ and $\alpha'(0) = 0$; clause 3 fails.
