---
tag: JM6VKSD84P
kind: definition
name: Order parameter
msc: [82B26, 82B20]
defines: XSA203109Z
uses: [DG9F3W6MZM, R0KGM32QN6]
sources:
  - url: https://en.wikipedia.org/wiki/Phase_transition
---

## Definition

Let $\Omega$ be the configuration space of a lattice system, and let $K$ be a group acting on $\Omega$ that leaves the Hamiltonian invariant.
Let $V$ be a finite-dimensional real vector space with a linear representation $\rho$ of $K$.
Assume that $0$ is the only vector of $V$ fixed by all $\rho(k)$.
Let $f \colon \Omega \to V$ be a bounded observable with $f(k \omega) = \rho(k) f(\omega)$ for all $k \in K$ and $\omega \in \Omega$.
Let $\mu$ be an equilibrium state, that is an infinite-volume [[Gibbs measure|DG9F3W6MZM]].
The *order parameter* of $\mu$ is the vector $\langle f \rangle_\mu = \int f \, d\mu$ in $V$.
The state $\mu$ is *disordered* if $\langle f \rangle_\mu = 0$ and *ordered* if $\langle f \rangle_\mu \ne 0$.

## Remarks

If $\mu$ is invariant under $K$, then $\langle f \rangle_\mu = \rho(k) \langle f \rangle_\mu$ for all $k$, so $\langle f \rangle_\mu = 0$.
Hence an ordered state breaks the symmetry $K$.

Example: for the [[Ising model|R0KGM32QN6]] on $\Z^d$ with zero field, $K = \Z/2$ acts by the global flip $\sigma \mapsto -\sigma$, $V = \R$, $\rho$ is the sign representation and $f(\sigma) = \sigma_0$.
The flip sends $\sigma_0$ to $-\sigma_0$, so the equivariance holds.
The order parameter is the magnetization $\langle \sigma_0 \rangle$; at low temperature in the plus state it equals the spontaneous magnetization, which is positive for $d \ge 2$.

Non-example: the energy observable $f(\sigma) = \sigma_0 \sigma_{e_1}$ is unchanged by the flip.
The trivial representation fixes every vector, which fails the condition on $\rho$, and indeed $\langle \sigma_0 \sigma_{e_1} \rangle > 0$ at every temperature.

For the classical Heisenberg model, $K = SO(3)$ and the order parameter is a vector in $\R^3$.
