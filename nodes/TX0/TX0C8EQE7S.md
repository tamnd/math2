---
tag: TX0C8EQE7S
kind: definition
name: Chapman–Enskog theory
msc: [82C40, 76P05, 35Q20]
defines: CS1VGMQAG3
uses: [MH6CSWD7F0, 3QSVWQJX11, HHTG8JVGKQ, 22V2W7KB1D, RW0JK9VDZE, 18KXZHVF4M]
sources:
  - url: https://en.wikipedia.org/wiki/Chapman%E2%80%93Enskog_theory
---

## Definition

Consider the [[Boltzmann equation|MH6CSWD7F0]] in the scaling
$$\partial_t f + v \cdot \nabla_x f = \frac{1}{\varepsilon} Q(f, f),$$
where $\varepsilon > 0$ is the [[Knudsen number|22V2W7KB1D]] and $Q$ is the collision operator.
Let $\rho$, $u$ and $T$ be the density, bulk velocity and temperature of $f$, as in the [[kinetic theory of gases|HHTG8JVGKQ]].
The *Chapman–Enskog expansion* seeks solutions of the form
$$f = f^{(0)} + \varepsilon f^{(1)} + \varepsilon^2 f^{(2)} + \cdots$$
subject to the following conditions.

1. Each $f^{(j)}$ depends on $(t, x)$ only through $\rho$, $u$, $T$ and their spatial derivatives at $(t, x)$.
2. $f^{(0)}$ is the local [[Maxwell–Boltzmann distribution|3QSVWQJX11]] with the fields $\rho$, $u$, $T$, and $f^{(j)}$ for $j \ge 1$ has zero mass, momentum and energy moments.
3. The fields obey conservation laws whose fluxes are expanded in the same way, $\partial_t = \partial_t^{(0)} + \varepsilon \partial_t^{(1)} + \cdots$, and each order is solved in turn.

*Chapman–Enskog theory* is the derivation of fluid equations from this expansion by truncation at a given order.

## Remarks

Truncation at order $0$ gives the compressible [[Euler equations|RW0JK9VDZE]].
Truncation at order $1$ gives the compressible [[Navier–Stokes equations|18KXZHVF4M]] with Fourier heat conduction.
The viscosity and the heat conductivity are given by solutions of linear integral equations with the linearized collision operator.
Truncation at order $2$ gives the Burnett equations, which have known instabilities.

Example: for the BGK operator $Q(f) = \nu(M[f] - f)$ the order-$1$ equation can be solved explicitly, $f^{(1)} = -\nu^{-1}\big( \partial_t^{(0)} + v \cdot \nabla_x \big) f^{(0)}$.
This gives Navier–Stokes equations with Prandtl number $1$.

Non-example: the Hilbert expansion also writes $f$ as a power series in $\varepsilon$.
But its coefficients are functions of $(t, x, v)$ not tied to the fluid fields, so it fails clause 1.
