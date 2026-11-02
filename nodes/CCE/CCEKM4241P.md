---
tag: CCEKM4241P
kind: statement
role: theorem
name: Kakutani's solution of the Dirichlet problem
msc: [60J45, 31B20, 60J65]
uses: [22735FGJV6, 8D56GQ4AG8, 0DEB0JMN0W, WND87FBAKC, 0Q4CBD3HX0, B7948M365K, 0HYPR64JM2]
about: [8D56GQ4AG8, 22735FGJV6]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_problem
---

## Statement

Let $d \ge 2$ and let $D \subset \R^d$ be a bounded [[domain|0Q4CBD3HX0]].
For $x \in \R^d$, let $(B_t)_{t \ge 0}$ be a $d$-dimensional [[Brownian motion|22735FGJV6]] started at $x$, with law $P^x$ and expectation $E^x$.
Let $\tau = \inf\set{t > 0 : B_t \notin D}$ be the exit time of $D$.
Let $\varphi \colon \partial D \to \R$ be continuous, and define
$$u(x) = E^x\big[\varphi(B_\tau)\big], \qquad x \in D.$$

1. $\tau < \infty$ almost surely, and $u$ is [[harmonic|0DEB0JMN0W]] on $D$.
2. If $\zeta \in \partial D$ is a [[regular boundary point|B7948M365K]], then $u(x) \to \varphi(\zeta)$ as $x \to \zeta$ with $x \in D$.
3. If every point of $\partial D$ is regular, then $u$ extended by $\varphi$ is the unique solution of the [[Dirichlet problem|8D56GQ4AG8]] with data $\varphi$.

## Remarks

Proof idea: $\tau$ is a [[stopping time|WND87FBAKC]], and $\tau < \infty$ because $D$ is bounded.
Take a ball $\overline{B}(x, r) \subset D$.
The strong Markov property at the exit time of the ball and rotation invariance show that $u(x)$ is the average of $u$ over the sphere $\partial B(x, r)$.
A bounded measurable function with this [[mean value property|0HYPR64JM2]] is harmonic.
At a regular point $\zeta$, a path started near $\zeta$ leaves $D$ quickly and close to $\zeta$, with high probability, which gives clause 2.
Example: for the unit disc and $x = 0$, the exit point $B_\tau$ is uniform on the circle, so $u(0)$ is the average of $\varphi$, as the mean value property requires.
Regularity is needed: on the punctured disc $D = \set{0 < \abs{x} < 1}$ in $\R^2$, Brownian motion never hits $0$, so $u$ ignores $\varphi(0)$.
With $\varphi(0) = 1$ and $\varphi = 0$ on the unit circle one gets $u \equiv 0$, which does not tend to $1$ at $0$.

## Explanations

### L1 human

To solve the Dirichlet problem at a point, start a random walk there and let it wander until it hits the boundary.
Read the boundary value where it hits, and average over all possible paths.
The result is the harmonic function with the given boundary values.

### L2 human

The theorem identifies classical potential theory with the theory of Brownian motion.
The probabilistic regularity criterion, $P^\zeta(\tau = 0) = 1$, agrees with the analytic notion of a regular point given by barriers or Wiener's criterion.
The formula also gives Monte Carlo methods for harmonic functions, such as the walk-on-spheres method.
The distribution of $B_\tau$ under $P^x$ is the harmonic measure of $D$ at $x$.
