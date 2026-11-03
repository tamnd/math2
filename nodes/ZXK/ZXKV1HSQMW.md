---
tag: ZXKV1HSQMW
kind: statement
role: proposition
name: Biot–Savart law for vortex filaments
msc: [76B47, 76M23]
uses: [B3SXT9TWFA, BTHH4Y71QR, 2JZ0C15A9C, 0299VCW1TH, 0NF6GQNXMY]
about: [B3SXT9TWFA]
sources:
  - url: https://en.wikipedia.org/wiki/Biot%E2%80%93Savart_law
---

## Statement

Let $\mathbf{u}$ be a smooth velocity [[vector field|0299VCW1TH]] on $\R^3$ with $\nabla \cdot \mathbf{u} = 0$, as in [[incompressible flow|2JZ0C15A9C]], and with $\mathbf{u}(x) \to 0$ as $\abs{x} \to \infty$.
Let its [[vorticity|B3SXT9TWFA]] $\boldsymbol{\omega} = \nabla \times \mathbf{u}$, the [[curl|0NF6GQNXMY]] of $\mathbf{u}$, have compact support.
Then
$$\mathbf{u}(x) = \frac{1}{4\pi} \int_{\R^3} \frac{\boldsymbol{\omega}(y) \times (x - y)}{\abs{x - y}^3}\, dy \quad \text{for all } x \in \R^3.$$
Now let the vorticity be concentrated on an oriented smooth closed curve $C$, a vortex filament with [[circulation|BTHH4Y71QR]] $\Gamma$.
In this limit the induced velocity at a point $x \notin C$ is
$$\mathbf{u}(x) = \frac{\Gamma}{4\pi} \oint_C \frac{d\mathbf{l}(y) \times (x - y)}{\abs{x - y}^3}.$$

## Remarks

The idea of the proof: since $\nabla \cdot \mathbf{u} = 0$, one can write $\mathbf{u} = \nabla \times \mathbf{A}$ with $\nabla \cdot \mathbf{A} = 0$, so $-\Delta \mathbf{A} = \boldsymbol{\omega}$.
Solving with the Newtonian potential gives $\mathbf{A}(x) = \frac{1}{4\pi}\int \frac{\boldsymbol{\omega}(y)}{\abs{x - y}}\, dy$, and taking the curl gives the formula.
Uniqueness holds because the difference of two solutions is divergence-free, curl-free and decays at infinity, hence it is harmonic and zero.
Example: for a straight infinite filament along the $z$-axis, the formula gives the azimuthal speed $\Gamma / (2\pi r)$ at distance $r$, the velocity of a point vortex.
The filament formula diverges on the curve itself.
The self-induced velocity of a curved filament grows like the logarithm of one over the core radius, so a real vortex needs a core of finite size.

## Explanations

### L1 human

Swirling motion in one place sets the fluid moving everywhere else.
The Biot–Savart law says exactly how.
Each small piece of a vortex pushes the fluid around it, with a speed that falls off like one over the square of the distance.
It is the same formula as the one for the magnetic field of an electric current, with vorticity in place of current.
A straight vortex line makes the fluid circle around it, faster near the line and slower far away.

### L2 human

The law recovers the velocity from the vorticity, which is the key step in vortex methods and in the vorticity form of the Euler equations.
In aerodynamics it gives the downwash of the trailing vortices in lifting-line theory and the influence coefficients of the vortex lattice method.
For a finite straight segment it can be integrated in closed form, which makes it cheap to evaluate for networks of straight vortex pieces.
