---
tag: F8JKDFKJW7
kind: definition
name: Elastic instability
msc: [74G60, 74B20]
defines: 50W7AQMS5Z
uses: [D9TW46P19Y, 0KX66CZMBB]
sources:
  - url: https://en.wikipedia.org/wiki/Elastic_instability
---

## Definition

Consider an elastic system under conservative loads with a load parameter $\lambda \ge 0$.
Let $\Pi(u, \lambda)$ be its total potential energy, a smooth function of the configuration $u$ in a space $U$.
An equilibrium of the system at load $\lambda$ is a configuration $u$ where the first variation $D_u \Pi(u, \lambda)$ vanishes.
The equilibrium is *stable* if $u$ is a strict local minimum of $\Pi(\cdot, \lambda)$.
Let $u_0(\lambda)$ be a smooth branch of equilibria that is stable for small $\lambda$.
The system shows *elastic instability* at the *critical load* $\lambda_c$ if two conditions hold.
The second variation $D_u^2 \Pi(u_0(\lambda), \lambda)$ is [[positive definite|0KX66CZMBB]] for $\lambda < \lambda_c$.
It fails to be positive definite at $\lambda = \lambda_c$.

## Remarks

Example: a rigid bar of length $L$ hinged at its foot, held upright by a torsional spring of stiffness $k$, with a vertical load $P = \lambda$ on top.
With tilt angle $\theta$, $\Pi(\theta, P) = \tfrac{1}{2} k \theta^2 - P L (1 - \cos \theta)$.
The upright state $\theta = 0$ is an equilibrium for every $P$, and $\Pi''(0) = k - P L$.
So it is stable for $P < k/L$ and the critical load is $P_c = k/L$.

Non-example: the same bar hanging down from its hinge, with $\Pi(\theta, P) = \tfrac{1}{2} k \theta^2 + P L (1 - \cos \theta)$.
Here $\Pi''(0) = k + P L > 0$ for every $P \ge 0$, so the second variation never loses positivity and there is no instability.

At $\lambda_c$ the second variation has a nontrivial kernel in the usual cases, and new branches of equilibria bifurcate there.
