---
tag: 441JWPAV3W
kind: definition
name: Stochastic partial differential equation
msc: [60H15, 35R60, 60H17]
defines: PRCQG82QTK
uses: [GC5BDZ6QBC, 22735FGJV6, 0QH5ENKZM1, 3VBRS94V1G, SJZX81A783]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_partial_differential_equation
---

## Definition

Let $(\Omega, \mathcal{F}, \mathbb{P})$ be a probability space, let $D \subseteq \R^d$ be open and let $T > 0$.
Let $L$ be a linear differential operator in the variable $x \in D$, and let $F$ and $G$ be functions.
Let $\xi$ be a random noise on $[0, T] \times D$, for example space-time white noise, the formal time derivative of a cylindrical [[Wiener process|22735FGJV6]] $W$.
A *stochastic partial differential equation* is an equation for a random field $u(t, x, \omega)$ of the form
$$\partial_t u = L u + F(u) + G(u) \, \xi, \qquad t \in (0, T], \ x \in D,$$
with initial and boundary conditions.
In Itô form it reads $du = (L u + F(u)) \, dt + G(u) \, dW$.
A solution is a [[stochastic process|0QH5ENKZM1]], adapted to the filtration of $W$, that satisfies the equation in a [[weak|SJZX81A783]] or [[mild|3VBRS94V1G]] sense.
Classical derivatives are not used, because $\xi$ is too irregular.

## Remarks

Example: the stochastic heat equation $\partial_t u = \partial_x^2 u + \xi$ on $(0, 1)$ with $u = 0$ at $x = 0, 1$ and $u(0, \cdot) = 0$, where $\xi$ is space-time white noise.
Its mild solution is $u(t, x) = \int_0^t \int_0^1 p_{t-s}(x, y) \, W(ds, dy)$, with $p$ the Dirichlet heat kernel of $(0, 1)$.
This is a well-defined Gaussian random field, continuous in $(t, x)$.
Non-example: the stochastic differential equation $dX = -X \, dt + dB$, with $B$ a Brownian motion, is driven by noise.
But it involves no derivatives in a space variable, so it is not a partial differential equation.
The same stochastic heat equation in dimension $d \ge 2$ still has a mild solution, but it is a random distribution rather than a function.
