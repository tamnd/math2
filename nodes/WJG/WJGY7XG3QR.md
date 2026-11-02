---
tag: WJGY7XG3QR
kind: definition
name: Parabolic partial differential equation
msc: [35K10, 35K25]
defines: 1CCTH8X2FT
uses: [B4TTNHSTRX, 6DZETZ5T9G]
sources:
  - url: https://en.wikipedia.org/wiki/Parabolic_partial_differential_equation
---

## Definition

Let $U \subseteq \R^n$ be open, let $T > 0$, and write the variables in $U \times (0, T)$ as $(x, t)$.
Consider a [[linear PDE|6DZETZ5T9G]] in $U \times (0, T)$ of the following form.
$$\partial_t u - \sum_{i,j=1}^{n} a_{ij}(x, t) \, \partial_i \partial_j u + \sum_{i=1}^{n} b_i(x, t) \, \partial_i u + c(x, t) \, u = f(x, t).$$
Here all coefficients are real, $a_{ij} = a_{ji}$, and $\partial_i$ is the derivative in $x_i$.
The equation is a *second-order linear parabolic equation* if its spatial part is [[uniformly elliptic|B4TTNHSTRX]].
That is, there is $\theta > 0$ with
$$\sum_{i,j=1}^{n} a_{ij}(x, t) \, \xi_i \xi_j \ge \theta \abs{\xi}^2 \quad \text{for all } (x, t) \in U \times (0, T), \ \xi \in \R^n.$$

## Remarks

Example: the [[heat equation|VP2HN86VAG]] $\partial_t u - \Delta u = 0$ is parabolic with $a_{ij} = \delta_{ij}$ and $\theta = 1$.
Non-example: the backward heat equation $\partial_t u + \Delta u = 0$ has $a_{ij} = -\delta_{ij}$, which fails the inequality for every $\theta > 0$, so it is not parabolic in this sense.
View a parabolic equation as a second-order equation in the $n + 1$ variables $(x, t)$.
Its coefficient matrix has one zero eigenvalue, in the $t$ direction, and $n$ eigenvalues of the same sign.
This matches the [[classification of second-order PDEs|5FC6BMM1NA]].
Higher-order parabolic equations, such as $\partial_t u + \Delta^2 u = 0$, are defined with an elliptic spatial operator of higher order.

## Explanations

### L1 human

A parabolic equation is a first-order time derivative plus a uniformly elliptic operator in space, with the signs arranged as in the heat equation.
