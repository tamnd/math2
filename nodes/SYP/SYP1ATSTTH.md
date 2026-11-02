---
tag: SYP1ATSTTH
kind: statement
role: theorem
name: Decay of the Fourier transform of surface measure
msc: [42B10, 42B20]
uses: [D5HZKE8E1A, DPVM34ADZV, SQVQ5DQT6W, 0V33BNKZ9S]
about: [DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Oscillatory_integral
---

## Statement

Let $n \ge 2$ and let $S \subseteq \R^n$ be a smooth hypersurface whose [[Gaussian curvature|SQVQ5DQT6W]] is nonzero at every point.
Let $\sigma$ be the surface measure on $S$, and let $\psi \colon \R^n \to \C$ be a [[smooth function|0V33BNKZ9S]] with compact support.
Let $\mu = \psi \, d\sigma$, and let its [[Fourier transform|DPVM34ADZV]] be
$$\hat\mu(\xi) = \int_S e^{-2\pi i x \cdot \xi} \psi(x) \, d\sigma(x).$$
Then there is a constant $C$ such that
$$\abs{\hat\mu(\xi)} \le C (1 + \abs{\xi})^{-(n-1)/2} \quad \text{for all } \xi \in \R^n.$$

## Remarks

By a partition of unity, one may assume that the support of $\psi$ meets $S$ in a small piece.
This piece is the graph of a smooth function $h$ over a ball in $\R^{n-1}$.
Then $\hat\mu(\xi)$ is an [[oscillatory integral|D5HZKE8E1A]] in $n - 1$ variables with phase $-2\pi (x' \cdot \xi' + h(x')\xi_n)$.
If $\xi$ is far from the normal directions to the piece, the phase has no critical point and the integral decays faster than any power.
If $\xi$ is close to a normal direction, the critical points are nondegenerate, because the curvature hypothesis makes the Hessian of $h$ invertible.
Then stationary phase gives the decay $\abs{\xi}^{-(n-1)/2}$.

Example: for the unit sphere $S^2 \subseteq \R^3$ and $\psi = 1$ near $S^2$, a computation in polar coordinates gives
$$\hat\sigma(\xi) = 2\pi \int_{-1}^{1} e^{-2\pi i \abs{\xi} t} \, dt = \frac{2 \sin(2\pi\abs{\xi})}{\abs{\xi}},$$
which decays like $\abs{\xi}^{-1} = \abs{\xi}^{-(3-1)/2}$ and no faster.

The curvature hypothesis is needed.
If $S$ is the hyperplane $\set{x_n = 0}$, which has curvature zero, then $e^{-2\pi i x \cdot \xi} = 1$ on $S$ when $\xi = (0, \ldots, 0, \xi_n)$.
So $\hat\mu(0, \ldots, 0, \xi_n) = \int_S \psi \, d\sigma$ for every $\xi_n$, and there is no decay when this integral is not $0$.

## Explanations

### L1 human

A measure spread on a curved surface, like the sphere, has a Fourier transform that tends to zero at infinity at a definite rate.
The more the surface curves in all directions, the more the waves cancel, and the rate is half the dimension of the surface.
A flat surface gives no decay in the direction perpendicular to it.

### L2 human

This decay is the starting point of the [[Stein–Tomas restriction theorem|ZZVWHNFY6F]], whose proof only uses the bound $\abs{\hat\mu(\xi)} \lesssim \abs{\xi}^{-(n-1)/2}$.
It also gives the dispersive decay of waves and the asymptotics of Bessel functions, since $\hat\sigma$ for the sphere is a Bessel function.
When some principal curvatures vanish, the decay is weaker and is measured by the number of nonvanishing curvatures.
