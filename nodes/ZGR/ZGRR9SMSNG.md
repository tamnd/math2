---
tag: ZGRR9SMSNG
kind: definition
name: Distributed parameter system
msc: [93C20, 93C25]
defines: G4QN6KV6EZ
uses: [ZPDTVZQN5K, HM2HHE3J51, EVF180QJXY, GC5BDZ6QBC, VP2HN86VAG]
sources:
  - url: https://en.wikipedia.org/wiki/Distributed_parameter_system
---

## Definition

Let $X$ and $U$ be real or complex [[Hilbert spaces|HM2HHE3J51]], with $X$ infinite-dimensional.
Let $A$ be the generator of a [[$C_0$-semigroup|EVF180QJXY]] $(S(t))_{t \ge 0}$ on $X$, and let $B \colon U \to X$ be a bounded linear operator.
The *(linear) distributed parameter system* given by $A$ and $B$ is the abstract [[control system|ZPDTVZQN5K]]
$$x'(t) = A x(t) + B u(t),$$
with state $x(t) \in X$ and input $u(t) \in U$.
For $x_0 \in X$ and $u \in L^2(0, T; U)$, its *mild solution* is
$$x(t) = S(t) x_0 + \int_0^t S(t - s) B u(s)\, ds, \qquad 0 \le t \le T.$$

## Remarks

In applications $X$ is a space of functions on a spatial domain and $A$ is a differential operator with boundary conditions.
So the system is a [[partial differential equation|GC5BDZ6QBC]] with a control term.
Control acting through the boundary, and point observation, lead to unbounded operators $B$ or $C$, which need a more general theory.

Example: the [[heat equation|VP2HN86VAG]] $\partial_t w(\xi, t) = \partial_\xi^2 w(\xi, t) + b(\xi) u(t)$ on $0 < \xi < 1$, with $w(0, t) = w(1, t) = 0$ and a fixed $b \in L^2(0, 1)$.
Take $X = L^2(0, 1)$, $U = \R$, $A w = w''$ with domain $H^2(0, 1) \cap H^1_0(0, 1)$, and $B u = u\, b$.
This $A$ is self-adjoint with eigenvalues $-k^2 \pi^2$, $k \ge 1$, and generates a $C_0$-semigroup, so the system fits the definition.

Non-example: the system $x' = Ax + Bu$ on $\R^n$ with matrices $A$ and $B$ is a lumped parameter system, not a distributed one, because its state space is finite-dimensional.
