---
tag: X6QC23AAB9
kind: definition
name: Harmonic map heat flow
msc: ["58E20", "53E99", 35K55]
defines: MD99PYBCE6
uses: [7CBT4SM83Y, W8F8S8DX5X, E6HDE1DFXD, VP2HN86VAG]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_map
---

## Definition

Let $(M, g)$ be a compact [[Riemannian manifold|7CBT4SM83Y]] without boundary, let $(N, h)$ be a Riemannian manifold, and let $u_0 \colon M \to N$ be a smooth map.
Let $0 < T \le \infty$.
A solution of the *harmonic map heat flow* with initial map $u_0$ on $[0, T)$ is a map $u \colon M \times [0, T) \to N$ with these properties.
It is smooth on $M \times (0, T)$, continuous up to $t = 0$, and
$$\frac{\partial u}{\partial t}(x, t) = \tau\big(u(\cdot, t)\big)(x) \quad \text{on } M \times (0, T), \qquad u(x, 0) = u_0(x),$$
where $\tau$ is the [[tension field|W8F8S8DX5X]].

## Remarks

The [[energy|E6HDE1DFXD]] decreases along a solution:
$$\frac{d}{dt} E\big(u(\cdot, t)\big) = -\int_M \abs{\tau(u(\cdot, t))}^2 \, dV_g \le 0.$$
If $N$ is compact, a solution exists on some interval $[0, T)$ with $T > 0$, since the equation is a semilinear parabolic system.
A map $u_0$ is a fixed point of the flow exactly when it is a harmonic map.

Example: for $N = \R$ the Christoffel symbols vanish, and the flow is the [[heat equation|VP2HN86VAG]] $\partial_t u = \Delta_g u$ on $M$.
Its solutions exist for all time and converge to the constant function equal to the mean of $u_0$.

Non-example: a family with $\partial_t u = -\tau(u)$ is not a solution of the harmonic map heat flow but of the backward flow, along which the energy increases.
For $N = \R$ this is the backward heat equation, which is ill-posed.
