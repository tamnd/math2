---
tag: T6WEFSKYHZ
kind: problem
name: Steklov eigenvalue problem
msc: [35P15, 35P05, 35J25]
uses: [0E0B6RA8K0, M4CEZ5K9HP, W783KDGT8E]
about: [W783KDGT8E]
sources:
  - url: https://en.wikipedia.org/wiki/Poincar%C3%A9%E2%80%93Steklov_operator
history:
  posed_by: "Vladimir Steklov"
  first_stated: "1902"
---

## Problem

Let $\Omega \subseteq \R^n$ be a bounded domain with Lipschitz boundary $\partial\Omega$ and outer unit normal $\nu$.
Find all $\sigma \in \R$ for which some nonzero $u \in H^1(\Omega)$ solves
$$\Delta u = 0 \text{ in } \Omega, \qquad \frac{\partial u}{\partial \nu} = \sigma u \text{ on } \partial\Omega,$$
in the weak sense.
Here $\Delta$ is the [[Laplacian|0E0B6RA8K0]] and $H^1(\Omega)$ is a [[Sobolev space|M4CEZ5K9HP]].
Such numbers $\sigma$ are the *Steklov eigenvalues* of $\Omega$, and one asks how they depend on the geometry of $\Omega$.

## Remarks

The Steklov eigenvalues are the eigenvalues of the [[Dirichlet-to-Neumann operator|W783KDGT8E]] of $\Omega$, which maps boundary values $f$ to the normal derivative of the harmonic extension of $f$.
They form a sequence $0 = \sigma_0 < \sigma_1 \le \sigma_2 \le \dots \to \infty$, and $\sigma_0 = 0$ belongs to the constant functions.
Example: for the unit disc, the functions $r^k \cos(k\theta)$ and $r^k \sin(k\theta)$ are harmonic with $\partial_r u = k u$ on the circle, so the eigenvalues are $0, 1, 1, 2, 2, 3, 3, \dots$.
Weinstock proved that among simply connected planar domains of given perimeter, the disc maximises $\sigma_1$.

## Explanations

### L1 human

Here the vibration happens only on the boundary, while the inside is in equilibrium.
The equation says that the flux across the edge is proportional to the value on the edge.
It models, for example, the sloshing of a liquid in a container and heat exchange through a surface.
