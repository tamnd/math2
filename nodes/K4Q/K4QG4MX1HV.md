---
tag: K4QG4MX1HV
kind: definition
name: Multidimensional transform
msc: [44A30, 42B10]
defines: 4PVP1C3JZG
uses: [YCK709QB06, 9M0NNNFJGM, FE1ZZJ8QW2]
sources:
  - url: https://en.wikipedia.org/wiki/Multidimensional_transform
---

## Definition

Let $n \ge 2$, let $\Omega \subseteq \R^n$ be a measurable set, and let $U$ be a set.
Let $K \colon U \times \Omega \to \C$ be a function, the [[kernel|9M0NNNFJGM]].
Let $f \colon \Omega \to \C$.
Its *multidimensional transform* with kernel $K$ is
$$(Tf)(u) = \int_\Omega K(u, x)\, f(x)\, dx,$$
a [[multiple integral|FE1ZZJ8QW2]], defined at those $u \in U$ where the integral converges absolutely.
For functions on $\Z^n$ the integral is replaced by a sum over $\Z^n$.

## Remarks

The transform is *separable* when $\Omega = \Omega_1 \times \cdots \times \Omega_n$, $U = U_1 \times \cdots \times U_n$ and $K(u, x) = K_1(u_1, x_1) \cdots K_n(u_n, x_n)$.
Then, by Fubini's theorem, $T$ is the composition of the one-variable transforms with kernels $K_j$ applied in each variable.

Example: $\Omega = U = \R^n$ and $K(\xi, x) = e^{-i \xi \cdot x}$ give the $n$-dimensional [[Fourier transform|DPVM34ADZV]], a separable transform since $e^{-i \xi \cdot x} = \prod_j e^{-i \xi_j x_j}$.

Non-example: the [[Radon transform|VJNZJ352PC]] sends a function on $\R^n$ to its integrals over hyperplanes.
It is not of the form above with a function $K$, since each value is an integral over a set of measure zero.
