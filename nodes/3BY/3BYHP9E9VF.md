---
tag: 3BYHP9E9VF
kind: definition
name: Elliptic partial differential equation
msc: [35J15, 35J30, 47F10]
defines: B4TTNHSTRX
uses: [6DZETZ5T9G, F31T650DKY, 0KX66CZMBB]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_partial_differential_equation
---

## Definition

Let $P = \sum_{\abs{\alpha} \le m} a_\alpha(x) \, \partial^\alpha$ be a [[linear differential operator|6DZETZ5T9G]] of order $m$ on an open set $\Omega \subseteq \R^n$, with [[principal symbol|F31T650DKY]] $\sigma_m(P)$.
The operator $P$ is *elliptic at* $x \in \Omega$ if $\sigma_m(P)(x, \xi) \ne 0$ for every $\xi \in \R^n \setminus \set{0}$.
It is *elliptic in* $\Omega$ if it is elliptic at every point of $\Omega$.
The equation $P u = f$ is then an *elliptic partial differential equation*.

For a second-order operator $\sum_{i,j} a_{ij}(x) \partial_i \partial_j + \sum_i b_i(x) \partial_i + c(x)$ with real symmetric $(a_{ij})$, this means that the matrix $(a_{ij}(x))$ is positive definite or negative definite at each $x$.
It is *uniformly elliptic* in $\Omega$ if there is a constant $\theta > 0$ with
$$\sum_{i,j=1}^{n} a_{ij}(x) \, \xi_i \xi_j \ge \theta \abs{\xi}^2 \quad \text{for all } x \in \Omega, \ \xi \in \R^n.$$

## Remarks

Example: the [[Laplacian|0E0B6RA8K0]] $\Delta = \sum_i \partial_i^2$ has principal symbol $\abs{\xi}^2$, which is nonzero for $\xi \ne 0$, so it is elliptic; it is uniformly elliptic with $\theta = 1$.
Example: the [[Cauchy–Riemann operator|PPSSTHTEDE]] $\partial_x + i \partial_y$ on $\R^2$ has symbol $\xi_1 + i \xi_2$, which vanishes only at $\xi = 0$, so it is elliptic of order $1$.
Non-example: the wave operator $\partial_t^2 - \partial_x^2$ has symbol $\tau^2 - \xi^2$, which vanishes at $(\tau, \xi) = (1, 1)$, so it is not elliptic.
If all coefficients are real and $n \ge 2$, an elliptic operator has even order $m$.
Indeed $\sigma_m(x, -\xi) = (-1)^m \sigma_m(x, \xi)$, and a real continuous function that does not vanish on the connected unit sphere cannot change sign.
For nonlinear second-order equations $F(D^2 u, D u, u, x) = 0$, ellipticity is a monotonicity condition of $F$ in the matrix variable $D^2 u$.

## Explanations

### L1 human

An operator is elliptic when its top-order part does not vanish in any direction, which for second-order equations means that the coefficient matrix is definite.
