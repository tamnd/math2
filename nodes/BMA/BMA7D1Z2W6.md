---
tag: BMA7D1Z2W6
kind: statement
role: theorem
name: H-theorem
msc: [82C40, 35Q20, 76P05]
uses: [MH6CSWD7F0, 3QSVWQJX11]
about: [MH6CSWD7F0]
sources:
  - url: https://en.wikipedia.org/wiki/H-theorem
same_as:
  wikidata: Q899853
  wikipedia: H-theorem
---

## Statement

Let $\mathbb{T}^3$ be the three-dimensional torus.
Let $B \colon [0, \infty) \times [-1, 1] \to [0, \infty)$ be a collision kernel with $B > 0$ almost everywhere.
For $v, v_* \in \R^3$ and $\sigma \in S^2$ put $v' = \tfrac12 (v + v_*) + \tfrac12 \abs{v - v_*}\, \sigma$ and $v_*' = \tfrac12 (v + v_*) - \tfrac12 \abs{v - v_*}\, \sigma$.
Let $f(t, x, v) > 0$ be a smooth solution on $[0, T) \times \mathbb{T}^3 \times \R^3$ of the [[Boltzmann equation|MH6CSWD7F0]]
$$\partial_t f + v \cdot \nabla_x f = \int_{\R^3} \int_{S^2} B\big( \abs{v - v_*}, \cos\theta \big) \big( f' f_*' - f f_* \big) \, d\sigma \, dv_*,$$
where $f' = f(t, x, v')$, $f_*' = f(t, x, v_*')$, $f_* = f(t, x, v_*)$, and $\cos\theta = \sigma \cdot (v - v_*) / \abs{v - v_*}$.
Assume that $f$ decays fast enough in $v$ for all the integrals below to converge and for differentiation under the integral sign.
Let $H(t) = \int_{\mathbb{T}^3} \int_{\R^3} f \log f \, dv \, dx$.
Then
$$\frac{dH}{dt} = - \frac14 \int_{\mathbb{T}^3} \int_{\R^3} \int_{\R^3} \int_{S^2} B \, \big( f' f_*' - f f_* \big) \log \frac{f' f_*'}{f f_*} \, d\sigma \, dv_* \, dv \, dx \le 0,$$
and $dH/dt = 0$ at time $t$ if and only if, for every $x$, the function $v \mapsto f(t, x, v)$ is a [[Maxwell–Boltzmann distribution|3QSVWQJX11]].

## Remarks

The transport term does not change $H$ on the torus, since $\int v \cdot \nabla_x (f \log f) \, dx = 0$.
For the collision term one uses the symmetries $(v, v_*) \leftrightarrow (v_*, v)$ and $(v, v_*) \leftrightarrow (v', v_*')$ of the collision integral, which have unit Jacobian.
Averaging the four resulting expressions gives the formula, and the integrand is $\ge 0$ because $(a - b)(\log a - \log b) \ge 0$.
Equality forces $f' f_*' = f f_*$, so $\log f$ is a collision invariant, a combination of $1$, $v$ and $\abs{v}^2$, and $f$ is a Gaussian in $v$.

Example: if $f$ is a global Maxwellian, constant in $x$ and $t$, then $f'f_*' = f f_*$ by conservation of momentum and energy in each collision, and $H$ is constant.

The physical entropy is $-kH$, so the theorem says that the entropy of an isolated dilute gas does not decrease.
It was proved by Ludwig Boltzmann in 1872.

## Explanations

### L1 human

Boltzmann defined a number $H$ that measures how far a gas is from equilibrium.
He showed that collisions between molecules can only make $H$ go down, or keep it the same.
It stays the same only when the velocities are spread in the bell-shaped Maxwell distribution.
This is a version of the second law of thermodynamics, derived from the mechanics of collisions.

### L2 human

The H-theorem gives the a priori bound on $\int f \log f$ that is used in the existence theory for the Boltzmann equation, for instance in the DiPerna–Lions theorem.
It also identifies the equilibria of the collision operator, which is the starting point of the [[Chapman–Enskog theory|CS1VGMQAG3]] and of hydrodynamic limits.
The apparent conflict with time-reversible mechanics, raised by Loschmidt, is resolved by the fact that the Boltzmann equation already contains the assumption of molecular chaos.
