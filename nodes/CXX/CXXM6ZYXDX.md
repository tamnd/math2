---
tag: CXXM6ZYXDX
kind: definition
name: Homoclinic orbit
msc: [34C37, 37C29]
defines: 6DBSQKZK4W
uses: [07BNRFQ0PJ, 0G4X36AE0X, 07TZ2Q4C1M, 0PKRYB8ATM]
sources:
  - url: https://en.wikipedia.org/wiki/Homoclinic_orbit
---

## Definition

Let $U$ be an open subset of $\R^n$, let $f \colon U \to \R^n$ be locally Lipschitz, and consider the [[autonomous system|07BNRFQ0PJ]] $x' = f(x)$.
Let $x_0 \in U$ be an [[equilibrium point|0G4X36AE0X]].
A solution $\gamma \colon \R \to U$ is homoclinic to $x_0$ if it is not constant and
$$\lim_{t \to -\infty} \gamma(t) = x_0 = \lim_{t \to +\infty} \gamma(t).$$
A homoclinic orbit is the [[trajectory|07TZ2Q4C1M]] $\gamma(\R)$ of such a solution.

## Remarks

A homoclinic orbit lies in the intersection of the stable and the unstable set of $x_0$, and it does not contain $x_0$.
Example: for $x' = y$, $y' = x - x^2$, the function $\gamma(t) = (x(t), x'(t))$ with $x(t) = \frac{3}{2} \operatorname{sech}^2(t/2)$ is a solution.
Indeed $x'' = \frac{3}{2} s - \frac{9}{4} s^2 = x - x^2$ with $s = \operatorname{sech}^2(t/2)$, and $x(t) \to 0$, $x'(t) \to 0$ as $t \to \pm\infty$, so $\gamma$ is homoclinic to the origin.
Its trajectory is the part of the curve $y^2 = x^2 - \frac{2}{3} x^3$ with $x > 0$.
Non-example: for the pendulum $x' = y$, $y' = -\sin x$, the solution with $x(t) \to -\pi$ as $t \to -\infty$ and $x(t) \to \pi$ as $t \to +\infty$ joins two different equilibria in $\R^2$.
So it is a heteroclinic orbit, not a homoclinic one.
A periodic orbit is also not homoclinic, since it does not tend to an equilibrium.

## Explanations

### L1 human

A homoclinic orbit is a path that leaves an equilibrium and comes back to the same one, taking infinite time in both directions.
In the plane it looks like a loop pinned at a saddle point.
