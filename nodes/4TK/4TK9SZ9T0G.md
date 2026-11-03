---
tag: 4TK9SZ9T0G
kind: definition
name: Covariant Hamiltonian field theory
msc: [70S05, 70G45]
defines: 90XD2E09FD
uses: [CX4M8K61AB, 0E3G0GRPZ6, SANYJGZ311, ZQYMWVT1TT]
sources:
  - url: https://en.wikipedia.org/wiki/Hamiltonian_field_theory
---

## Definition

Let $Y \to X$ be a smooth [[fiber bundle|CX4M8K61AB]] over an oriented $n$-dimensional manifold $X$, with fibers of dimension $k$.
Use bundle coordinates $(x^\mu, y^i)$, $\mu = 1, \dots, n$, $i = 1, \dots, k$.
Let $\omega = dx^1 \wedge \cdots \wedge dx^n$ and $\omega_\mu = \iota_{\partial_\mu} \omega$, the contraction of $\omega$ with $\partial / \partial x^\mu$.

Let $V Y$ be the vertical tangent bundle of $Y$.

1. The *momentum phase space* is the Legendre bundle $\Pi \to Y$ with fiber $V^*_y Y \otimes T_x X \otimes \Lambda^n T^*_x X$ over $y \in Y$ above $x \in X$.
Its elements are $p^\mu_i \, dy^i \otimes \partial_\mu \otimes \omega$, and $(x^\mu, y^i, p^\mu_i)$ are coordinates on $\Pi$.
2. A *Hamiltonian form* is a [[differential form|0E3G0GRPZ6]] on $\Pi$ that reads in these coordinates
$$H = p^\mu_i \, dy^i \wedge \omega_\mu - \mathcal{H}(x^\nu, y^j, p^\nu_j) \, \omega,$$
for a smooth local function $\mathcal{H}$, the Hamiltonian density.
Here the first term is summed over $\mu$ and $i$.
3. For a section $x \mapsto (y^i(x), p^\mu_i(x))$ of $\Pi \to X$, its *covariant Hamilton equations* for $H$ are
$$\partial_\mu y^i = \frac{\partial \mathcal{H}}{\partial p^\mu_i}, \qquad \sum_{\mu = 1}^n \partial_\mu p^\mu_i = -\frac{\partial \mathcal{H}}{\partial y^i}.$$

*Covariant Hamiltonian field theory* is the study of the fields as solutions of the covariant Hamilton equations of a Hamiltonian form.

## Remarks

The function $\mathcal{H}$ depends on the chosen coordinates, but the form $H$ is a global object on $\Pi$; the covariant Hamilton equations do not depend on the coordinates.

A first-order [[Lagrangian density|SANYJGZ311]] $\mathcal{L}(x, y, z)$ with $z^i_\mu$ standing for $\partial_\mu y^i$ defines the Legendre map $p^\mu_i = \partial \mathcal{L} / \partial z^i_\mu$, a fiberwise [[Legendre transformation|ZQYMWVT1TT]].
If this map is a diffeomorphism, then $\mathcal{H} = p^\mu_i z^i_\mu - \mathcal{L}$, with $z$ expressed through $p$, defines a Hamiltonian form, and its covariant Hamilton equations are equivalent to the Euler–Lagrange equations of $\mathcal{L}$.

Example: let $X = \R^2$ with $\eta = \mathrm{diag}(1, -1)$, $Y = X \times \R$ and $\mathcal{H} = \frac{1}{2} \eta_{\mu\nu} p^\mu p^\nu$.
The equations read $\partial_\mu y = \eta_{\mu\nu} p^\nu$ and $\partial_\mu p^\mu = 0$, so $\eta^{\mu\nu} \partial_\mu \partial_\nu y = 0$, which is the wave equation $\partial_1^2 y - \partial_2^2 y = 0$.

Non-example: the canonical Hamiltonian formulation has one momentum $\pi(x)$ conjugate to $\partial_t \varphi$ at each point of space.
It is not of this form, because it splits spacetime into space and time and uses an infinite-dimensional phase space.
